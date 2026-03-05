from django.shortcuts import render, redirect
from .models import Slot, Booking

def home(request):
    return render(request, 'index.html')

def available_slots(request):
    slots = Slot.objects.filter(is_booked=False).order_by('slot_date', 'slot_time')
    return render(request, 'available.html', {'slots': slots})

def book_slot(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        Booking.objects.create(slot=slot, user_name=name, user_email=email)
        slot.is_booked = True
        slot.save()
        return redirect('bookings')
    return render(request, 'book.html', {'slot': slot})

def view_bookings(request):
    bookings = Booking.objects.all().order_by('-booked_at')
    return render(request, 'bookings.html', {'bookings': bookings})
