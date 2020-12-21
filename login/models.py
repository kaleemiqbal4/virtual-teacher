from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    email_id = models.CharField(max_length=70, blank=False, default='')
    contact = models.CharField(max_length=15, blank=False, default='')
    otp = models.CharField(max_length=6,blank=False, default='')
    status = models.BooleanField(default=False)