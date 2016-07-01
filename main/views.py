from django.shortcuts import render
from django.views.generic import TemplateView


class indexView(TemplateView):
    template_name = 'main/index.html'


class jobsView(TemplateView):
    template_name = 'main/jobs.html'
