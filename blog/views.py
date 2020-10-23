from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    context = {
        'blogs' : Blog.objects.all().order_by('-pub_date')
    }
    return render(request, 'blog/allblogs.html', context)

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog/detail.html', {'blog' : blog})