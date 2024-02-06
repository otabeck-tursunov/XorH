from django.shortcuts import render
from .models import *


def index(request):
    search = request.GET.get('search')
    togrilar = TogriSoz.objects.filter(soz=search)
    if togrilar:
        togriSoz = togrilar[0]
        notogriSozlar = NotogriSoz.objects.filter(t_soz=togriSoz)
        context = {
            'togriSoz': togriSoz,
            'notogriSozlar': notogriSozlar
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')