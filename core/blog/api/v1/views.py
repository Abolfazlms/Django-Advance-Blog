
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets


from .serializer import PostSerlizer
from blog.models import Post

from django.shortcuts import get_object_or_404

# Example for function base view
"""
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        serializer = PostSerlizer(post,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerlizer(data=request.data)
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
    #     serializer = PostSerlizer(post)
    #     return Response(serializer.data)  
    # except Post.DoesNotExist:
        # return Response({'detail':'post does not exist.'},status=404)
        # return Response({'detail':'post does not exist.'},status=status.HTTP_404_NOT_FOUND)   
        #    
    post = get_object_or_404(Post,pk=id,status=True)    
    if request.method == 'GET':       
        serializer = PostSerlizer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerlizer(post,data=request.data)
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
    serializer_class = PostSerlizer
    def get(self,request):
        '''retrieving a list of posts'''
        post = Post.objects.filter(status=True)
        serializer = PostSerlizer(post,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        '''creating a post with provided data'''
        serializer = PostSerlizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    '''getting detail of the post and edit plus remove it.'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerlizer

    def get(self, request, id):        
        '''retrieving the post data'''
        post = get_object_or_404(Post,pk=id,status=True)  
        serializer = PostSerlizer(post)
        return Response(serializer.data)  
    
    def put(self, request, id):
        '''editing the post data'''
        post = get_object_or_404(Post,pk=id,status=True) 
        serializer = PostSerlizer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        '''deleting the post data'''
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({'detail':'item remove successfully.'},status=status.HTTP_204_NO_CONTENT)
"""

class PostList(ListCreateAPIView):
    '''getting a list of posts and creating new posts'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerlizer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    '''getting detail of the post and edit plus remove it.'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerlizer
    queryset = Post.objects.filter(status=True)
    #lookup_field = 'id' #custom name for parameter or change it on urls.py (default : pk)  

# Example foe View set in class base view
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerlizer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    def create(self,request):
        pass
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post,pk=pk,status=True)
        post.delete()
        return Response({'detail':'item remove successfully.'},status=status.HTTP_204_NO_CONTENT)