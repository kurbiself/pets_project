from django.shortcuts import render
from .models import PetsTypes, Breeds, PetsOwners, Pets
from django.http import HttpResponse, JsonResponse
from django import forms
from .forms import PetsFilter
from .serializers import (
    PetsOwnersSerializer,
    PetsTypesSerializer,
    BreedsSerializer,
    PetsSerializer,
)
from rest_framework.parsers import JSONParser
from rest_framework import generics, viewsets
from django.views.decorators.csrf import csrf_exempt


class PetsTypesViewsSet(viewsets.ModelViewSet):
    serializer_class = PetsTypesSerializer

    def get_queryset(self):
        name_filter = self.request.query_params.get("name")
        if name_filter:
            return PetsTypes.objects.filter(name__icontains=name_filter)
        else:
            return PetsTypes.objects.all()


class BreedsViewsSet(viewsets.ModelViewSet):
    serializer_class = BreedsSerializer

    def get_queryset(self):
        data = self.request.data
        t = data.get("type")
        if t:
            return Breeds.objects.filter(type=t)
        else:
            return Breeds.objects.all()


class PetsTypesList(generics.ListAPIView):
    serializer_class = PetsTypesSerializer

    def get_queryset(self):
        name_filter = self.request.query_params.get("name")
        if name_filter:
            return PetsTypes.objects.filter(name__icontains=name_filter)
        else:
            return PetsTypes.objects.all()


class PetsTypesMixin:
    queryset = PetsTypes.objects.all().order_by("name")
    serializer_class = PetsTypesSerializer


class PetsTypesListView(PetsTypesMixin, generics.ListAPIView):
    pass


class PetsTypesCreateView(PetsTypesMixin, generics.CreateAPIView):
    pass


class PetsTypesUpdateView(PetsTypesMixin, generics.UpdateAPIView):
    pass


class PetsTypesDestroyView(PetsTypesMixin, generics.DestroyAPIView):
    pass


class PetsTypesRetrieveView(PetsTypesMixin, generics.RetrieveAPIView):
    pass


# Create your views here.
@csrf_exempt
def pets_types(request):
    if request.method == "GET":
        items = PetsTypes.objects.all().order_by("name")  # Сортировка по имени
        serializer = PetsTypesSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PetsTypesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=204)


@csrf_exempt
def pet_type(request, pk):
    try:
        item = PetsTypes.objects.get(pk=pk)
    except PetsTypes.DoesNotExist as e:
        return HttpResponse(content=e, status=404)
    if request.method == "GET":
        serializer = PetsTypesSerializer(item, many=False)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PetsTypesSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)


def pets_types_view(request):
    template_name = "pets_list/pets_types.html"
    if request.method == "GET":
        tmp = PetsTypes.objects.all().order_by("name")  # Сортировка по имени
        items = [str(item) for item in tmp]  # получили строковое представление объекта
    context = {"title": "Типы животных", "data": items}
    # return HttpResponse(','.join(items))
    return render(request, template_name, context)


@csrf_exempt
def breeds(request):
    if request.method == "GET":
        items = Breeds.objects.all().order_by("name")  # Сортировка по имени
        serializer = BreedsSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BreedsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=204)


@csrf_exempt
def breed(request, pk):
    try:
        item = Breeds.objects.get(pk=pk)
    except Breeds.DoesNotExist as e:
        return HttpResponse(content=e, status=404)
    if request.method == "GET":
        serializer = BreedsSerializer(item, many=False)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BreedsSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)


def breeds_view(request, pk=None):
    template_name = "pets_list/breeds.html"
    if request.method == "GET":
        if pk:
            tmp = Breeds.objects.get(id=pk)
            items = [tmp]
        else:
            tmp = Breeds.objects.all().order_by("name")
            items = list(tmp)
    context = {"title": "Породы", "data": items}
    return render(request, template_name, context)


@csrf_exempt
def pets_owners(request):
    if request.method == "GET":
        items = PetsOwners.objects.all().order_by("name")  # Сортировка по имени
        serializer = PetsOwnersSerializer(items, many=True)
        return JsonResponse(
            serializer.data, safe=False, status=200
        )  # safe = False - принимает любой объект
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PetsOwnersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=204)


@csrf_exempt
def pets_owner(request, pk):
    try:
        item = PetsOwners.objects.get(pk=pk)
    except PetsOwners.DoesNotExist as e:
        return HttpResponse(content=e, status=404)
    if request.method == "GET":
        serializer = PetsOwnersSerializer(item, many=False)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PetsOwnersSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)


def pets_owners_view(request, pk=None):
    template_name = "pets_list/pets_owners.html"
    if request.method == "GET":
        if pk:
            tmp = PetsOwners.objects.get(id=pk)
            items = [tmp]
        else:
            tmp = PetsOwners.objects.all().order_by("name")
            items = list(tmp)
    context = {"title": "Хозяева", "data": items}
    return render(request, template_name, context)


@csrf_exempt
def pets(request):
    if request.method == "GET":
        items = Pets.objects.all().order_by("name")  # Сортировка по имени
        serializer = PetsSerializer(items, many=True)
        return JsonResponse(
            serializer.data, safe=False, status=200
        )  # safe = False - принимает любой объект
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=204)


@csrf_exempt
def pet(request, pk):
    try:
        item = Pets.objects.get(pk=pk)
    except PetsOwners.DoesNotExist as e:
        return HttpResponse(content=e, status=404)
    if request.method == "GET":
        serializer = PetsSerializer(item, many=False)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PetsSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)


def pets_view(request, pk=None):
    template_name = "pets_list/pets.html"
    form = PetsFilter(request.GET or None)
    context = {"form": form}
    if request.method == "GET":
        if form.is_valid() and (
            form.cleaned_data["pet_name"] != ""
            or form.cleaned_data["owner_name"] != ""
            or form.cleaned_data["birthday"] is not None
        ):
            tmp = Pets.objects
            if form.cleaned_data["pet_name"]:
                tmp = tmp.filter(name__icontains=form.cleaned_data["pet_name"])
                # items = list(tmp)
            if form.cleaned_data["birthday"]:
                tmp = tmp.filter(birth=form.cleaned_data["birthday"])
                # items = list(tmp)
            if form.cleaned_data["owner_name"]:
                tmp = tmp.filter(owner__name__icontains=form.cleaned_data["owner_name"])
            items = list(tmp)
        elif pk == None:
            tmp = Pets.objects.all().order_by("name")
            items = list(tmp)
        else:
            tmp = Pets.objects.get(id=pk)
            items = [tmp]

    context.update({"title": "Питомцы", "data": items})
    return render(request, template_name, context)
