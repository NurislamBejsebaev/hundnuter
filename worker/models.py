from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    expected_salary = models.IntegerField()
    is_searching = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    creared_at = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author.username


class Resume(models.Model):
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        related_name='resume'
    )
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






