from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.text)
    