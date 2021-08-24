from django.contrib import admin
from .models import Challenge, People, Place, Thing
# Register your models here.
admin.site.register(Challenge)
admin.site.register(People)
admin.site.register(Place)
admin.site.register(Thing)