from django.contrib import admin
# Register your models here.
from .models import Driver ,Manager ,User
# from django.apps import apps



admin.site.register(Driver)
admin.site.register(Manager)
admin.site.register(User)
