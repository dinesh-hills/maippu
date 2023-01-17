from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListView(APIView):
    def get(self, request):
        queryset = BlogPost.objects.all()
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogPostDetailView(APIView):
    def get(self, request, pk):
        try:
            blog_post = BlogPost.objects.select_related('author').get(pk=pk)
            serializer = BlogPostSerializer(blog_post)
        except BlogPost.DoesNotExist:
            return Response({'error': 'no content exist'} , status=status.HTTP_200_OK)
        return Response(serializer.data)