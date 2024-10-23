from django.urls import path
from . import views

urlpatterns = [
    path('petstypes/', views.pets_types),
]
