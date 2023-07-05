from django.shortcuts import render, HttpResponse, redirect
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


def add_resume(request):
    if request.method == "GET":
        return render(request, 'resumes/resume_add.html')
    elif request.method == "POST":
        new_rusume = Resume()
        new_rusume.worker = request.user.worker
        new_rusume.created_at = request.POST['form-created_at']
        new_rusume.title = request.POST['form-title']
        new_rusume.text = request.POST['form-text']
        new_rusume.save()
        return HttpResponse('successfully added')


def resume_edit(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == "POST":
        resume.title = request.POST['title']
        resume.text = request.POST['text']
        resume.save()
        return redirect(f'/vacancy/{resume.id}/')
    return render(request, 'resumes/resume_edit.html', {'resume': resume})





