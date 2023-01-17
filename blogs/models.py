from django.db import models
from ckeditor.fields import RichTextField


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # membership = models.CharField(max_length=1, choices=[], default='')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class BlogPost(models.Model):
    heading = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.heading}'