from rest_framework import serializers
from blog.models import Post, Category

# class PostSerlizer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id','title','content','author','category','created_date','published_date','status']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id','name']