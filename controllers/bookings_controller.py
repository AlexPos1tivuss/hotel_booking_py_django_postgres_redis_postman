from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
from models.models import UserBooking, Room, User
from django.utils.dateparse import parse_date
from django.utils.timezone import now


class BookingController(View):
    def post(self, request):
        try:
            user_id = request.POST.get("user_id")
            room_id = request.POST.get("room_id")
            payment_type = request.POST.get("payment_type")
            total_price = request.POST.get("total_price")

            user = User.objects.get(id=user_id)
            room = Room.objects.get(id=room_id)

            booking = UserBooking.objects.create(
                user=user,
                room=room,
                date=parse_date(now().date()),
                time=now().time(),
                price=total_price,
                payment_type=payment_type
            )

            cache.set(f"booking:{booking.id}", {
                "user": user.name,
                "room": room.type,
                "price": total_price,
                "payment_type": payment_type
            }, timeout=3600)

            return JsonResponse({"message": "Booking created successfully", "booking_id": booking.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
