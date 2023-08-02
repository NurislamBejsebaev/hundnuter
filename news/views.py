from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ArticleNew


class ArticleNewListView(LoginRequiredMixin, ListView):
    model = ArticleNew


def news_detail(request, pk):
    news_object = ArticleNew.objects.get(pk=pk)
    return render(request, 'news/detail.html', {'news_object': news_object})


class ArticleNewCreateView(CreateView):
    model = ArticleNew
    fields = '__all__'
    template_name_suffix = "_create_form"


class ArticleNewUpdateView(UpdateView):
    model = ArticleNew
    fields = '__all__'
    template_name_suffix = "_update_form"
    # success_url = reverse_lazy('recruit-list')
