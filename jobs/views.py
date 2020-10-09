from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    context = {
        'posts' : Job.objects.all()
    }
    return render(request, 'jobs/home.html', context)