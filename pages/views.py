from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import ContactForm

def index(request):
    return render(request, 'home/index.html')

def projects_view(request):
    return render(request, 'projects/projects_view.html')

def web_view(request):
    return render(request, 'web/web_view.html')

def iot_view(request):
    return render(request, 'iot/iot_view.html')

def send_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['geric99997@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email/email_view.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')