from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Recipe, Ingredient, Contact

admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Contact)
