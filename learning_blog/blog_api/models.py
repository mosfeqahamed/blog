from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    img = models.URLField()  
    short = models.TextField()  
    content = models.TextField() 
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name of the commenter
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"