from django.shortcuts import render, redirect
from django.views.generic import View
from .send import mensajes
from django.views.decorators.csrf import csrf_exempt
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

    @csrf_exempt
    def post(request):
        if request.method == 'POST':
            content = request.POST.get('body')
            print('-------------')
            print(content)
            return HttpResponse(content)
