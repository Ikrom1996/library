import datetime
from django.utils import timezone
from django.http import HttpResponse

class LogIPMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response  # Keyingi middleware yoki viewni chaqiradi


    def __call__(self, request):

        ip = request.META.get('HTTP_USER_AGENT', 'Noma’lum IP')

        now = datetime.datetime.now()

        print(f"[{now}] So‘rov IP: {ip}")  # Terminalga chop etamiza
        print(request.META)

        response = self.get_response(request)  # So‘rovni keyingi bosqichga yuboramiza
        return response



class BlockingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self,request):
        if not 8 < timezone.now().hour + 5   < 16:
            return HttpResponse('soat 8:00 dan 16:00 gacha ishlaydi saytimiz')
        response = self.get_response(request)
        return response

