from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from core.models import Vacancy, Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import VacancyForm, VacancyEditform, CompanyForm, CompanyEdit
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
    return render(request, 'company/company_list.html', contextr)


def company_info(request, id):
    company = Company.objects.get(id=id)
    context = {'company': company}
    return render(request, "company/info.html", context)


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


def sign_in(request):
    if request.POST == 'POST':
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            HttpResponse('Неверный пароль или логин')

    return render(request, 'auth/sign_in.html')


def sign_out(request):
    logout(request)
    return redirect(sign_in)


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
        new_vacan.title = request.POST['titlee']
        new_vacan.salary = int(request.POST['salary'])
        new_vacan.email = request.POST['email']
        new_vacan.description = request.POST['description']
        new_vacan.save()
        return HttpResponse('successfully added')


def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm
    return render(request, 'vacancy/vacancy_django_form.html', {"vacancy_form": vacancy_form})


def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST['titlee']
        vacancy.salary = int(request.POST['salary'])
        vacancy.email = request.POST['email']
        vacancy.description = request.POST['description']
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(request, 'vacancy/vacan_edit.html', {'vacancy': vacancy})


def vacancy_edit_via_django_form(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    if request.method == 'GET':
        vacancy_edit_form = VacancyEditform(instance=vacancy_object)
        return render(request, 'vacancy/vacancy_edit_form.html', {'vacancy_edit_form': vacancy_edit_form})
    elif request.method == 'POST':
        vacancy_edit_form = VacancyForm(data=request.POST, instance=vacancy_object)
        if vacancy_edit_form.is_valid():
            obj = vacancy_edit_form.save()
            return redirect(vacancy_detail, id=obj.id)
        else:
            HttpResponse('ajhvf yt dfkblyf')


def company_add(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save()
            return redirect(f'/company-info/{new_company.id}/')
    else:
        company_form = CompanyForm()
        return render(request, 'company/add.html', {"form": company_form})


def company_edit(request, id):
    company_object = Company.objects.get(id=id)
    if request.method == 'GET':
        company_edit_form = CompanyEdit(instance=company_object)
        return render(request, 'company/edit.html', {'form': company_edit_form})
    elif request.method == 'POST':
        company_edit_form = CompanyForm(data=request.POST, instance=company_object)
        if company_edit_form.is_valid():
            company = company_edit_form.save()
            return redirect(company_info, id=company.id)
        else:
            return HttpResponse('ajhvf yt dfkblyf')
