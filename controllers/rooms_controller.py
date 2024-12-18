from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
from models import Room

class RoomsController(View):
    def post(self, request):
        try:
            number = request.POST.get("number")
            room_type = request.POST.get("type")
            price = request.POST.get("price")

            room = Room.objects.create(
                number=number, type=room_type, price=price
            )

            cache.set(f"room:{room.id}", {
                "number": number,
                "type": room_type,
                "price": price
            }, timeout=3600)

            return JsonResponse({"message": "Room created successfully", "room_id": room.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
