from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post, Category
from blog.serializers import PostSerializer, CategorySerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination


'''
creating views using ModelViewSet
'''
class PostModelViewSet(ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    pagination_class = DefaultPagination
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title','content']
    ordering_fields = ['published_date']
    
class CategoryModelViewSet(ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 

'''
creating views using concrete views (generic views + mixins)
'''

class PostList(ListCreateAPIView):
    '''
    getting a list of posts and creating a new post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    '''
    get, update and delete a post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

'''
creating views using APIVIEW
'''
    
# class PostList(APIView):
#     permission_classes= [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     '''
#     getting a list of posts and creating a new post
#     '''
#     def get(self,request):
#         '''
#         retrieve a list of posts
#         '''
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         '''
#         create a new post
#         '''
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostDetail(APIView):
#     '''
#     get, update and delete a post
#     '''
#     permission_classes= [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
        
#     def get(self, request, pk):
#         post = get_object_or_404(Post, id=pk, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self, request,pk):
#         post = get_object_or_404(Post, id=pk, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         post = get_object_or_404(Post, id=pk, status=True)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)