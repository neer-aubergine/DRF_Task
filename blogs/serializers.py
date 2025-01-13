from rest_framework import serializers
from .models import Blog , Category , Tags
from users.serializers import UserSerializer
from users.models import User

class BlogSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username' , read_only=True)
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'author_username',
            'content',
            'category',
            'tags',
            'created_at',
            'updated_at',
        )
    # def create(self, validated_data):
    #     tags_data = validated_data.pop('tags')
    #     author_username = validated_data.pop('author')['username']
    #     author = User.objects.get(username=author_username)
    #     blog = Blog.objects.create(author=author, **validated_data)
    #     blog.tags.set(tags_data)
    #     return blog