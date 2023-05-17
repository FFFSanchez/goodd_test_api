from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks'
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    class Meta:
        verbose_name = ('Задача')
        verbose_name_plural = ('Задачи')

    def __str__(self):
        return self.text
