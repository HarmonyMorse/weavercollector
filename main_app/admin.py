from django.contrib import admin
from .models import Weaver, Sighting, Power

# Register your models here.
admin.site.register(Weaver)
admin.site.register(Sighting)
admin.site.register(Power)