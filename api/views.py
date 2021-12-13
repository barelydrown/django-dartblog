from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from blog.models import Category, Tag, Post
from .serializers import (
    CategorySerializer, TagSerializer, PostSerializer,
    CreateCategorySerializer, CreateTagSerializer, CreatePostSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = (IsAdminUser,)


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = (IsAdminUser,)


class CategoryDestroyView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = (IsAdminUser,)


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_classes = (IsAdminUser,)


class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_classes = (IsAdminUser,)


class TagDestroyView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_classes = (IsAdminUser,)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (IsAdminUser,)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (IsAdminUser,)


class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (IsAdminUser,)
