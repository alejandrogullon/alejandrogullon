from django.http import HttpResponse
from django.shortcuts import render

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../domostats/"))
import temperature, hue_requests

def index(request):
    hue_requests.set_endpoint()
    text = temperature.all_rooms()
    return render(request, 'domostatsApp/domostatsApp.html', {'text' : text })