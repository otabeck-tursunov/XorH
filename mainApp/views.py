from django.shortcuts import render
from .models import *


def index(request):
    search = request.GET.get('search')
    togrilar = TogriSoz.objects.filter(soz=search)
    if togrilar and search:
        togriSoz = togrilar[0]
        notogriSozlar = NotogriSoz.objects.filter(t_soz=togriSoz)
        context = {
            'togriSoz': togriSoz,
            'notogriSozlar': notogriSozlar
        }
        return render(request, 'index.html', context)
    elif search:
        notogriSozlar = NotogriSoz.objects.filter(soz=search)
        if notogriSozlar:
            togriSoz = TogriSoz.objects.get(id=notogriSozlar[0].t_soz.id)
            notogriSozlar = NotogriSoz.objects.filter(t_soz=togriSoz)
            context = {
                'togriSoz': togriSoz,
                'notogriSozlar': notogriSozlar
            }
            return render(request, 'index.html', context)
    return render(request, 'index.html')

