from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo
from .serializers import TodoSerilizer

class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer

class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer