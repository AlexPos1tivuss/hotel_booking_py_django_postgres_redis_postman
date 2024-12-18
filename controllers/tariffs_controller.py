from django.http import JsonResponse
from django.views import View
from django.core.cache import cache

class TariffsController(View):
    def post(self, request):
        try:
            tariff_name = request.POST.get("name")
            price = request.POST.get("price")

            cache.set(f"tariff:{tariff_name}", {
                "name": tariff_name,
                "price": price
            }, timeout=3600)

            return JsonResponse({"message": "Tariff created successfully", "tariff_name": tariff_name}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
