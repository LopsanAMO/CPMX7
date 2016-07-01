from django.contrib import admin
from .models import Trabajo 

# Register your models here.
@admin.register(Trabajo)

class adminTrabajo(admin.ModelAdmin):
    list_display = ('colonia',)
