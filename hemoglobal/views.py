from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from agenda.models import turno

class index(LoginRequiredMixin, ListView):
    model = turno
    template_name = 'index.html'
    def get_queryset(self):
        queryset = turno.objects.proximos_turnos()
        return queryset
    
