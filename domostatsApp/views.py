from django.http import HttpResponse
from django.shortcuts import render

import sys
sys.path.insert(1, '/Users/Alejandro/workspace/domostats/')
import temperature, hue_requests

def index(request):
    hue_requests.set_endpoint()
    text = temperature.all_rooms()
    return render(request, 'domostatsApp/domostatsApp.html', {'text' : text })    
    #return HttpResponse("Holi 😊")