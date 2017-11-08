from django.contrib import admin
from parqueos.models import Parqueo, ParqueoAdmin, Vehiculos, VehiculosAdmin
# Register your models here.
admin.site.register(Parqueo, ParqueoAdmin)
admin.site.register(Vehiculos, VehiculosAdmin)
