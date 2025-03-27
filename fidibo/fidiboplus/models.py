from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Users(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(null = True, blank=True)
    number = PhoneNumberField(unique = True)
    cart = models.JSONField()

class Subscription(models.Model):
    user = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "user")
    subscription_status = models.BooleanField(default = False)
