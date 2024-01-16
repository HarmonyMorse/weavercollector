from django import forms
from .forms import SightingForm
from django.shortcuts import render, redirect
from .models import Weaver, Power
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def weavers_index(request):
    weavers = Weaver.objects.all()
    for w in weavers:
        w.enemies = w.enemies.split(",")
    return render(request, "weavers/index.html", {"weavers": weavers})


def weavers_detail(request, weaver_id):
    w = Weaver.objects.get(id=weaver_id)
    id_list = w.powers.all().values_list("id")
    powers_weaver_doesnt_have = Power.objects.exclude(id__in=id_list)
    w.enemies = w.enemies.split(",")
    sighting_form = SightingForm()
    return render(
        request,
        "weavers/detail.html",
        {
            "w": w,
            "sighting_form": sighting_form,
            "powers": powers_weaver_doesnt_have,
        },
    )


def add_sighting(request, weaver_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.weaver_id = weaver_id
        new_sighting.save()
    return redirect("detail", weaver_id=weaver_id)


class WeaverCreate(CreateView):
    model = Weaver
    fields = ["name", "description", "enemies"]

    # https://stackoverflow.com/questions/52021136/is-it-possible-to-add-placeholder-in-generic-create-view-form
    def get_form(self, form_class=None):
        form = super(WeaverCreate, self).get_form(form_class)
        form.fields["enemies"].widget = forms.TextInput(
            attrs={"placeholder": "Seperated by commas"}
        )
        return form


class WeaverUpdate(UpdateView):
    model = Weaver
    fields = "__all__"


class WeaverDelete(DeleteView):
    model = Weaver
    success_url = "/weavers"


class PowerList(ListView):
    model = Power
    context_object_name = "power_list"


class PowerDetail(DetailView):
    model = Power


class PowerCreate(CreateView):
    model = Power
    fields = "__all__"


class PowerUpdate(UpdateView):
    model = Power
    fields = ["name", "color"]


class PowerDelete(DeleteView):
    model = Power
    success_url = "/powers"


def assoc_power(request, weaver_id, power_id):
    Weaver.objects.get(id=weaver_id).powers.add(power_id)
    return redirect("detail", weaver_id=weaver_id)


def unassoc_power(request, weaver_id, power_id):
    Weaver.objects.get(id=weaver_id).powers.remove(power_id)
    return redirect("detail", weaver_id=weaver_id)
