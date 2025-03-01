from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to washing center")

# def vehicle_type(request):
#     if request.method == 'POST':
#         city = request.POST('type')
#         data = {
#             "price":50
#         }
#         print(data)
#     else:
#         data = {}