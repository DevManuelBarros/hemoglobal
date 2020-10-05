from django.contrib import admin
from .models import especialidad
from .models import medicos
from .models import obra_social
from .models import turno
from .models import usuario
from .models import paciente

admin.site.register(especialidad)
admin.site.register(medicos)
admin.site.register(obra_social)
admin.site.register(turno)
admin.site.register(usuario)
admin.site.register(paciente)
