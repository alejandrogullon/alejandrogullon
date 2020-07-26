from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

def index(request):
    return render(request, 'home/home.html')

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "User-agent: AdsBot-Google",
        "Disallow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")