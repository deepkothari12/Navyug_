from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , Http404
from . models import Category
from store.models import product

# Create your views here.
# def product_categories_(request):
#     return HttpResponse("Hello Worlds")

def only_specify_categories(request , category_slug = None):

    categoryes = None
    products = None

    if category_slug is not None:
        categoryes = get_object_or_404(Category , category_slug = category_slug)
        # print("--->>>>>>>>",categoryes)
        products = product.objects.filter(category_fk = categoryes)

    context = {
    'product': products,
    'categoryes': categoryes
    }


    return render(
        request = request , 
        template_name = "categories.html",
        context = context
    )

def product_details(request , category_slug = None , product_slug = None):
    

    # print("functionsssssssss callinggggg" , category_slug , product_slug )
    try : 
        single_product = product.objects.get(
                category_fk__category_slug = category_slug,
                product_slug = product_slug
            )
        print("----------------->>>>>>>>" , single_product)
    except product.DoesNotExist:
        single_product = None
        # print("Product not found")
        raise Http404("Product not found")
    
    context = {
        'single_product': single_product,
        # 'products_count': product_count
    }
    

    return render(request , "product_details.html" , context = context)