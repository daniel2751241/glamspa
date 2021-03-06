from .views import *
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexView.as_view()),
    path('inicio', IndexView.as_view()),
    path('nosotros', NosotrosView.as_view(), name='nosotros'),
    path('sedes', SedesView.as_view(), name='sedes'),
    path('contacto', ContactoView.as_view(), name='contacto'),
    path('garantias', GarantiasView.as_view(), name='garantias'),
    # Seminarios
    path('seminarios/micropigmentacion-completa', MicropigmentacionCompletaView.as_view()),
    path('seminarios/lifting-de-pestanas', LiftingPestanasView.as_view()),
    path('seminarios/diseno-de-cejas', DisenoCejasView.as_view()),
    path('seminarios/microblading', MicroblandingView.as_view()),
    # Servicios Cejas
    path('servicios/diseno-de-cejas-con-cera', CejasCeraView.as_view()),

    path('servicios/efecto-polvo',
         TemplateView.as_view(template_name='servicios/cejas/efecto-polvo.html')),
    path('servicios/diseno-de-cejas-con-hilo',
         TemplateView.as_view(template_name='servicios/cejas/cejas-con-hilo.html')),
    path('servicios/mapa-de-cejas',
         TemplateView.as_view(template_name='servicios/cejas/mapa-cejas.html')),
    path('servicios/maquillaje-de-cejas',
         TemplateView.as_view(template_name='servicios/cejas/maquillaje-cejas.html')),
    path('servicios/micropigmentacion',
         TemplateView.as_view(template_name='servicios/cejas/micropigmentacion.html')),
    path('servicios/valoracion-micropigmentacion',
         TemplateView.as_view(template_name='servicios/cejas/valoracion-micropigmentacion.html')),
    path('servicios/microblading',
         TemplateView.as_view(template_name='servicios/cejas/microblading.html')),
    path('servicios/microshading',
         TemplateView.as_view(template_name='servicios/cejas/microshading.html')),
    path('servicios/cejas-compacta',
         TemplateView.as_view(template_name='servicios/cejas/cejas-compacta.html')),
    path('servicios/laminado-cejas',
         TemplateView.as_view(template_name='servicios/cejas/laminado-cejas.html')),
    path('servicios/correcion-tatuajes-cejas',
         TemplateView.as_view(template_name='servicios/cejas/correcion-tatuajes-cejas.html')),
    path('servicios/borrado-tatuajes-ceja',
         TemplateView.as_view(template_name='servicios/cejas/borrado-tatuajes-ceja.html')),
    # Servicios pestanas
    path('servicios/lifting-pestanas',
         TemplateView.as_view(template_name='servicios/pestanas/lifting-pestanas.html')),
    path('servicios/pestanas-punto-punto',
         TemplateView.as_view(template_name='servicios/pestanas/pestanas-punto-punto.html')),
    path('servicios/extension-pestanas',
         TemplateView.as_view(template_name='servicios/pestanas/extension-pestanas.html')),
    path('servicios/clasica-efecto-pestanina',
         TemplateView.as_view(template_name='servicios/pestanas/clasica-efecto-pestanina.html')),
    path('servicios/extension-tipo-seda',
         TemplateView.as_view(template_name='servicios/pestanas/extension-tipo-seda.html')),
    path('servicios/volumen-ruso',
         TemplateView.as_view(template_name='servicios/pestanas/volumen-ruso.html')),
    path('servicios/retoque-pestanas',
         TemplateView.as_view(template_name='servicios/pestanas/retoque-pestanas.html')),
    path('servicios/retoque-pestanas-clasicas',
         TemplateView.as_view(template_name='servicios/pestanas/retoque-pestanas-clasicas.html')),
    path('servicios/retoque-tipo-seda',
         TemplateView.as_view(template_name='servicios/pestanas/retoque-tipo-seda.html')),
    path('servicios/retoque-volumen-ruso',
         TemplateView.as_view(template_name='servicios/pestanas/retoque-volumen-ruso.html')),
    path('servicios/retiro-extension-pestanas',
         TemplateView.as_view(template_name='servicios/pestanas/retiro-extension-pestanas.html')),
    # Servicios depilacion corporal
    path('servicios/depilacion-corporal',
         TemplateView.as_view(template_name='servicios/corporal/mujeres.html')),
    path('servicios/hombres',
         TemplateView.as_view(template_name='servicios/corporal/hombres.html')),
    # Servicios depilacion facial
    path('servicios/rostro-completo-cera',
         TemplateView.as_view(template_name='servicios/facial/completo-cera.html')),
    path('servicios/rostro-completo-hilo',
         TemplateView.as_view(template_name='servicios/facial/completo-hilo.html')),
    # Servicios pedicure
    path('servicios/pedicure-tradicional',
         TemplateView.as_view(template_name='servicios/pedicure/pedicure-tradicional.html')),
    path('servicios/pedicure-semipermanente',
         TemplateView.as_view(template_name='servicios/pedicure/pedicure-semipermanente.html')),
    path('servicios/pedicure-chocolaterapia',
         TemplateView.as_view(template_name='servicios/pedicure/chocolaterapia.html')),
    path('servicios/pedicure-parafina',
         TemplateView.as_view(template_name='servicios/pedicure/parafina.html')),
    path('servicios/pedicure-vitamina-e',
         TemplateView.as_view(template_name='servicios/pedicure/vitamina-e.html')),
    path('servicios/pedicure-aromaterapia',
         TemplateView.as_view(template_name='servicios/pedicure/aromaterapia.html')),
    path('servicios/pedicure-veloterapia',
         TemplateView.as_view(template_name='servicios/pedicure/veloterapia.html')),
    path('servicios/desintoxicacion',
         TemplateView.as_view(template_name='servicios/pedicure/desintoxicacion.html')),
    path('servicios/pediluvio',
         TemplateView.as_view(template_name='servicios/pedicure/pediluvio.html')),
    path('servicios/bombas-sales',
         TemplateView.as_view(template_name='servicios/pedicure/bombas-sales.html')),
    # Servicios manicure
    path('servicios/manicure-tradicional',
         TemplateView.as_view(template_name='servicios/manicure/tradicional.html')),
    path('servicios/manicure-semipermanente',
         TemplateView.as_view(template_name='servicios/manicure/semipermanente.html')),
    path('servicios/dipping-powder',
         TemplateView.as_view(template_name='servicios/manicure/dipping-powder.html')),
    path('servicios/manicure-ruso',
         TemplateView.as_view(template_name='servicios/manicure/ruso.html')),
    path('servicios/acrilicas-esculpidas',
         TemplateView.as_view(template_name='servicios/manicure/acrilicas-esculpidas.html')),
    path('servicios/esmaltado-tradicional',
         TemplateView.as_view(template_name='servicios/manicure/esmaltado-tradicional.html')),
    path('servicios/puntas-y-estructuras',
         TemplateView.as_view(template_name='servicios/manicure/puntas-y-estructuras.html')),
    path('servicios/esmaltado-semipermanente',
         TemplateView.as_view(template_name='servicios/manicure/esmaltado-semipermanente.html')),
    path('servicios/unas-tips',
         TemplateView.as_view(template_name='servicios/manicure/unas-tips.html')),
    path('servicios/recubrimiento-acrilico',
         TemplateView.as_view(template_name='servicios/manicure/recubrimiento-acrilico.html')),
    path('servicios/mantenimiento-unas',
         TemplateView.as_view(template_name='servicios/manicure/mantenimiento-unas.html')),
    path('servicios/recubrimiento-acrilico',
         TemplateView.as_view(template_name='servicios/manicure/recubrimiento-acrilico.html')),
    path('servicios/retirado-unas',
         TemplateView.as_view(template_name='servicios/manicure/retirado-unas.html')),
    path('servicios/manicure-chocolaterapia',
         TemplateView.as_view(template_name='servicios/manicure/chocolaterapia.html')),
    path('servicios/manicure-parafina',
         TemplateView.as_view(template_name='servicios/manicure/parafina.html')),
    path('servicios/manicure-vitamina-e',
         TemplateView.as_view(template_name='servicios/manicure/vitamina-e.html')),
    path('servicios/manicure-aromaterapia',
         TemplateView.as_view(template_name='servicios/manicure/aromaterapia.html')),
    path('servicios/manicure-veloterapia',
         TemplateView.as_view(template_name='servicios/manicure/veloterapia.html')),
    path('servicios/manicure-retirado-semipermanente',
         TemplateView.as_view(template_name='servicios/manicure/retirado-semipermanente.html')),
]

