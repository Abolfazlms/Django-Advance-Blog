from rest_framework import serializers
from blog.models import Post, Category

# class PostSerlizer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id','name']
class PostSerializer(serializers.ModelSerializer):

    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    # category = serializers.SlugRelatedField(
    #     many=False,
    #     slug_field='name',
    #     queryset=Category.objects.all()
    #     )
    # category = CategorySerializer()
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id','title','image','content','author','category','snippet','status','relative_url','absolute_url','created_date','published_date']
        # read_only_fields = ['content']
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    def to_representation(self,instance):
        request = self.context.get('request')
        # print(request.__dict__)
        rep = super().to_representation(instance)
        rep ['state'] = 'list'
        if request.parser_context.get('kwargs').get('pk'):
            # rep ['state'] = 'single'
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        
        rep['category'] = CategorySerializer(instance.category).data
        
        return rep
