# from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import FormView

# @ users forms
from .forms import CustomUserCreationForm, CustomUserAuthForm, CustomUserEmailConfirm, CustomUserChangeForm, CompanyDetailsForm, CustomUserChangePasswordForm, ExtendedUserCreationForm, ShippingFormSet

# @ mail
from core.settings import DEFAULT_FROM_EMAIL
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# @ users models
from .models import CompanyDetails, ShippingAddress, CustomUsers

# @ modules
import random

# @ Tools
from tools.inspector import inspect_level, inspect_type

# @ reciver
from django.db.models.signals import pre_save
from django.dispatch import receiver

# ! --------------- Views --------------- ! #


# * ------------------------------------------------------------------- SignUp
class SignUpView(FormView):
    
    # -- class settings
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_finish')
    extra_context = {
        'title': 'Registration'
    }

    # @ POST
    def form_valid(self, form):

        # -- recaptcha
        if self.request.recaptcha_is_valid:

            # -- form is valid
            if form.is_valid():

                # -- create new user
                form.save()

                # -- return form valid
                return super().form_valid(form)

        # -- render template
        return render(self.request, 'signup.html', self.get_context_data())
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


    def get(self, request, *args, **kwargs):
        # @ if user in not anonimus
        if request.user.is_authenticated:
            return redirect(reverse_lazy('user_info'))
        else:
            return super().get(request, *args, **kwargs)


# * ------------------------------------------------------------------- SignUpExtended
class SignUpViewExtended(FormView):
    
    # -- class settings
    template_name = 'signup_extended.html'
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy('signup_extended')
    extra_context = {
        'title': 'Registration'
    }

    # @ POST
    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            if form.is_valid():
            
                # -- create new user
                form.save()

                type = form.cleaned_data.get('user_type')
                type_name = 'user'
                user = CustomUsers.objects.get(username = form.cleaned_data['username'])

                if type == '0':
                    type_name = 'staff'
                    user.is_staff = 1
                    user.user_type = 0
                elif type == '1':
                    type_name = 'user'
                    user.user_type = 1
                elif type == '2':
                    type_name = 'vendor'
                    user.user_type = 2

                user.save()
                
                messages.success(self.request, f'The {type_name} was successfully created')

            # -- return form valid
            return super().form_valid(form)

        # -- render template
        return render(self.request, self.success_url, self.get_context_data())
        
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


    def get(self, request, *args, **kwargs):
        # @ if user in not anonimus
        if request.user.is_authenticated and request.user.is_staff == True:
            return super().get(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('signin'))


# * ------------------------------------------------------------------- SignIn
class SignInView(FormView):

    template_name = 'signin.html'
    form_class = CustomUserAuthForm
    extra_context = {
        'title': 'Authorization'
    }
    success_url = reverse_lazy('email_confirm')

    # * POST
    def form_valid(self, form):
                    
        # -- recaptcha
        if self.request.recaptcha_is_valid:
            # -- form is valid
            user = CustomUsers.objects.get(username=form.cleaned_data.get('username'))
            user_type = user.user_type
            form_type = int(form.cleaned_data.get('user_type'))

            # * client door
            if user_type == form_type and user_type == 1:

                if user.level == 0:
                    user.level = 1

                if form.cleaned_data.get('remember_me') == True or form.cleaned_data.get('remember_me') == 1:
                    user.remember_me = 1

                user.save()

                # -- create secret key
                code = random.randrange(100000, 999999)

                self.request.session['user_email'] = user.email
                self.request.session['user_id'] = user.id
                self.request.session['confirm_code'] = code
                
                # --> send code
                subject = 'Activation code for b2b.Labrilliante.com'
                html_message = render_to_string('_mail_confirm.html', {
                    'login': user.username,
                    'code': code 
                })
                plain_message = strip_tags(html_message)
                from_email = DEFAULT_FROM_EMAIL
                to = user.email
                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

                return redirect(reverse_lazy('email_confirm'))
                
            # * vendor door
            elif user_type == form_type and user_type == 2:
                login(self.request, user)
                return redirect(reverse_lazy('white'))
            else:
                messages.error(self.request, 'Check the correctness of the entered data')
                return redirect(reverse_lazy('signin'))

    def form_invalid(self, form):
        messages.error(self.request, 'Check the correctness of the entered data')
        return super().get(self.request)
    
    # * GET
    def get(self, request, *args, **kwargs):
        # @ if user in not anonimus
        if request.user.is_authenticated:
            return redirect(reverse_lazy('user_info'))
        else:
            return super().get(request, *args, **kwargs)


