from tasks.models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import OwnerOrReadOnly

from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, OwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
