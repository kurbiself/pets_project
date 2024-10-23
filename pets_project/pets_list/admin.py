from django.contrib import admin
from .models import PetsTypes, Pets, PetsOwners, Breeds

# Register your models here.

admin.site.register(PetsTypes)
admin.site.register(Pets)
admin.site.register(PetsOwners)
admin.site.register(Breeds)


