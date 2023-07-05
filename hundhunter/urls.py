from django.contrib import admin
from django.urls import path
from worker.views import *
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about),
    path('contacts/',  contacts),
    path('adress/', adress),
    path('vacancies/', vacancy_list),
    path('companies/', company_list),
    path('workers/', worker_list),
    path("worker/<int:id>/", worker_info),
    path('resume-list/', resume_list),
    path("resume-info/<int:id>/", resume_info),
    path('add-resume/', add_resume, name='add-resume'),
    path("resume-edit/<int:id>/", resume_edit, name='resume-edit'),
    path('my-resume', my_resume, name="my-resume"),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-detail'),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('vacancies-add/', vacancy_add, name='vacancies-add'),
    path('search/', search, name='search'),
    path("registration/", reg_view, name='reg')
]
