from django.shortcuts import render
from .serializers import PostSerializers
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostList(ListCreateAPIView):
    # permission_classes = (Is,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
