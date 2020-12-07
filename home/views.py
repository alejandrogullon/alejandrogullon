from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../domostats/"))
import temperature, hue_requests

def index(request):
    hue_requests.set_endpoint()
    text = temperature.all_rooms()
    return render(request, 'home/home.html', {'text' : text })

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "User-agent: AdsBot-Google",
        "Disallow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")