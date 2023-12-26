from rest_framework.serializers import ModelSerializer
from .models import Post, Category
from rest_framework import serializers
from accounts.models import Profile

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(ModelSerializer):
    content = serializers.ReadOnlyField()
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    # relative_url = serializers.URLField(source = 'get_absolute_api_url')
    absolute_url = serializers.SerializerMethodField()
    # category = CategorySerializer()
    
    class Meta:
        model = Post
        fields = ['id','absolute_url', 'title','author','published_date', 'content', 'snippet', 'status', 'category']
        read_only_fields = ['id','absolute_url', 'author']
        
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category,context={'request':request}).data
        
        return rep    
        
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id= self.context.get('request').user.id)
        return super().create(validated_data)
