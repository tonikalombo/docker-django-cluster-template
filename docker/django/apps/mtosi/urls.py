from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipmentinventoryretrieval/getcontainedequipment/', views.getcontainedequipment, name='getcontainedequipment'),
]
