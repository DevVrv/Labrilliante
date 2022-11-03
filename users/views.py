from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import FormView

# @ users forms
from .forms import CustomUserCreationForm, CustomUserAuthForm, CustomUserEmailConfirm, CustomUserChangeForm, CompanyDetailsForm, CustomUserChangePasswordForm, ExtendedUserCreationForm, ShippingFormSet

# @ users models
from .models import CompanyDetails, ShippingAddress, CustomUsers

# @ modules
import random

# @ Tools
from tools.inspector import inspect_level, inspect_type

# ! --------------- Views --------------- ! #


# * ------------------------------------------------------------------- SignUp
class SignUpView(FormView):
    
    # -- class settings
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signin')
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
            user_inspect = CustomUsers.objects.get(username=form.cleaned_data.get('username'))
            user_type = user_inspect.user_type
            form_type = int(form.cleaned_data.get('user_type'))

            # * client door
            if user_type == form_type and user_type == 1:

                if user_inspect.level == 0:
                    user_inspect.level = 1

                if form.cleaned_data.get('remember_me') == True or form.cleaned_data.get('remember_me') == 1:
                    user_inspect.remember_me = 1

                user_inspect.save()

                login(self.request, user_inspect)
                return redirect(reverse_lazy('user_info'))
                
            # * vendor door
            elif user_type == form_type and user_type == 2:
                login(self.request, user_inspect)
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


# * ------------------------------------------------------------------- Confirm
def confirm_user(request):

    # -- try to get user email
    try:
        # -- user email
        user_email = request.session['user_email']
    except KeyError:
        # -- redirect to signin
        return redirect(reverse_lazy('signin'))

    # -- create confirm form
    form = CustomUserEmailConfirm()
    
    # -- get user
    user = CustomUsers.objects.filter(username=request.session['user_login'])
    this_user = user.get(username=request.session['user_login'])

    # -- try code resend
    try:
        request.session['resend_code']
        # -- get code from request session
        confirm_code = int(request.session['confirm_code'])
        # -- code whas resended
        resended = True
    except KeyError:
        # -- get code from request session
        confirm_code = int(request.session['confirm_code'])
        # -- code whas not resended
        resended = False

    #  @ POST
    if request.method == 'POST':

        # -- create confirm form
        form = CustomUserEmailConfirm(request.POST)

        #  -- check valid
        if form.is_valid():

            # -- get form code
            form_code = int(form.cleaned_data.get('code'))

            # -- accept code
            if form_code == confirm_code:

                # -- check user level
                if this_user.level == '0':
                    this_user.level = '1'
                
                # -- remember me update
                user.update(remember_me=request.session['remember_me'])
                    
                # -- login in
                login(request, this_user)

                # -- create success message
                messages.success(request, 'Authorization was successful')
            else:
                # -- create error message
                messages.error(request, 'Invalid confirmation code')

    # -- create context
    context = {
        'title': 'Email Confirm',
        'form': form,
        'user_email': user_email,
        'timer': resended
    }

    # -- render template
    return render(request, 'confirm.html', context)


# * ------------------------------------------------------------------- Confirm again
def confirm_user_again(request):
    # -- try to get user email
    try:
        # -- user email
        user_email = request.session['user_email']
    except KeyError:
        # -- redirect to signin
        return redirect(reverse_lazy('signin'))

    # -- resend code
    request.session['resend_code'] = True

    # -- create confirm code
    confirm_code = random.randint(100000, 999999)
    request.session['confirm_code'] = confirm_code

    # -- email settings
    subject = 'Подтверждение email LaBrilliante.com'
    content = f'Ваш код активации: {confirm_code}'
    from_mail = 'dev.vrv@yandex.ru'
    mail = send_mail(subject, content, from_mail, [user_email], fail_silently=False)

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
        if user_form.is_valid():
            user_form.save()
        else:
            print(123)
            messages.error(request, 'A user with this data already exists')
            return redirect(reverse_lazy('user_info'))

        # -- company details
        company_form = CompanyDetailsForm(request.POST, instance=CompanyDetails.objects.get(user_id=request.user.pk))
        if company_form.is_valid():
            company_form.save()


        # -- shipping details
        shipping_formset = ShippingFormSet(request.POST)

        # * get cleaned data
        clean_data = shipping_formset.cleaned_data 
        
        # * create exists bool
        exists = False

        # * update shipping       
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

        # -- success message create
        messages.success(request, 'Data has been successfully changed')

        # -- update user info
        return redirect(reverse_lazy('user_info'))

    # @ GET
    # * shipping formset
    shipping_formset = ShippingFormSet()

    # * user form
    user_form = CustomUserChangeForm(instance=request.user or None)

    # * company form
    company_form = getCompany(request)

    # * shipping address
    shipping_items = ShippingAddress.objects.filter(user_id=request.user.pk)

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