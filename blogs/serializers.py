import re
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.__str__', read_only=True)

    eta_read = serializers.SerializerMethodField(method_name='cal_read_time')
    def cal_read_time(self, blogPost: BlogPost):
        p = re.compile(r'<.*?>')
        body = p.sub('', blogPost.body)
        return round(body.split(" ").__len__()/220, 1)

    class Meta:
        model = BlogPost
        fields = ['id', 'author_name', 'created_at', 'heading', 'body', 'eta_read']