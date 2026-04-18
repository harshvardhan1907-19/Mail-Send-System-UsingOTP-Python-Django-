from django.shortcuts import render
from .forms import Smtp
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import random
import django.contrib.sessions

def send_mail_(request):

    form = Smtp()

    if  request.method == "POST":
        form =  Smtp(request.POST)

        if 'send_otp' in request.POST and form.is_valid():
            otp = random.randint(100000,999999)
            request.session['otp'] = str(otp)
            request.session['form_data'] = form.cleaned_data

            send_mail(
                subject="Your OTP",
                message=f"Your OTP is {otp}",
                from_email='Techmicra pvt ltd <YOUR EMAIL NAME>',
                recipient_list=[form.cleaned_data['to']],
            )

            messages.info(request, "otp sent!")

        elif 'verify_otp' in request.POST:
            user_otp = request.POST.get('otp')
            session_otp = request.session.get('otp')

            if user_otp == session_otp:
                data = request.session.get('form_data')

                send_mail(
                    subject=data['subject'],
                    message=data['message'],
                    from_email='Techmicra pvt ltd <YOUR EMAIL NAME>',
                    recipient_list=[data['to']],
                    fail_silently=False,
                )

                request.session.pop('otp', None)
                request.session.pop('form_data', None)

                messages.success(request, "Email sent successfully")
                # show success message or clear form
                form = Smtp()
            else:
                messages.error(request, "Invalid otp")
                # return render(request, 'Reply.html', {'mailInfo':mail_info})

    return render(request, 'mail.html', {"mailForm":form})