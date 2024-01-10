from django.shortcuts import render
from .models import Weaver

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def weavers_index(request):
    weavers = Weaver.objects.all()
    for w in weavers:
        w.enemies = w.enemies.split(",")
    return render(request, 'weavers/index.html', {"weavers": weavers})