from django.shortcuts import render
from django.core.mail import send_mail
from .models import RegisteredUser
from .forms import EmailForm
from django.conf import settings

def send_email_to_users(request):
    users = RegisteredUser.objects.all()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [user.email for user in users]

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # sender
                recipient_list,            # receivers
                fail_silently=False,
            )
            return render(request, 'send_email.html', {'form': form, 'success': True})
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})