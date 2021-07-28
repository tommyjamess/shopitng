from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from products.models import *
from django.contrib import messages

# Create your views here.

def index(request):

    setting = Setting.objects.get(pk=1)
    banner1 = Banner_one.objects.all()
    banner2 = Banner_two.objects.get(pk=1)
    banner3 = Banner_three.objects.get(pk=1)
    brands = Brand.objects.all()
    categories = Category.objects.all()
    featured = Product.objects.filter(featured=True)
    reco = Product.objects.filter(recommended=True)
    cat = Category.objects.all()

    context = {
        'setting': setting,
        'banner': banner1,
        'banner2': banner2,
        'banner3': banner3,
        'brands': brands,
        'cat': categories,
        'featured': featured,
        'reco': reco,
        'cat': cat,
    }
    return render(request, 'home.html', context)

def average(request, id):

    reviews = Review.objects.filter(product__id=id)
    avg = reviews.aggregate(Avg("rate"))
    print(avg, '...................')

    context = {
        'avg':avg,
    }

    return render( request, 'home_content.html', context)


def updateme(request):
    if request.method == 'POST':
        form = UpdateMeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
            return redirect('/')

    return render(request, 'home.html', context)