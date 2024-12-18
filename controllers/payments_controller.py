from django.http import JsonResponse
from django.views import View
from django.core.cache import cache

class PaymentsController(View):
    def post(self, request):
        try:
            booking_id = request.POST.get("booking_id")
            payment_type = request.POST.get("payment_type")
            amount = request.POST.get("amount")

            cache.set(f"payment:{booking_id}", {
                "payment_type": payment_type,
                "amount": amount
            }, timeout=3600)

            return JsonResponse({"message": "Payment recorded successfully", "booking_id": booking_id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
