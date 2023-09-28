from django.db import models

# Create your models here.
class contact(models.Model):
	name=models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	phone = models.CharField(max_length=50)
	msg = models.CharField(max_length=255)

class register_tb(models.Model):
	name=models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	cpassword = models.CharField(max_length=50)