from django.contrib import admin
from .models import Order,Address,Item,Profile


admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Profile)
admin.site.register(Item)


# Register your models here.
