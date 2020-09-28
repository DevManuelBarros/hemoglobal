from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),
    path('accounts/', include(('users.urls', 'users'), namespace='users')),
    path('agenda/', include(('agenda.urls', 'agenda'), namespace='agenda')),
    ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
