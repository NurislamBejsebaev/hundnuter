from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ResumeEditForm, ResumeForm


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


@login_required(login_url='sign-in')
def add_resume(request):
    if request.method == "GET":
        return render(request, 'resumes/resume_add.html')
    elif request.method == "POST":
        new_rusume = Resume()
        new_rusume.worker = request.user.worker
        new_rusume.title = request.POST['title']
        new_rusume.text = request.POST['text']
        new_rusume.save()
        return HttpResponse('successfully added')


def resume_edit(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == "POST":
        resume.title = request.POST['title']
        resume.text = request.POST['text']
        resume.save()
        return redirect(f'/resume-info/{resume.id}/')
    return render(request, 'resumes/resume_edit.html', {'resume': resume})


def resume_edit_django_form(request, id):
    resume_object = Resume.objects.get(id=id)
    if request.method == 'GET':
        form = ResumeEditForm(instance=resume_object)
        return render(request, 'resumes/resume_edit_df.html', {'form': form})
    elif request.method == 'POST':
        form = ResumeEditForm(data=request.POST, instance=resume_object, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(resume_info, id=obj.id)
        else:
            HttpResponse('форма не валидно')


# def add_resume_df_django_form(request):
#     if request.method == 'POST':
#         form_resume = ResumeForm(request.POST)
#         if form_resume.is_valid():
#             resume_new = form_resume.save(commit=False)
#             resume_new.author_id = request.user.id  # Устанавливаем идентификатор текущего пользователя как автора резюме
#             resume_new.save()
#             return redirect(f'/resume-info/{resume_new.id}/')
#     obj_resume = ResumeForm()
#     return render(request, 'resumes/resume_add_django_form.html', {'resume_ad': obj_resume})

def add_resume_df_django_form(request):
    if request.method == 'POST':
        form_resume = ResumeForm(request.POST)
        if form_resume.is_valid():
            resume_new = form_resume.save(commit=False)
            worker = get_object_or_404(Worker, user=request.user)  # Получаем объект Worker для текущего пользователя
            resume_new.worker = worker  # Устанавливаем объект Worker в качестве значения поля "worker"
            resume_new.save()
            return redirect(f'/resume-info/{resume_new.id}/')
    obj_resume = ResumeForm()
    return render(request, 'resumes/resume_add_django_form.html', {'resume_ad': obj_resume})