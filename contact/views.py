from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage, BadHeaderError

def contact(request):
    """
    Contact view. Take request and send email to the admin.
    """
    # check if the request method is post
    if request.method == "POST":
        # Get data from the submitted data
        message_name = request.POST.get('username')
        message_email = request.POST.get('email')
        message_subject = request.POST.get('subject') 
        message = request.POST.get('message')
        # Send an email
        # EmailMessage( subject, message, email_from, recipient_list )
        try:
            email = EmailMessage(
                f'{message_subject} | {message_name}', # subject & sender's name 
                f'Form: {message_name} \nEmail: {message_email} \nMessage: {message}', # message
                [settings.EMAIL_HOST_USER], # from email
                [settings.EMAIL_HOST_USER], # to email list
                reply_to = [message_email,],
            )
            email.send(fail_silently=False)
            # Display success message
            messages.success(request, ' شكرا لتواصلك معنا. سوف يتم التواصل معك فى أقرب وقت ممكن...')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')      
        return redirect('contact:contact')
    
    return render(request, 'contact/contact.html', {})
