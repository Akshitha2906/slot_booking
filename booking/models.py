from django.db import models

class Slot(models.Model):
    slot_date = models.DateField()
    slot_time = models.CharField(max_length=50)
    is_booked = models.BooleanField(default=False)

class Booking(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)
