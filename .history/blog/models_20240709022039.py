from typing import Iterable
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img_url=models.URLField(null=True)#nullable coloumn aaka maaththa
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title