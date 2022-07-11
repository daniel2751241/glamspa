from django.shortcuts import render
from app.models import Slide
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['slides'] = Slide.objects.all()
        return context

class NosotrosView(TemplateView):
    template_name = 'nosotros.html'

class SedesView(TemplateView):
    template_name = 'sedes.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'

# Seminarios
class MicropigmentacionCompletaView(TemplateView):
    template_name = 'seminarios/micropigmentacion-completa.html'

class MicroblandingView(TemplateView):
    template_name = 'seminarios/microblanding.html'

class LiftingPestanasView(TemplateView):
    template_name = 'seminarios/lifting-de-pestanas.html'

class DisenoCejasView(TemplateView):
    template_name = 'seminarios/diseno-de-cejas.html'

# Servicios
class CejasCeraView(TemplateView):
    template_name = 'servicios/cejas/cejas-cera.html'

# Garantías
class GarantiasView(TemplateView):
    template_name = 'garantias/garantias.html'
