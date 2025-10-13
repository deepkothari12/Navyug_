from django.shortcuts import render
from django.shortcuts import render , redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import os
# Create your views here.
##email logic

def contacts(request):
    # print("In contact view")
    if request.method == 'POST':
        # print("Post request")
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, phone, email, message)

        # Create HTML email content
        html_message = render_to_string('emails/contact_email.html', {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
        })
        plain_message = strip_tags(html_message)
        # print("-->", plain_message)
        try:
            send_mail(
                subject=f'New Inquiry from {name}',
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['deepkothari55@gmail.com'],  # where you want to receive messages
                html_message=html_message,
            )
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        except Exception as e:
            messages.error(request, f'Sorry, something went wrong: {e}')

    
        return redirect('/')  # Redirect to same page after submit
    # else:
    #     print("Get request")

    return render(request, 'main.html')  # Or your main page template