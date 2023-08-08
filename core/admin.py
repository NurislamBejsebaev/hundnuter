from django.contrib import admin
from .models import *

# admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Category)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'salary', 'email']
    search_fields = ['title', 'descrition', 'candidate__name', 'candidate__user__username']
    list_filter = ['category', 'salary']
    list_editable = ['title', 'salary', 'email']