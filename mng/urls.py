from django.conf.urls import url
from django.contrib import admin
from . import views
#admin.autodisover()

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
