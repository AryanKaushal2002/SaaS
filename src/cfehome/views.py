from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def hello(request, *args, **kwargs):
    
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path= request.path)
    page_title = "my page"
    PageVisit.objects.create()
    context = {'page_title': page_title, "page_visit_count": page_qs.count, "total_visit_count": qs.count}
    
    return render(request, 'home.html', context)