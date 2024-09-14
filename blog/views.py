from rest_framework import viewsets,mixins 

from blog.models import Category,Post
from blog.serializers import CategorySerializer,PostSerializer


class CategoryViewSet(viewsets.mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

