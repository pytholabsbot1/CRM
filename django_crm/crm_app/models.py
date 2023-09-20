from django.db import models

# Create your models here.
from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lead(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    source = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ActivityName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.ForeignKey(ActivityName, on_delete=models.CASCADE)
    notes = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name