from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.middleware.csrf import get_token


def api_data_view(request: object) -> object:
    data = {'message': 'Hello from Django API!'}
    print("data")
    return JsonResponse(data)



def csrf_cookie_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})
