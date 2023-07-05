from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from core.models import Vacancy, Company
from django.contrib.auth.models import User
# Create your views here.


def homepage(request):
    return render(request=request, template_name="index.html")


def about(request):
    return HttpResponse('Хотите найди работу или найди работника мечты')


def contacts(request):
    return HttpResponse('''
        <div>
            phone: +3874628734 <br>
            email: fdsgfs@gmail.com
        </div>
    
    ''')


def adress(request):
    return HttpResponse('''
        <ul>
            <li>г. Бишкек 7мкр, 26/1</li>
            <li>г. Ош, Черемушка, дом 235</li>
        </ul>
    ''')


def vacancy_list(request):
    context = {"vacancies": Vacancy.objects.all()}
    return render(request, 'vacancy/vacanies.html', context)


def company_list(request):
    contextr = {"companies": Company.objects.all()}
    return render(request, 'company_list.html', contextr)


def vacancy_detail(request, id):
    vacancy_object = get_object_or_404(Vacancy, id=id)
    candidates = vacancy_object.candidate.all()
    context = {
        'vacancy': vacancy_object,
        'candidates': candidates,
    }
    return render(request, 'vacancy/vacancy_detail.html', context)


def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {'vacancies': vacancy_list}
    return render(request, 'vacancy/vacanies.html', context)


def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse('Готово')

    return render(
        request,
        "auth/register.html"

    )


def vacancy_add(request):
    if request.method == "GET":
        return render(request, 'vacancy/vacan_add.html')
    elif request.method == "POST":
        new_vacan = Vacancy()
        # new_vacan.candidate = request.
        new_vacan.title = request.POST['title']
        new_vacan.salary = int(request.POST['salary'])
        new_vacan.email = request.POST['email']
        new_vacan.description = request.POST['description']
        new_vacan.save()
        return HttpResponse('successfully added')


def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST['title']
        vacancy.salary = int(request.POST['salary'])
        vacancy.email = request.POST['email']
        vacancy.description = request.POST['description']
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(request, 'vacancy/vacan_edit.html', {'vacancy': vacancy})