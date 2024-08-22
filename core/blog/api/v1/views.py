
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets

from.permissions import IsOwnerOrReadOnly


from .serializer import PostSerializer, CategorySerializer
from blog.models import Post, Category

from django.shortcuts import get_object_or_404

# Example for function base view
"""
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])

def postDetail(request,id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)  
    # except Post.DoesNotExist:
        # return Response({'detail':'post does not exist.'},status=404)
        # return Response({'detail':'post does not exist.'},status=status.HTTP_404_NOT_FOUND)   
        #    
    post = get_object_or_404(Post,pk=id,status=True)    
    if request.method == 'GET':       
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'item remove successfully.'},status=status.HTTP_204_NO_CONTENT)

"""

# Example for APIView
"""
from rest_framework.views import APIView
class PostList(APIView):
    '''getting a list of posts and creating new posts'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request):
        '''retrieving a list of posts'''
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        '''creating a post with provided data'''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    '''getting detail of the post and edit plus remove it.'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):        
        '''retrieving the post data'''
        post = get_object_or_404(Post,pk=id,status=True)  
        serializer = PostSerializer(post)
        return Response(serializer.data)  
    
    def put(self, request, id):
        '''editing the post data'''
        post = get_object_or_404(Post,pk=id,status=True) 
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        '''deleting the post data'''
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({'detail':'item remove successfully.'},status=status.HTTP_204_NO_CONTENT)
"""

# Example for GenericAPIView
"""
class PostList(ListCreateAPIView):
    '''getting a list of posts and creating new posts'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    '''getting detail of the post and edit plus remove it.'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    #lookup_field = 'id' #custom name for parameter or change it on urls.py (default : pk)  
"""
# Example foe View set in class base view
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    @action(methods=['get'], detail=False)
    def get_ok(self, request):
        return Response({'detail':'ok'})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

