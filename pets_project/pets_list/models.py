from django.db import models


# Create your models here.

class PetsTypes(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, 
                            null=False, verbose_name='Название')
    note = models.TextField(blank=True, null=True, verbose_name='Заметки')

    class Meta:
        verbose_name = 'Тип домашнего животного'
        verbose_name_plural = 'Типы домашних животных'
    
    def __str__(self):
        return self.name

    




class Breeds(models.Model):
    type = models.ForeignKey(PetsTypes, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    note = models.TextField(blank=True, null=True)
    verbose_name = 'Породы'

class PetsOwners(models.Model):
    name = models.CharField(max_length=128, unique= True, blank=False, null=False)
    verbose_name = 'Владельцы домашнего питомца'

class Pets(models.Model):
    breed = models.ForeignKey(Breeds, on_delete=models.CASCADE)
    owner = models.ForeignKey(PetsOwners, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    sex = models.BooleanField()
    year_of_birth = models.DateField(null=True) #если не знаем дату рождения
    color = models.CharField(max_length=64)
    note = models.TextField(blank=True, null=True)
    verbose_name = 'Домашние питомцы'
   





