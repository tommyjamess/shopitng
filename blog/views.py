from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from home.models import Setting
from .models import *
from products.models import *
from user.models import UserProfile
# Create your views here.

def blogcontent(request):
    setting = Setting.objects.get(pk=1)
    blog_items = Post.objects.all()
    cat = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'setting': setting,
        'list': blog_items,
        'cat': cat,
        'brands': brands,
    }


    return render (request, 'bloglist.html', context)


def blogdetail(request, id, slug):
    template_name = 'blogdetail.html'
    post = get_object_or_404(Post, slug=slug)
    response = post.responses.filter(active=True)

    new_response = None

    if request.method == 'POST':
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            new_response = form.save(commit=False)
            new_response.post = post
            new_response.save()

    setting = Setting.objects.get(pk=1)
    detail = Post.objects.get(pk=id)
    cat = Category.objects.all()
    brands = Brand.objects.all()
    
    


    context = {
        'setting': setting,
        'blog': detail,
        'responses': response,
        'cat': cat,
        'brands': brands
        
    }

    return render(request, template_name, context)

