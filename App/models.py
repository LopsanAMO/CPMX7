from django.db import models

class Empleadore(models.Model):
	#atributos
	nombres = models.CharField(max_length=120)
	apellidos = models.CharField(max_length=120)
	edad = models.IntegerField()
	trabajo = models.CharField(max_length=120)
	correo = models.CharField(max_length=120)
	imagen = models.ImageField(upload_to="imagenesPerfilEmpleadores")

	def __str__(self):
		return self.nombres

class Trabajo(models.Model):
	#atributos
	profesion = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)
	ubicacion = models.CharField(max_length=100, null=False, blank=False)
	fecha = models.DateTimeField(null=False, blank=False)
	pagoHora = models.CharField(null=False, blank=False)
	duracionHora = models.IntegerField(null=False, blank=False)
    calle = models.CharField(max_length=120, null=False, blank=False)
	numero = models.CharField(max_length=10, null=False, blank=False)
	colonia = models.CharField(max_length=200, null=False, blank=False)
	delegacionMunicipio = models.CharField(max_length=120, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
	tipoLugar = models.CharField(max_length=120, null=False, blank=False)

        def __str__(self):
            return self.descripcion
