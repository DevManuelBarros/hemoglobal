from django.http import JsonResponse
from django.core.mail import EmailMessage

from .models import turno


def cambiar_estado_turno(request):
    turno_id = request.GET.get('pk')
    turno_id = turno.objects.filter(pk = turno_id).last()
    if turno_id.asistio == 'No':
        turno_id.asistio = 'Si'
    else:
        turno_id.asistio = 'No'
    response = {}
    turno_id.save()
    response['valor'] = str(turno_id.asistio)
    return JsonResponse(response)


def enviar_email(request):
    mensaje = request.GET.get('mensaje')
    mensaje = mensaje.replace('.', '.\n')
    paciente = 'Estimado/a ' + request.GET.get('paciente').strip() + ':\n\t     '
    mensaje =  paciente + mensaje
    to_email = request.GET.get('email')
    response = {}
    try:
        email = EmailMessage('Confirmación de Turno (Hemoglobal)', mensaje, to=[to_email])
        email.send()
        response['valor'] = 'Se ha enviado correctamente el email a {}'.format(to_email)
    except:
        response['valor'] =  'Ha surgido un error al enviar el email'
    return JsonResponse(response)
        
    



