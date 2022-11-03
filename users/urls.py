from django.urls import path
from .views import SignUpView, SignInView, SignUpViewExtended, confirm_user, change_pass, confirm_user_again, user_info, logout_view

from .decorators import check_recaptcha

urlpatterns = [

    # * -------------------------------------------------------------------- create new user
    path('signup/', check_recaptcha(SignUpView.as_view()), name='signup'),

    # * -------------------------------------------------------------------- create new user
    path('signup/extended/', check_recaptcha(SignUpViewExtended.as_view()), name='signup_extended'),

    # * -------------------------------------------------------------------- login in user
    path('signin/', check_recaptcha(SignInView.as_view()), name='signin'),

    # * -------------------------------------------------------------------- sign_out
    path('signout/', logout_view, name='signout'),

    # * -------------------------------------------------------------------- email confirm
    path('confirm/', confirm_user, name='email_confirm'),

    # * -------------------------------------------------------------------- email confirm
    path('confirm/again/', confirm_user_again, name='email_confirm_again'),

    # * -------------------------------------------------------------------- client info 
    path('info/', user_info, name='user_info'),
    
    # * -------------------------------------------------------------------- password change
    path('change_pass', change_pass, name='change_pass'),

]
