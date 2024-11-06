from django.urls import path
from . import views

urlpatterns = [
    path('petstypes/', views.pets_types),
    path('breeds/', views.breeds),
    path('petsowners/', views.pets_owners),
    path('pets/', views.pets),
    path('pets/<int:pk>', views.pets),
]
