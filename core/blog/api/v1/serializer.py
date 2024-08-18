from rest_framework import serializers
from blog.models import Post

# class PostSerlizer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id','title','content','author','category','created_date','published_date','status']