from rest_framework import serializers
from api.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'created')