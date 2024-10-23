from django.shortcuts import render
from .models import PetsTypes
from django.http import HttpResponse

# Create your views here.

def pets_types(request):
    if request.method == 'GET':
        tmp = PetsTypes.objects.all().order_by('name') #Сортировка по имени
        items = [str(item) for item in tmp]

    return HttpResponse(','.join(items))