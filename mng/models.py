from django.db import models
from django.utils import timezone

class Virtual_domain(models.Model):
	name = models.CharField(max_length=50)
	class Meta:
		db_table = "virtual_domains"
	def __str__(self):
		return self.name


class Virtual_user(models.Model):
	domain = models.ForeignKey(Virtual_domain, on_delete=models.CASCADE)
	user = models.CharField(max_length=40)
	password = models.CharField(max_length=32)
	firstname = models.CharField(max_length=100)
	tel_w1 = models.CharField(max_length=100)
	surname = models.CharField(max_length=50)
	quota = models.IntegerField()
	job = models.CharField(max_length=100)
	tel_m = models.CharField(max_length=45)
	born = models.CharField(max_length=10)
	tel_w2 = models.CharField(max_length=45)
	notice = models.CharField(max_length=15)
	pass_change = models.DateTimeField(default=timezone.now)
	class Meta:
		db_table = "virtual_users"
	def __str__(self):
		return self.user
