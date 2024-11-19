from django import forms

class PetsFilter(forms.Form):
    pet_name = forms.CharField(label='Кличка', max_length=64, required=False)
    owner_name = forms.CharField(label='Имя хозяина', required=False)
    birthday = forms.DateField(label='Дата рождения', required=False, widget=forms.DateInput(attrs={'type': 'date'}))