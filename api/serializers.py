from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Task
        fields = '__all__'
