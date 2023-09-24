from django.db import models
from django.utils import timezone


# Create your models here.
from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lead(models.Model):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=255 ,null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(null=True, blank=True)
    source = models.CharField(max_length=255 ,null=True, blank=True)
    notes = models.TextField(null=True, blank=True )
    label = models.ForeignKey(Label,null=True, blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClientIP(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address

class ActivityName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.ForeignKey(ActivityName, on_delete=models.CASCADE)
    schedule = models.DateTimeField(null=True, blank=True)
    notes = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name