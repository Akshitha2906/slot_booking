#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from booking.models import Slot
if Slot.objects.count() == 0:
    slots = [('2026-03-06','09:00 AM - 10:00 AM'),('2026-03-06','10:00 AM - 11:00 AM'),('2026-03-06','11:00 AM - 12:00 PM'),('2026-03-06','01:00 PM - 02:00 PM'),('2026-03-06','02:00 PM - 03:00 PM'),('2026-03-06','03:00 PM - 04:00 PM'),('2026-03-07','09:00 AM - 10:00 AM'),('2026-03-07','10:00 AM - 11:00 AM'),('2026-03-07','11:00 AM - 12:00 PM'),('2026-03-07','01:00 PM - 02:00 PM'),('2026-03-07','02:00 PM - 03:00 PM'),('2026-03-07','03:00 PM - 04:00 PM')]
    for d,t in slots:
        Slot.objects.create(slot_date=d, slot_time=t)
    print('Slots added')
"
