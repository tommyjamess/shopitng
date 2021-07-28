from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Setting, Banner_one
from .models import *
from django.db.models import Avg

# Create your views here.
def products(request):
    setting = Setting.objects.get(pk=1)
    # cat = Category.objects.all()
    brands = Brand.objects.all()
    product = Product.objects.all()
    cat = Category.objects.all()
    # reviews = Review.objects.filter(product__id=id)
    # avg = reviews.aggregate(Avg("rate"))
    

    context = {
        'setting': setting,
        'brands': brands,
        'products': product,
        'cat': cat,
        # 'avg': avg,
    }
    

    return render(request, 'products.html', context)


def prod_detail(request, id):
    product = Product.objects.get(pk=id)
    banner1 = Banner_one.objects.all()
    prodid = Product.objects.get(id=id)
    brands = Brand.objects.all()
    cat = Category.objects.all()
    reviews = Review.objects.filter(product__id=id)
    avg = reviews.aggregate(Avg("rate"))

    

    context = {
        'banner': banner1,
        'product': product,
        'brands': brands,
        'cat': cat,
        'prodid': prodid,
        'reviews': reviews,
        'avg': avg,
    }

    return render(request, 'prod_detail.html', context)


def category(request, id):
    setting = Setting.objects.get(pk=1)
    catego = Product.objects.filter(cat__id=id)
    cat = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'setting': setting,
        'catego': catego,
        'cat': cat,
        'brands': brands,
    }

    return render(request, 'cat.html', context)

def brands(request, id):
    setting = Setting.objects.get(pk=1)
    brand = Product.objects.filter(brand__id=id)
    cat = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'setting': setting,
        'brand': brand,
        'cat': cat,
        'brands': brands,
    }

    return render(request, 'brand.html', context)


def review_rate(request):
    if request.method == "GET":
        prod_id = request.GET.get('prodid')
        print(prod_id, '........')
        product = Product.objects.get(id=prod_id)
        user = request.user
        comment = request.GET.get('comment')
        rate = request.GET.get('rating')
        Review(product=product, user=user, comment=comment, rate=rate).save()

        return redirect('prod_detail', id=prod_id, )
