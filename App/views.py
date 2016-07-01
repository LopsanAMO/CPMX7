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


def send_form(query):
	params = { "hitsPerPage": 5 }
	json_data = raw_search(Trabajo, query, params)
	json_array = json_data["hits"]
	for x in range(0,4):
		if(len(json_array) == 0 and x == 0):
			mensajes("No encontramos trabajos para ti :c intenta mas tarde c:")
			break
		if(len(json_array) > x):
			job_name = json_array[x]["profesion"]
			job_phone = json_array[x]["telefono"]
			job_money = int((json_array[x]["pagoHora"])) * 8 * 20
			job_message = "Trabajo: " + job_name +  " Telefono: " + job_phone + " Salario: " + str(job_money)
			mensajes(job_message)	

class Home(View):
	def get(self, request):
		template_name = 'index.html'
		return render(request, template_name)

	def post(self,request):
		content = request.POST.get('Body')
		contenido = str(content)		
		send_form(contenido)
		
		return HttpResponse(request,content)
