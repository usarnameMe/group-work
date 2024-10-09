from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:pk>/edit/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicle/<int:pk>/delete/', views.delete_vehicle, name='delete_vehicle'),
    path('add/', views.add_vehicle, name='add_vehicle'),
]
