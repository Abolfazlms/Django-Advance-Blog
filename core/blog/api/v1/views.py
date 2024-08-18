
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import PostSerlizer
from blog.models import Post

from django.shortcuts import get_object_or_404

data = {
    'id':1,
    'title':'hello'
}

@api_view(['GET','POST'])
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