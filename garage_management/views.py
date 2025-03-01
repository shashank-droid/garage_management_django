from django.http import HttpResponse #http response is used to pass information back to view
from django.shortcuts import render


def Hello_vehicles(request):
    #return hello vehicles
    return HttpResponse("hello vehicles")

def vehicle_type(request):
    if request.method == 'POST':
        city = request.POST('type')
        data = {
            "price":50
        }
        print(data)
    else:
        data = {}
    return render(request, "garage_management/index.html", data) 