from django.shortcuts import render , redirect
from product_categories.models import Category
from django.http import FileResponse, Http404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import os
from django.conf import settings

def home_page(request):

    Categorys = Category.objects.all()

    # print(Categorys)
    context = {
        'categories' : Categorys
    }

    return render(request, 'main.html' , context=context)

def download_brochure(request):
    brochure_path = os.path.join(settings.MEDIA_ROOT, 'brocher', 'brochure_navayuga.pdf')

    if os.path.exists(brochure_path):
        return FileResponse(open(brochure_path, 'rb'), as_attachment=True, filename='Product-Brochure.pdf')
    else:
        raise Http404("Brochure not found.")
    

    return render(request, 'main.html')

