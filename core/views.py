from django.shortcuts import render, HttpResponse, get_object_or_404
from core.models import Vacancy, Company
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
