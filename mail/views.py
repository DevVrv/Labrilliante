import json
from django.http import HttpResponse
from django.core.mail import send_mail

from users.models import CustomUsers

def send_message(request, title, message):
    
    # <-- get user
    user = request.user
    user_mail = user.mail

    # <-- get manager
    manager = CustomUsers.objects.get(pk=request.user.manager_id)
    manager_email = manager.email

    # --> send mail
    if manager_email != '' and manager_email != NULL and user_mail != '' and user_mail != NULL:
        send_mail(
            'Test for email',
            'Hello message.',
            'dev.vrv@gmail.com',
            ['vrv.lfm@gmail.com'],
            fail_silently=False
        )

    ressponce = {
        'message': 'success'
    }

    return HttpResponse (json.dumps(ressponce), content_type="application/json")
