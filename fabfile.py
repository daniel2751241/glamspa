from fabric import Connection, task
from patchwork.files import exists
from invoke import Responder
from getpass import getpass
import os

# Pasos para hacer depoloy
# 1. fab --prompt-for-login-password -H {HOST} deploy
# 2. fab --prompt-for-login-password -H root-promedios setup-server

USER = 'cejasspabogota'
BASE_DIR = f'/home/{USER}/repositories'
PROJECT_FOLDER = 'cejas'
GIT_URl = 'https://gitlab.com/promd/cejas.git'
WRK_DIRECTORY = os.path.join(BASE_DIR, PROJECT_FOLDER)
DOMAIN = 'cejasspabogota.com'
SERVICE_FILE = 'django-cejas.service'

gituser = Responder(
    pattern=r'Username for ',
    response=input('Usuario de git: ') + '\n'
)

gitpass = Responder(
    pattern=r'Password for ',
    response=getpass('Contrasena de git: ') + '\n'
)

@task
def git_clone(c):
    if not exists(c, BASE_DIR):
        c.run(f'mkdir -p {BASE_DIR}')
    c.run(f'cd {BASE_DIR} && git clone {GIT_URl} {PROJECT_FOLDER}', pty=True,
          watchers=[gitpass, gituser])
    if not exists(c, os.path.join(WRK_DIRECTORY, '.env')):
        c.run(f'cd {WRK_DIRECTORY} && cp .env.example .env ')


@task
def update_files(c):
    c.run(f'cd {WRK_DIRECTORY} && git pull origin master', pty=True,
          watchers=[gitpass, gituser])

@task
def install_dependencies(c):
    c.run('~/.local/bin/poetry config settings.virtualenvs.in-project true')
    c.run(f'cd {WRK_DIRECTORY} && ~/.local/bin/poetry install')
    c.run(f'cd {WRK_DIRECTORY}')
    c.run(f'chmod +x {WRK_DIRECTORY}/.venv/bin/uwsgi')

@task
def upload_conf_files(c):
    service_file = f'/etc/systemd/system/{SERVICE_FILE}'
    include_folder = lambda x: f'/etc/apache2/conf.d/userdata/{x}/2_4/{USER}/{DOMAIN}'
    if not exists(c, service_file):
        c.put(f'confs/{SERVICE_FILE}', service_file)
    if not exists(c, include_folder('std')):
        c.run(f'mkdir -p {include_folder("std")}')
        c.run(f'mkdir -p {include_folder("ssl")}')
        c.put('confs/extra.conf', os.path.join(include_folder('std'),
                                               'extra.conf'))
        c.run(f'ln -s {include_folder("std")} {include_folder("ssl")}')

@task
def restart_services(c):
    c.run('/usr/local/cpanel/scripts/rebuildhttpdconf')
    c.run('/usr/local/cpanel/scripts/restartsrv_httpd')
    c.run(f'systemctl daemon-reload && systemctl start {SERVICE_FILE}')

@task
def deploy(c):
    print('Deploying')
    git_clone(c)
    install_dependencies(c)
    print('Deploy realizado correctamente.')
    print(f'Verifique http://{DOMAIN}/')

@task
def setup_server(c):
    upload_conf_files(c)
    restart_services(c)
    print('Servidor configurado correctamente. Proceda a realizar el deploy.')
