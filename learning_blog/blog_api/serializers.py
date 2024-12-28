from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)  # Nested comments

    class Meta:
        model = Post
        fields = '__all__'
