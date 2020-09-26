from django.http import JsonResponse

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





