from django.contrib import admin
from .models import Car, Make, Models, SubModel


admin.site.register(Car)
admin.site.register(Make)
admin.site.register(Models)
admin.site.register(SubModel)
