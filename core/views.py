from django.shortcuts import render, HttpResponse
from core.models import Vacancy
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
    return render(request, 'vacanies.html', context)