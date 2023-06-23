from django.contrib import admin
from django.urls import path
from worker.views import (
    worker_list
)
from core.views import (
    homepage,
    about,
    contacts,
    adress,
    vacancy_list,
    company_list,
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
]
