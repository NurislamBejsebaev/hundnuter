from django.contrib import admin
from django.urls import path
from worker.views import (
    worker_list,
    worker_info,
    resume_list,
    resume_info,
    my_resume,
)
from core.views import (
    homepage,
    about,
    contacts,
    adress,
    vacancy_list,
    company_list,
    vacancy_detail,
)

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
    path('my-resume', my_resume, name="my-resume"),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy_detail'),
]
