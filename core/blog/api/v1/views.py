from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

# Create your views here.
class PostList(APIView):
    permission_classes= [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    '''
    getting a list of posts and creating a new post
    '''
    def get(self,request):
        '''
        retrieve a list of posts
        '''
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        '''
        create a new post
        '''
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetail(APIView):
    '''
    get, update and delete a post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
        
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request,pk):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    