from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Recruit(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='recruiter'
    )
    city = models.CharField(max_length=255, null=True, blank=True)
    counrty = models.CharField(max_length=255, null=True, blank=True)
    payment_for_found = models.IntegerField(null=True, blank=True)
    bonus_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('recruit-detail', args=[str(self.pk)])
