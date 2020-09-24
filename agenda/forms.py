from django import forms

from .models import especialidad, medicos, obra_social, turno


class_control = {'class' : 'form-control'}

class especialidad_form(forms.ModelForm):
    class Meta:
        model = especialidad
        fields = ('__all__')
        widgets = {
                    'nombre' : forms.TextInput(attrs=class_control),
        }


class medicos_form(forms.ModelForm):
    class Meta:
        model = medicos
        fields = ('__all__')
        widgets = {
                    'nombre' : forms.TextInput(attrs=class_control),
                    'apellido' : forms.TextInput(attrs=class_control),
                    'especialidad_id' : forms.Select(attrs=class_control),
                    'tipo_celular_1' : forms.Select(attrs=class_control),
                    'telefono1' : forms.TextInput(attrs=class_control),
                    'tipo_ceclular_2' : forms.Select(attrs=class_control),
                    'telefono2' : forms.TextInput(attrs=class_control)
                    }

class obra_social_form(forms.ModelForm):
    class Meta:
        model = obra_social
        fields = ('__all__')
        widgets = {
                    'nombre' : forms.TextInput(attrs=class_control),
                    'direccion' : forms.TextInput(attrs=class_control),
                    'cuit' : forms.TextInput(attrs=class_control),
                    'telefono' : forms.TextInput(attrs=class_control)
                    }

class turno_form(forms.ModelForm):
    class Meta:
        model = turno
        fields = ('fecha_turno', 'nombre', 'apellido', 'obra_social_id', 'numero_de_afiliado', 'tipo_celular_1',
                  'telefono1', 'tipo_celular_2', 'telefono2', 'email', 'observaciones',
                  'medicos_id', 'asignado')
        widgets = {
                    'fecha_turno' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'datetime-local' }),
                    'nombre' : forms.TextInput(attrs=class_control),
                    'apellido' : forms.TextInput(attrs=class_control),
                    'obra_social_id' : forms.Select(attrs=class_control),
                    'numero_de_afiliado' : forms.TextInput(attrs=class_control),
                    'tipo_celular_1' : forms.Select(attrs=class_control),
                    'telefono1' : forms.TextInput(attrs=class_control),
                    'tipo_celular_2' : forms.Select(attrs=class_control),
                    'telefono2' : forms.TextInput(attrs=class_control),
                    'email' : forms.EmailInput(attrs=class_control),
                    'observaciones' : forms.TextInput(attrs=class_control),
                    'medicos_id' : forms.Select(attrs=class_control),
                    'asignado' : forms.Select(attrs=class_control),
                    }
