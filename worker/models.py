from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    expected_salary = models.IntegerField()
    is_searching = models.BooleanField(default=False)

    def __str__(self):
        return self.name