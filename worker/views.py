from django.shortcuts import render
from .models import *


def worker_list(request):
    context = {"workers": Worker.objects.all()}
    return render(request, 'worker/worker_list.html', context)


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    context = {'worker': worker_object}
    return render(request, 'worker/worker.html', context)


def resume_list(request):
    resume_query = Resume.objects.all()
    return render(request, "resumes/resume_list.html", {'resumes': resume_query})


def resume_info(request, id):
    resume_query = Resume.objects.get(id=id)
    context = {'resume': resume_query}
    return render(request, "resumes/resume_info.html", context)


def my_resume(request):
    resume_query = Resume.objects.filter(worker=request.user.worker)
    return render(request, "resumes/resume_list.html", {'resumes': resume_query})