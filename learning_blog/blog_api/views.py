from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Category,Post,Comment
from .serializers import CategorySerializer, PostSerializers, CommentSerializers

#Category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostsByCategoryView(ListAPIView):
    serializer_class = PostSerializers

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')  # Extract the category ID from the URL
        return Post.objects.filter(category_id=category_id).order_by('-created_at')

#Category post and details
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

#newest
class LastSixPostsView(ListAPIView):
    serializer_class = PostSerializers

    def get_queryset(self):
        # Get the last 6 posts ordered by creation date (most recent first)
        return Post.objects.order_by('-created_at')[:6]
    

# Comment 
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    