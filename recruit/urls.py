from django.urls import path
from recruit.views import *
urlpatterns = [
    path('list/', recruit_list, name='recruit-list'),
    path('list-class/', RecruitView.as_view(), name='recruit-list-class'),
    path('list-class-generic/', RecruitListView.as_view(), name='recruit-list-class-generic'),
    path('detail/<int:pk>/', recruit_detail, name='recruit-detail'),
    path('create/', RecruitCreateView.as_view(), name='recruit-create'),
    path('update/<int:pk>/', RecruitUpdateView.as_view(), name='recruit-update'),
]