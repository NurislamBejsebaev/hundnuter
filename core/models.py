from django.db import models
from worker.models import Worker
from django.contrib.auth.models import User


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания ')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True,
    )
    review = models.ManyToManyField(
        to=User,
        blank=True
    )
    category = models.ForeignKey(
        to='Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = "Вакансии"
        ordering = ['salary']
        unique_together = [['title', 'email']]


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    num_employees = models.IntegerField()
    is_hunting = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

