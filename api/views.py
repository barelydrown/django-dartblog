from rest_framework import generics
from rest_framework.response import Response

from blog.models import Category, Tag, Post
from .serializers import CategorySerializer


class PostListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
