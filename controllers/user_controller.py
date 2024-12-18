from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
from models.models import User

class UserController(View):
    def post(self, request):
        try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = User.objects.create(
                name=name, phone=phone, email=email, password=password
            )

            cache.set(f"user:{user.id}", {
                "name": name,
                "email": email,
                "phone": phone
            }, timeout=3600)

            return JsonResponse({"message": "User created successfully", "user_id": user.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