# * ------------------------------------------------------------------- SignUp finish
def signup_finish(request):
    context = {}
    return render(request, 'signup_finish.html', context)


# * ------------------------------------------------------------------- Confirm
def confirm_user(request):

    # -- try to get user email and id
    try:
        timer = request.session['timer']
    except KeyError:
        timer = False

    try:
        # -- user email
        confirm_code = request.session['confirm_code']
        user_id = request.session['user_id']
        user = CustomUsers.objects.get(pk=user_id)
    except KeyError:
        # -- redirect to signin
        return redirect(reverse_lazy('signin'))


    # -- create confirm form
    form = CustomUserEmailConfirm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if int(form.cleaned_data.get('code')) == int(confirm_code):
                messages.success(request, 'Success, entered code is valid')
                login(request, user)
            else:
                messages.error(request, 'Entered code is not valid')
                return redirect(reverse_lazy('email_confirm'))
   
    # -- create context
    context = {
        'title': 'Email Confirm',
        'form': form,
        'user_email': user.email,
        'timer': timer
    }

    # -- render template
    return render(request, 'confirm.html', context)


# * ------------------------------------------------------------------- Confirm again
def confirm_user_again(request):

    # -- try to get user email and id
    try:
        # -- user email
        user_id = request.session['user_id']
        user = CustomUsers.objects.get(pk=user_id)

    except KeyError:
        # -- redirect to signin
        return redirect(reverse_lazy('signin'))


    # -- get new code
    confirm_code = random.randrange(100000, 999999)
    request.session['confirm_code'] = confirm_code

    # --> send code
    subject = 'Activation code for b2b.Labrilliante.com'
    html_message = render_to_string('_mail_confirm.html', {
        'login': user.username,
        'code': confirm_code 
    })
    plain_message = strip_tags(html_message)
    from_email = DEFAULT_FROM_EMAIL
    to = user.email
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    # -- add message
    messages.info(request, 'New code was sended on your email')
    request.session['timer'] = 60

    # -- return to confirm
    return redirect(reverse_lazy('email_confirm'))


