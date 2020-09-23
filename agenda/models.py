from django.db import models

#------------------------------
# Variables de Opciones
#------------------------------

SI_NO = (
         ('Si','Si'),
         ('No', 'No'),
         )

TIPO_TELEFONO = (
                ('CP', 'Celular Personal'),
                ('CL', 'Celular Laboral'),
                ('LP', 'Linea Personal'),
                ('LL', 'Linea Laboral'),
        )



#------------------------------
# Clases
#------------------------------


class especialidad(models.Model):
    nombre = models.CharField(max_length=50)


class medicos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad_id = models.ForeignKey('especialidad', on_delete=models.CASCADE)
    tipo_celular_1 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono1 = models.CharField(max_length=60)
    tipo_celular_2 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono2 = models.CharField(max_length=60)

class obra_social(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    cuit = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

class turno(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_turno = models.DateTimeField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    asistio = models.CharField(max_length=2, choices=SI_NO, default='No')
    obra_social_id = models.ForeingKey(obra_social, on_delete=models.CASCADE)
    tipo_celular_1 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono1 = models.CharField(max_length=50)
    tipo_celular_2 = models.CharField(max_length=20, choices=TIPO_TELEFONO, default='CP')
    telefono2 = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=250)
    medicos_id = models.ForeignKey(medicos, on_delete=models.CASCADE)
    #campo user para asociar al seguimiento.
