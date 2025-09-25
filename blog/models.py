from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title