# * ------------------------------------------------------------------- User Info
def user_info(request):

    if not inspect_type(request, 1):
        return redirect(reverse_lazy('signin'))

    if not inspect_level(request, 1):
        return redirect(reverse_lazy('signin'))

    # -- get company form
    def getCompany(request):

        # if compnay is not registered - create company details
        if not CompanyDetails.objects.filter(user_id=request.user.id):
            # create company details
            compnay_details = {
                'user_id': request.user.id
            }
            CompanyDetails.objects.create(**compnay_details)
            # create company details form
            form = CompanyDetailsForm()

        # if compnay is registered - get istance from company details
        else:
            # create company details form with instance
            form = CompanyDetailsForm(instance=CompanyDetails.objects.get(user_id=request.user.id))

        # return form obj
        return form

    # @ POST
    if request.method == 'POST':

        # -- personal details
        user_form = CustomUserChangeForm(request.POST, instance=CustomUsers.objects.get(id=request.user.pk))

        # -- company details
        company_form = CompanyDetailsForm(request.POST, instance=CompanyDetails.objects.get(user_id=request.user.pk))

        # -- shipping details
        shipping_formset = ShippingFormSet(request.POST)
        
        # --> update forms
        if user_form.is_valid():
            user_form.save()
        else:
            messages.error(request, 'A user with this data already exists')
            return redirect(reverse_lazy('user_info'))
        if company_form.is_valid():
            company_form.save()

        # <-- get cleaned data
        clean_data = shipping_formset.cleaned_data 
        
        # -- create exists bool
        exists = False

        # --> update shipping       
        if shipping_formset.has_changed():
            for i, shipping in enumerate(shipping_formset):

                # * commit save
                ship = shipping.save(commit=False)

                # * update user_pk
                if ship.user_id is None:
                    ship.user_id = request.user.pk

                # data is not empty
                for key in clean_data[i]:
                    if (clean_data[i][key] != '' and clean_data[i][key] != ' ' and clean_data[i][key] != None):
                        exists = True
                        
                # if exists save
                if exists:
                    ship.save()
                    exists = False

        if shipping_formset.has_changed() or user_form.has_changed() or company_form.has_changed():
            # -- success message create
            messages.success(request, 'Data has been successfully changed. The manager assigned to you will contact you soon')

            # --> send email for manager
            user = request.user
            user_login = user.username
            user_first_name = user.first_name
            user_last_name = user.last_name
            user_email = user.email
            user_tel = user.tel

            company = CompanyDetails.objects.get(user_id=user.id)
            company_name = company.company_name
            company_email = company.company_email
            company_tel = company.company_tel
            company_address = company.company_address

            manager = CustomUsers.objects.get(pk=user.manager.id)
            manager_email = manager.email

            subject = f'User {user_login} has been updated'
            html_message = render_to_string('_mail_user_updated.html', {
                'fname': user_first_name,
                'lname': user_last_name or '--',
                'login': user_login,
                'user_tel': user_tel or '--',
                'user_email': user_email or '--',

                'company_name': company_name,
                'company_email': company_email,
                'company_tel': company_tel,
                'company_address': company_address,
            })
            plain_message = strip_tags(html_message)
            from_email = DEFAULT_FROM_EMAIL
            if manager_email == '':
                to = DEFAULT_FROM_EMAIL
            else:
                to = manager_email

            mail_result = mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        else:
            messages.info(request, 'You haven\'t made any changes')

        return redirect(reverse_lazy('user_info'))

    # @ GET
    # * shipping formset
    shipping_formset = ShippingFormSet()

    # * user form
    user_form = CustomUserChangeForm(instance=request.user or None)

    # * company form
    company_form = getCompany(request)

    # * shipping address
    shipping_items = ShippingAddress.objects.filter(user_id=request.user.id)

    # * single form
    
    shipping_formset.extra = 1
        
    # -- create context data
    context = {
        'title': 'Client Info',
        'user_form': user_form,
        'company_form': company_form,
        'shipping_formset': shipping_formset
    }
    
    # -- render template
    return render(request, 'user_info.html', context)
            
            
# * ------------------------------------------------------------------- Change password
def change_pass(request):
    
    if not inspect_level(request, 1):
        return redirect(reverse_lazy('signin'))


    # -- create change password form
    form = CustomUserChangePasswordForm(user=request.user)

    # @ POST
    if request.method == 'POST':
        # -- create change password form
        form = CustomUserChangePasswordForm(user=request.user, data=request.POST)
        # -- check valid
        if form.is_valid():
            # save
            form.save()
            # update session
            update_session_auth_hash(request, form.user)
            # create success message
            messages.success(request, 'Your password has been changed')
        else:
            # create error message
            messages.error(request, 'Somthing went wrong')

    # -- create context
    context = {
        'title': 'Change Password',
        'form': form,
    }

    # -- render template
    return render(request, 'change_pass.html', context)


# * ------------------------------------------------------------------- Logout
def logout_view(request):

    form = CustomUserAuthForm

    context = {
        'form': form,
        'title': 'Authorization',
    }

    logout(request)

    return redirect(reverse_lazy('signin'))


# * ------------------------------------------------------------------- update user level
@receiver(pre_save, sender=CustomUsers)
def on_change(sender, instance: CustomUsers, **kwargs):
    if instance.id is None: # new object will be created
        pass # write your code here
    else:
        previous = CustomUsers.objects.get(id=instance.id)
        if previous.level != instance.level: # field will be updated
            if previous.level < instance.level and instance.level >= 2:
                subject = 'Raising the level'
                html_message = render_to_string('_mail_user_raise.html', {
                    'title': 'Your level has been upgraded',
                    'message': 'New features are available to you on the site',
                    'level': instance.level,
                })
                plain_message = strip_tags(html_message)
                from_email = DEFAULT_FROM_EMAIL
                to = instance.email

                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            

