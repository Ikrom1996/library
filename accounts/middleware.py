import datetime

class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Keyingi middleware yoki view'ni chaqiradi

    def __call__(self, request):
        ip = request.META.get('HTTP_USER_AGENT', 'Noma’lum IP')
        now = datetime.datetime.now()
        print(f"[{now}] So‘rov IP: {ip}")  # Terminalga chop etamiz
        response = self.get_response(request)  # So‘rovni keyingi bosqichga yuboramiz
        return response
