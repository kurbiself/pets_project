from rest_framework import serializers
from models import PetsTypes

class PetsTypesSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = PetsTypes
       fields = ('id', 'name', 'note')
