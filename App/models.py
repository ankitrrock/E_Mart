from django.db import models

# Create your models here.


class registration(models.Model):
    user_name = models.CharField(max_length=50,null=True, blank=True)
    u_email = models.EmailField(max_length=25,null=True, blank=True)
    u_password = models.CharField(max_length=20,null=True, blank=True)
    u_cpassword = models.CharField(max_length=10,null=True, blank=True)
