from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# imports app
from .forms import especialidad_form
from .forms import medicos_form

from .models import especialidad
from .models import medicos

#---------------------------------------
# Especialidad
#---------------------------------------

class especialidad_create(LoginRequiredMixin, CreateView):
	form_class = especialidad_form
	template_name = 'agenda/especialidad_create.html'
	success_url = reverse_lazy('index')


class especialidad_list(LoginRequiredMixin, ListView):
	model = especialidad

class especialidad_detail(LoginRequiredMixin, DetailView):
	model = especialidad

class especialidad_update(LoginRequiredMixin, UpdateView):
	pass

#-----------------------------------------
# Medicos
#-----------------------------------------

class medicos_form(LoginRequiredMixin, CreateView):
	template_name = 'agenda/especialidad_create.html'
	forms_class = medicos_form
	success_url = reverse_lazy('index')


