from django.contrib import admin
from .models import BlogPost, Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['heading', 'author', 'created_at']