from django.contrib import admin
from .models import *

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'cedula', 'phone_number',
                    'phone_number2', 'email', 'date_of_birth')
    search_fields = ('name', 'last_name', 'cedula')
