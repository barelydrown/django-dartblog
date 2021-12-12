from rest_framework import serializers
from blog.models import Category, Tag, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = serializers.SlugRelatedField(slug_field='slug', many=True)

    class Meta:
        model = Post
        fields = '__all__'
