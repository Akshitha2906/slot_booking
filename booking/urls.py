from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('available/', views.available_slots, name='available'),
    path('book/<int:slot_id>/', views.book_slot, name='book'),
    path('bookings/', views.view_bookings, name='bookings'),
]
