from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('available/', views.available_slots, name='available'),
    path('book/<int:slot_id>/', views.book_slot, name='book'),
    path('bookings/', views.view_bookings, name='bookings'),
    path('add-slot/', views.add_slot, name='add_slot'),
    path('delete-slot/<int:slot_id>/', views.delete_slot, name='delete_slot'),
]
