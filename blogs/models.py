from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # membership = models.CharField(max_length=1, choices=[], default='')

    def __str__(self) -> str:
        return self.first_name

class BlogPost(models.Model):
    heading = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.heading