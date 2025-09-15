from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    content = models.TextField()