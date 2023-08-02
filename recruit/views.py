from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recruit


def recruit_list(request):
    recruiters = Recruit.objects.all()
    return render(request, 'recruit/list.html', {'recruiters': recruiters})


def recruit_detail(request, pk):
    recruit_object = Recruit.objects.get(pk=pk)
    return render(request, 'recruit/detail.html', {'recruit_object': recruit_object})


class RecruitView(View):
    def get(self, request):
        recruiters = Recruit.objects.all()
        return render(request, 'recruit/list.html', {'recruiters': recruiters})


class RecruitListView(LoginRequiredMixin, ListView):
    model = Recruit


class RecruitCreateView(CreateView):
    model = Recruit
    fields = '__all__'
    template_name_suffix = "_create_form"


class RecruitUpdateView(UpdateView):
    model = Recruit
    fields = '__all__'
    template_name_suffix = "_update_form"
    # success_url = reverse_lazy('recruit-list')