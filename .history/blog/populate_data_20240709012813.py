from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help="This commands inserts podt data"


    def handle(self, *args: Any, **options: Any):
        return super().handle(*args, **options)