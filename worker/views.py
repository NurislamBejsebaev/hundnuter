from django.shortcuts import render
from .models import *


def worker_list(request):
    context = {"workers": Worker.objects.all()}
    return render(request, 'worker_list.html', context)
