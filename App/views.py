from django.shortcuts import render, redirect
from django.views.generic import View
from .send import mensajes
from django.http import HttpResponse

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

class Home(View):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)

    def post(self,request):
        content = request.POST.get('Body')
        contenido = str(content)
        contenido = contenido.split(' ')
        msg1 = 'estas bien rica'
        msg2 = 'no estas bien rica'
        if contenido[0] == 'TRABAJO':
            mensajes(msg1)
        else:
            mensajes(msg2)
        print(contenido)
        return HttpResponse(request,content)
