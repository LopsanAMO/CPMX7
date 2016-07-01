from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

from django.contrib.algoliasearch import raw_search
import json

from .models import Trabajo
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

class Home(View):
	def get(self, request):
		template_name = 'index.html'
		return render(request, template_name)

	def post(self,request):
		content = request.POST.get('Body')
		contenido = str(content)
		print('contenido: ' + contenido)
		msg1 = 'estas bien rica'
		msg2 = 'no estas bien rica'
		params = { "hitsPerPage": 5 }
		json_data = raw_search(Trabajo, contenido, params)
		
		job_name = json_data["hits"][0]["profesion"]
		job_phone = json_data["hits"][0]["telefono"]
		job_money = (json_data["hits"][0]["pagoHora"]) * 8 * 20

		print(job_money + job_phone + job_money)
		contenido = contenido.split(' ')
		if contenido[0] == 'TRABAJO':
			mensajes(msg1)
			#try:
			#    trabajos = Trabajo.objects.get(colonia=contenido[1])
			#except:
			#    try:
			#        trabajos = Trabajo.objects.get(delegacionMunicipio=contenido[1])
			#    except:
			#        try:
			#            trabajos = Trabajo.objects.get(estado=contenido[1])
			#        except:
		else:
			mensajes(msg2)
		print(contenido)
		return HttpResponse(request,content)
