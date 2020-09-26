from django.urls import path

# especialidad
from .views import especialidad_create
from .views import especialidad_list
from .views import especialidad_update
# medicos
from .views import medicos_create
from .views import medicos_list
from .views import medicos_update
# obra social
from .views import obra_social_create
from .views import obra_social_list
from .views import obra_social_update
# turnos
from .views import turno_create
from .views import turno_list
from .views import turno_update
from .views import turno_detail
# ajax
from .ajax import cambiar_estado_turno

urlpatterns = [
                # especialidad
                path('especialidad/create/', especialidad_create.as_view(), name='especialidad_create'),
                path('especialidad/list/', especialidad_list.as_view(), name='especialidad_list'),
                path('especialidad/update/<int:pk>', especialidad_update.as_view(), name='especialidad_update'),
                # medicos
                path('medicos/create/', medicos_create.as_view(), name='medicos_create'),
                path('medicos/list/', medicos_list.as_view(), name='medicos_list'),
                path('medicos/update/<int:pk>', medicos_update.as_view(), name='medicos_update'),
                # obra sociales
                path('obra_social/create/', obra_social_create.as_view(), name='obra_social_create'),
                path('obra_social/list/', obra_social_list.as_view(), name='obra_social_list'),
                path('obra_social/update/<int:pk>', obra_social_update.as_view(), name='obra_social_update'),
                # turnos
                path('turno/create/', turno_create.as_view(), name='turno_create'),
                path('turno/list/', turno_list.as_view(), name='turno_list'),
                path('turno/update/<int:pk>', turno_update.as_view(), name='turno_update'),
                path('turno/detail/<int:pk>', turno_detail.as_view(), name='turno_detail'),
                # ajax
                path('cambiar_estado_turno/', cambiar_estado_turno, name='cambiar_estado_turno'),

        ]
