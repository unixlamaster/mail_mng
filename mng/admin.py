from django.contrib import admin
from .models import Virtual_domain
from .models import Virtual_user

class Virtual_domainAdmin(admin.ModelAdmin):
#    date_hierarchy = "created_on"
    list_display = ('id','name')
    search_fields = ['name']

class Virtual_userAdmin(admin.ModelAdmin):
#    date_hierarchy = "created_on"
    list_display = ('id','user','firstname','tel_w1','surname')
    search_fields = ['user']
    exclude = ('password','pass_change')

admin.site.register(Virtual_domain, Virtual_domainAdmin)
admin.site.register(Virtual_user, Virtual_userAdmin)

