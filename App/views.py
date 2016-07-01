from django.shortcuts import render, redirect
from django.views.generic import View
from .send import mensajes

# Create your views here.

class Enviar(View):
    def get(self, request):
        template_name = 'cosa.html'
        return render(request, template_name)

    def post(self, request):
        template_name = 'hecho.html'
        template_error = 'error.html'
        mensae = request.POST.get('mensaje')
        try:
            mensajes(mensae)
            return render(request, template_name)
        except:
            return render(request, template_error)
