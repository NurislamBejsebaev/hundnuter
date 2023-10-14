from django.contrib import admin
from django.urls import path, include
from worker.views import *
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', about),
    path('contacts/',  contacts),
    path('adress/', adress),
    path('vacancies/', vacancy_list),
    path('companies/', company_list),
    path('company-info/<int:id>/', company_info, name='company-info'),
    path('company-add/', company_add),
    path('company-edit//<int:id>/', company_edit, name='company-edit'),
    path('workers/', worker_list),
    path("worker/<int:id>/", worker_info),
    path('resume-list/', resume_list),
    path("resume-info/<int:id>/", resume_info),
    path('add-resume/', add_resume, name='add-resume'),
    path("resume-edit/<int:id>/", resume_edit, name='resume-edit'),
    path("resume-edit-df/<int:id>/", resume_edit_django_form, name='resume-edit-df'),
    path('add-resume-df/', add_resume_df_django_form),
    path('my-resume', my_resume, name="my-resume"),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-detail'),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('vacancies-add/', vacancy_add, name='vacancies-add'),
    path('vacancies-add-df/', vacancy_add_via_django_form, name='vacancies-add-df'),
    path('vacancy-redactor/<int:id>/', vacancy_edit_via_django_form, name='vacancy-edit-df'),
    path('search/', search, name='search'),
    path("registration/", reg_view, name='reg'),
    path("sign-in/", sign_in, name='sign-in'),
    path("login-generic/", LoginView.as_view(), name='sign-in-generic'),
    path("sign-out/", sign_out, name='sign-out'),
    path("recruit/", include('recruit.urls')),
    path("news/", include('news.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# new_resume = form.save(commit=False)
# new_resume = request.user.worker

handler404 = "hundhunter.views.page_not_found_view"
