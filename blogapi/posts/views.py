from .serializers import PostSerializers, UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .models import Post
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer