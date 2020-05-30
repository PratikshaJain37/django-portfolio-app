from django.shortcuts import render
from about.models import About
# Create your views here.

def about_index(request):
    about_info = About.objects.all()
    context = {
        'about':about_info
    }
    return render(request, 'about_index.html', context)