from django.contrib import admin # type: ignore
from .models import Item, Restaurant, User

# Register your models here.

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Item)


