from django.apps import AppConfig
from django.contrib import algoliasearch
from .index import TrabajoIndex
class AppConfig(AppConfig):
    name = 'App'

    def ready(self):
        Trabajo = self.get_model('trabajo')
        algoliasearch.register(Trabajo, TrabajoIndex)