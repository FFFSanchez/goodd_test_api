from tasks.models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator
from .permissions import OwnerOrReadOnly

from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, OwnerOrReadOnly]

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        #cache.clear()
        return super(TaskViewSet, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.request.user.tasks.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
