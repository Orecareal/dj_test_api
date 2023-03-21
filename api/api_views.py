from rest_framework import viewsets
from api.serializers import PostSerializers as ps
from api.models import Post


class PostViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ps
    http_method_names = ['get']