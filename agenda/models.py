from django.db import models
from datetime import datetime
from datetime import timedelta


#------------------------------
# Cumston QuerySet
#------------------------------

class turno_manager(models.Manager):
	def proximos_turnos(self):
		ahora = datetime.utcnow()
		turnos = self.filter(fecha_turno__gte=ahora, fecha_turno__lte=ahora + timedelta(days=7))
		return turnos



#------------------------------
# Variables de Opciones
#------------------------------

SI_NO = (
         ('Si','Si'),
         ('No', 'No'),
         ('Cancelado', 'Cancelado'),
         ('Postergado', 'Postergado'),
         )

TIPO_TELEFONO = (
                ('CP', 'Celular Personal'),
                ('CL', 'Celular Laboral'),
                ('LP', 'Linea Personal'),
                ('LL', 'Linea Laboral'),
        )

#------------------------------
# Campos
#------------------------------
class especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class medicos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad_id = models.ForeignKey(especialidad, on_delete=models.CASCADE)
    tipo_celular_1 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono1 = models.CharField(max_length=60, blank=True)
    tipo_celular_2 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono2 = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.apellido + ', ' + self.nombre

class obra_social(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    cuit = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)
    numero_de_afiliado = models.CharField(max_length=50, default='Sin datos')
    obra_social_id = models.ForeignKey(obra_social, on_delete=models.CASCADE)
    tipo_celular_1 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono1 = models.CharField(max_length=50, blank=True)
    tipo_celular_2 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono2 = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.apellido + ', ' + self.nombre

class turno(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_turno = models.DateTimeField(null=True, blank=True)
    paciente_id = models.ForeignKey(paciente, blank=True, on_delete=models.CASCADE)
    asistio = models.CharField(max_length=10, choices=SI_NO, default='No')
    observaciones = models.CharField(max_length=250)
    medicos_id = models.ForeignKey(medicos, on_delete=models.CASCADE)
    asignado = models.ForeignKey(usuario, on_delete=models.CASCADE, blank=True)
    objects = turno_manager()

class informe_consulta(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    turno_id = models.ForeignKey(turno, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=250)