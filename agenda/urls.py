from django.urls import path


from .views import especialidad_create
from .views import especialidad_list
from .views import especialidad_update
from .views import especialidad_detail

urlpatterns = [
                # especialidad
                path('especialidad/create/', especialidad_create.as_view(), name='especialidad_create'),
                path('especialidad/list/', especialidad_list.as_view(), name='especialidad_list'),
                path('especialidad/update/', especialidad_update.as_view(), name='especialidad_update'),
                path('especialidad/detail/', especialidad_detail.as_view(), name='especialidad_detail'),
                # medicos
        ]
