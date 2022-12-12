from ipware import get_client_ip
from django.http import HttpResponse

BLACK_LIST = [
]

def is_valid_ip(get_response):
    def middleware(request):
        ip, is_routable = get_client_ip(request)
        response = get_response(request)
        print("ip visitante:", ip)
        return response
    return middleware

""" class IPIsValid():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)

        if ip in BLACK_LIST:
            return HttpResponse('Bad request', status=404)
        else:
            return get_response(request) """