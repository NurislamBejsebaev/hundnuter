from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ArticleNew(models.Model):
    author = models.ForeignKey(
        to=User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='news',
    )
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    likes_users = models.ManyToManyField(User, blank=True)
    user_views = models.ManyToManyField(
        to=User,
        related_name='new_views',
        blank=True,

    )

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title


class NewsView(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,

    )
    new = models.ForeignKey(
        to=ArticleNew,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [['user', 'new']]

