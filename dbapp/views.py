from django.shortcuts import render, get_object_or_404

from dbapp.models import Blogpost


# Create your views here.

def bloglist(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

def blog_details(request,id):
    post = get_object_or_404(Blogpost,id=id)
    return render(request, 'blog_details.html', {'post':post})
