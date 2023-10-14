from django.shortcuts import render
def page_not_found_view(request, exeception):
    return render(request, 'auth/404.html', status=404)