from django import forms
from django.shortcuts import render
from .models import Weaver
from django.views.generic.edit import CreateView, UpdateView

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

def weavers_detail(request, weaver_id):
    w = Weaver.objects.get(id=weaver_id)
    w.enemies = w.enemies.split(",")
    return render(request, 'weavers/detail.html', {"w": w})

class WeaverCreate(CreateView):
    model = Weaver
    fields = '__all__'
    
    # https://stackoverflow.com/questions/52021136/is-it-possible-to-add-placeholder-in-generic-create-view-form
    def get_form(self, form_class=None):
        form = super(WeaverCreate, self).get_form(form_class)
        form.fields['enemies'].widget = forms.TextInput(attrs={'placeholder': 'Seperated by commas'})
        return form

class WeaverUpdate(UpdateView):
    model = Weaver
    fields = '__all__'