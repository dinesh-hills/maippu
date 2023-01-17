from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blog-list'),
    path('<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
]
