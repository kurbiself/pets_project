from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix="pt", viewset=views.PetsTypesViewsSet, basename="pt")
router.register(prefix="br", viewset=views.BreedsViewsSet, basename="br")


urlpatterns = [
    path("", include(router.urls)),
    path("petstypes/list/", views.PetsTypesListView.as_view()),
    path("petstypes/list2/", views.PetsTypesList.as_view()),
    path("petstypes/create/", views.PetsTypesCreateView.as_view()),
    path("petstypes/update/<int:pk>", views.PetsTypesUpdateView.as_view()),
    path("petstypes/destroy/<int:pk>", views.PetsTypesDestroyView.as_view()),
    path("petstypes/retrieve/<int:pk>", views.PetsTypesRetrieveView.as_view()),
    path("petstypes/", views.pets_types),
    path("petstypes/<int:pk>", views.pet_type),
    path("view/petstypes/", views.pets_types_view),
    path("breeds/", views.breeds),
    path("breeds/<int:pk>", views.breed),
    path("view/breeds/", views.breeds_view),
    path("view/breeds/<int:pk>", views.breeds_view),
    path("petsowners/", views.pets_owners),
    path("petsowners/<int:pk>", views.pets_owner),
    path("view/petsowners/", views.pets_owners_view),
    path("view/petsowners/<int:pk>", views.pets_owners_view),
    path("pets/", views.pets),
    path("pets/<int:pk>", views.pet),
    path("view/pets/", views.pets_view),
]
