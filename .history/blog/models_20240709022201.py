from typing import Iterable
from django.db import models


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img_url=models.URLField(null=True)#nullable coloumn aaka maaththa
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slu=slug

    def __str__(self):
        return self.title