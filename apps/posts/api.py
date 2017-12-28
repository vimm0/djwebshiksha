from rest_framework import viewsets

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer