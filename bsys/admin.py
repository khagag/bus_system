from django.contrib import admin
# Register your models here.

from django.apps import apps

# auto-register all models in the app "bsys"
app = apps.get_app_config('bsys')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
