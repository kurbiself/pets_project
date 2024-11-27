from django.urls import path
from . import views

urlpatterns = [
    path('petstypes/', views.pets_types),
    path('petstypes/<int:pk>', views.pet_type),
    path('view/petstypes/', views.pets_types_view),
    path('breeds/', views.breeds),
    path('breeds/<int:pk>', views.breed),
    path('view/breeds/', views.breeds_view),
    path('view/breeds/<int:pk>', views.breeds_view),
    path('petsowners/', views.pets_owners),
    path('petsowners/<int:pk>', views.pets_owner),
    path('view/petsowners/', views.pets_owners_view),
    path('view/petsowners/<int:pk>', views.pets_owners_view),
    path('pets/', views.pets),
    path('pets/<int:pk>', views.pet),
    path('view/pets/', views.pets_view),
]
