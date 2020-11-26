#from django.db import models
from djongo import models
# Create your models here.

class Articleinfo(models.Model):

    Website = models.TextField()
    Title = models.TextField()
    Authors = models.JSONField()
    Publish_Date = models.TextField()
    Article = models.TextField()
    URL= models.TextField()