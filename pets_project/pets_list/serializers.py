from rest_framework import serializers
from .models import PetsTypes, PetsOwners, Pets, Breeds


class BreedsSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source="type")

    class Meta:
        model = Breeds
        fields = ("id", "name", "type", "note", "type_name")


class PetsTypesSerializer(serializers.ModelSerializer):
    breeds = BreedsSerializer(source="breeds_set", many=True, read_only = True)
    
    class Meta:
        model = PetsTypes
        fields = ("id", "name", "note", "breeds")


class PetsOwnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetsOwners
        fields = ("id", "name")


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = (
            "id",
            "name",
            "sex",
            "sex_name",
            "breed",
            "breed_name",
            "owner",
            "owner_name",
            "birth",
            "color",
            "note"
        )
