from django.contrib.algoliasearch import AlgoliaIndex

class TrabajoIndex(AlgoliaIndex):
	fields = 'profesion', 'descripcion', 'fecha', 'pagoHora', 'duracionHora', 'calle', 'numero', 
				'colonia', 'delegacionMunicipio', 'estado', 'tipoLugar', 'telefono'
	settings = {'attributesToIndex': ('profesion', 'descripcion', 'fecha', 'pagoHora', 'duracionHora', 'calle', 'numero'
				'colonia', 'delegacionMunicipio', 'estado', 'tipoLugar', 'telefono')}