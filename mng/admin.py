from django.contrib import admin
from .models import Virtual_domain
from .models import Virtual_user

admin.site.register(Virtual_domain)
admin.site.register(Virtual_user)
