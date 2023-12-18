from rest_framework.serializers import ModelSerializer
from .models import Post, Category
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title','author','published_date', 'content', 'status', 'category']
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'