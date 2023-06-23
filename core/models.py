from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания ')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    num_employees = models.IntegerField()
    is_hunting = models.BooleanField(default=False)

    def __str__(self):
        return self.name