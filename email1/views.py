from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  
from prakash import settings  
from django.core.mail import send_mail  
  
  
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success Message Has Been Sent By your django App"  
    to      = "prakash.mewari@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  