from django.db import models
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

class Resume(models.Model):
    fname=models.TextField(max_length=100)
    lname=models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.email



