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
from .forms import obra_social_form
from .forms import turno_form
from .forms import paciente_form
from .forms import informe_consulta_form


from .models import especialidad
from .models import medicos
from .models import obra_social
from .models import turno
from .models import paciente
from .models import informe_consulta

#---------------------------------------
# Especialidad
#---------------------------------------

class especialidad_create(LoginRequiredMixin, CreateView):
	form_class = especialidad_form
	template_name = 'agenda/especialidad_create.html'
	success_url = reverse_lazy('agenda:especialidad_list')


class especialidad_list(LoginRequiredMixin, ListView):
	model = especialidad

class especialidad_update(LoginRequiredMixin, UpdateView):
	model = especialidad
	form_class = especialidad_form
	template_name = 'agenda/especialidad_update.html'
	success_url = reverse_lazy('agenda:especialidad_list')

#-----------------------------------------
# Medicos
#-----------------------------------------

class medicos_create(LoginRequiredMixin, CreateView):
	template_name = 'agenda/medicos_create.html'
	form_class = medicos_form
	success_url = reverse_lazy('agenda:medicos_list')

class medicos_list(LoginRequiredMixin, ListView):
	model = medicos

class medicos_update(LoginRequiredMixin, UpdateView):
	model = medicos
	template_name = 'agenda/medicos_update.html'
	form_class = medicos_form
	success_url = reverse_lazy('agenda:medicos_list')

#-----------------------------------------
# Obra Social
#-----------------------------------------

class obra_social_create(LoginRequiredMixin, CreateView):
	template_name = 'agenda/obra_social_create.html'
	form_class = obra_social_form
	success_url = reverse_lazy('agenda:obra_social_list')

class obra_social_list(LoginRequiredMixin, ListView):
	model = obra_social

class obra_social_update(LoginRequiredMixin, UpdateView):
	model = obra_social
	template_name = 'agenda/obra_social_update.html'
	form_class = obra_social_form
	success_url = reverse_lazy('agenda:obra_social_list')

#---------------------------------------
# Paciente
#---------------------------------------

class paciente_create(LoginRequiredMixin, CreateView):
	template_name = 'agenda/paciente_create.html'
	form_class = paciente_form
	success_url = reverse_lazy('agenda:paciente_list')

class paciente_list(LoginRequiredMixin, ListView):
	model = paciente

class paciente_update(LoginRequiredMixin, UpdateView):
	model = paciente
	template_name = 'agenda/paciente_update.html'
	form_class = paciente_form
	success_url = reverse_lazy('agenda:paciente_list')

class paciente_detail(LoginRequiredMixin, DetailView):
	model = paciente
	template_name = 'agenda/paciente_detail.html'


#---------------------------------------
# Turnos
#---------------------------------------

class turno_create(LoginRequiredMixin, CreateView):
	template_name = 'agenda/turno_create.html'
	form_class = turno_form
	success_url = reverse_lazy('agenda:turno_list')

class turno_list(LoginRequiredMixin, ListView):
	model = turno

class turno_update(LoginRequiredMixin, UpdateView):
	model = turno
	template_name = 'agenda/turno_update.html'
	form_class = turno_form
	success_url = reverse_lazy('agenda:turno_list')

class turno_detail(LoginRequiredMixin, DetailView):
	model = turno
	template_name = 'agenda/turno_detail.html'

#---------------------------------------
# Informe consulta
#---------------------------------------

