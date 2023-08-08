from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class ArticleNewListView(LoginRequiredMixin, ListView):
    model = ArticleNew


def news_detail(request, pk):
    new = ArticleNew.objects.get(pk=pk)
    new.views_count += 1
    new.user_views.add(request.user)
    new.save()

    new_view_object = NewsView.objects.get_or_create(
        new=new,
        user=request.user
    )

    return render(request, 'news/articlenew_detail_form.html', {'object_list': new})


class ArticleNewCreateView(CreateView):
    model = ArticleNew
    fields = '__all__'
    template_name_suffix = "_create_form"


class ArticleNewUpdateView(UpdateView):
    model = ArticleNew
    fields = '__all__'
    template_name_suffix = "_update_form"
    # success_url = reverse_lazy('recruit-list')
