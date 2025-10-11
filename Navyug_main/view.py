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

##email logic
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create HTML email content
        html_message = render_to_string('emails/contact_email.html', {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
        })
        plain_message = strip_tags(html_message)
        print("-->", plain_message)
        try:
            send_mail(
                subject=f'New Inquiry from {name}',
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['deepkothari923@gmail.com'],  # where you want to receive messages
                html_message=html_message,
            )
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        except Exception as e:
            messages.error(request, f'Sorry, something went wrong: {e}')

    
        return redirect('contact')  # Redirect to same page after submit
    # else:
    #     print("Get request")

    return render(request, 'main.html')  # Or your main page template