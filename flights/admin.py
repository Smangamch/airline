from django.contrib import admin
from .models import flights, Airport, passengers

# Register your models here.


admin.site.register(Airport)
admin.site.register(flights)
admin.site.register(passengers)


