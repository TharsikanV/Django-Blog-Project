from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img_url=models.URLField(blank=True)#nullable coloumn aaka maaththa

    def