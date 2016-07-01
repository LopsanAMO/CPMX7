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

    STATE_CHOICES = sorted({
        ('AGU', 'Aguascalientes'), ('BCN', 'Baja California'),
        ('BCS', 'Baja California Sur'),
        ('CAM', 'Campeche'), ('CHH', 'Chihuahua'),
        ('CHP', 'Chiapas'), ('COA', 'Coahuila'),
        ('COL', 'Colima'),
        ('CDMX', 'Ciudad de Mexico'),
        ('DUR', 'Durango'), ('GRO', 'Guerrero'),
        ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'),
        ('JAL', 'Jalisco'), ('MEX', 'Estado de México'),
        ('MIC', 'Michoacán'), ('MOR', 'Morelos'),
        ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'),
        ('OAX', 'Oaxaca'), ('PUE', 'Puebla'),
        ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'),
        ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potosí'),
        ('SON', 'Sonora'), ('TAB', 'Tabasco'),
        ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'),
        ('VER', 'Veracruz'), ('YUC', 'Yucatán'),
        ('ZAC', 'Zacatecas')})

    DELEGACION_CHOICES = sorted({
        ('AGU', 'Aguascalientes'), ('BCN', 'Baja California'),
        ('BCS', 'Baja California Sur'),
        ('CAM', 'Campeche'), ('CHH', 'Chihuahua'),
        ('CHP', 'Chiapas'), ('COA', 'Coahuila'),
        ('COL', 'Colima'),
        ('CDMX', 'Ciudad de Mexico'),
        ('DUR', 'Durango'), ('GRO', 'Guerrero'),
        ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'),
        ('JAL', 'Jalisco'), ('MEX', 'Estado de México'),
        ('MIC', 'Michoacán'), ('MOR', 'Morelos'),
        ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'),
        ('OAX', 'Oaxaca'), ('PUE', 'Puebla'),
        ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'),
        ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potosí'),
        ('SON', 'Sonora'), ('TAB', 'Tabasco'),
        ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'),
        ('VER', 'Veracruz'), ('YUC', 'Yucatán'),
        ('ZAC', 'Zacatecas')})

    #atributos
    profesion = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)

    ubicacion = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    pagoHora = models.CharField(max_length=50,null=False, blank=False)
    duracionHora = models.IntegerField(null=False, blank=False)
    calle = models.CharField(max_length=120, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    colonia = models.CharField(max_length=200, null=False, blank=False)
    delegacionMunicipio = models.CharField(max_length=50,choices=DELEGACION_CHOICES,  null=True, blank=True)
    estado = models.CharField(max_length=50,choices=STATE_CHOICES,  null=True, blank=True)
    tipoLugar = models.CharField(max_length=120, null=False, blank=False)


    def __str__(self):
        return self.descripcion
