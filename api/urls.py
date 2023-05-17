from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('v1/', include(router.urls)),
]
