from django.urls import path
from .views import send_message

urlpatterns = [

    path('test/', send_message, name='test_mail')

]
