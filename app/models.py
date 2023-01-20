from django.db import models

class Slide(models.Model):
    image = models.ImageField('imagen', upload_to='images/slides')

    def __str__(self):
        return f'Slide #{self.pk}'

class Client(models.Model):
    name = models.CharField('nombres', max_length=40)
    last_name = models.CharField('apellidos', max_length=40)
    date_of_birth = models.DateField('fecha de nacimiento', null=True, blank=True)
    email = models.EmailField(blank=True)
    cedula = models.CharField('cedula', max_length=40, blank=True)
    phone_number = models.CharField('teléfono', max_length=40, blank=True)
    phone_number2 = models.CharField('celular', max_length=40, blank=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return f'{self.name} {self.last_name}'
