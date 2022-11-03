from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

subject = 'Subject'
html_message = render_to_string('mail_template.html', {'context': 'values'})
plain_message = strip_tags(html_message)
from_email = 'From <from@example.com>'
to = 'to@example.com'

mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
