from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('agenda/', include(('agenda.urls', 'agenda'), namespace='agenda')),
    ]
