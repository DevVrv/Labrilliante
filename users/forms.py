from django import forms
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUsers, CompanyDetails, ShippingAddress

# * signup form
class CustomUserCreationForm(UserCreationForm):

    user_type = forms.CharField(initial=1, required=False, max_length=1, widget=forms.RadioSelect(attrs={
        'class': 'd-none'
    }))
    
    username = forms.CharField(max_length=150, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'User Name'
        }))

    email = forms.CharField(required=True, max_length=255, label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        
        }))

    tel = forms.IntegerField(required=True, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tel',

        }))

    password1 = forms.CharField(max_length=150, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
        }))

    password2 = forms.CharField(max_length=150, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat the password'
        }))

    class Meta:
        model = CustomUsers
        fields = ('username', 'email', 'tel')

# * signup form
class ExtendedUserCreationForm(UserCreationForm):

    user_types = (
        (0, 'Staff'),
        (1, 'User'),
        (2, 'Vendor'),
    )

    user_type = forms.ChoiceField(initial=0, choices=user_types, widget=forms.Select(attrs={
        'class': 'form-select'
    }))
    
    username = forms.CharField(max_length=150, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'User Name'
    }))

    email = forms.CharField(required=False, max_length=255, label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        
    }))

    tel = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tel',

    }))

    password1 = forms.CharField(max_length=150, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
        }))

    password2 = forms.CharField(max_length=150, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat the password'
        }))

    class Meta:
        model = CustomUsers
        fields = ('username', 'email', 'tel')

# * signin form
class CustomUserAuthForm(AuthenticationForm):

    user_types = (
        (1, 'Client'),
        (2, 'Vendor'),
    )

    username = forms.CharField(max_length=150, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'User Name'
        }))

    password = forms.CharField(max_length=150, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
        }))

    user_type = forms.ChoiceField(choices=user_types, widget=forms.RadioSelect(attrs={'class': 'd-none switcher'}), initial='1')

    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'checkbox d-none',
        }))

# * email confirm form
class CustomUserEmailConfirm(forms.Form):
    # code input
    code = forms.CharField(max_length=6, min_length=6, label='', 
    widget=forms.NumberInput(attrs={
        'class': 'form-control text-center px-0',
        'placeholder': 'Enter Code'
    }))

# * change password form
class CustomUserChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(max_length=150, min_length=8, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter old password'
    }))
    new_password1 = forms.CharField(max_length=150, min_length=8, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter new password'
    }))
    new_password2 = forms.CharField(max_length=150, min_length=8, label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat new password'
    }))
    
    model = CustomUsers
    fields = ['old_password', 'new_password1', 'new_password2']
 
# * change client info form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsers
        fields = ['first_name', 'last_name', 'job_title', 'email', 'tel']
        widgets = {
            'first_name': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'last_name': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'email': forms.EmailInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info'}),
            'tel': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'job_title': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
        }

# * company details form
class CompanyDetailsForm(forms.ModelForm):
    class Meta:
        model = CompanyDetails
        fields = [
            'company_name', 
            'company_address', 
            'company_city', 
            'company_country', 
            'company_region', 
            'company_zip', 
            'company_tel', 
            'company_email', 
            'company_web_address'
            ]
        widgets = {
            'company_name': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_tel': forms.NumberInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_email': forms.EmailInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info'}),
            'company_address': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_city': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_web_address': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_region': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_country': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
            'company_zip': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
        }

# * shipping formset
ShippingFormSet = modelformset_factory(
    ShippingAddress, 
    fields=(
        'shipping_company_name', 
        'shipping_attention_name',
        'shipping_address', 
        'shipping_city', 
        'shipping_country', 
        'shipping_region', 
        'shipping_zip', 
        'shipping_tel', 
        'shipping_email', 
    ),
    widgets = {
    'shipping_company_name': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_attention_name': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_tel': forms.NumberInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_email': forms.EmailInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_address': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_city': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_region': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_country': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}),
    'shipping_zip': forms.TextInput(attrs={'disabled': 'true', 'class': 'form-control form-control-client-info w-100 rounded mt-2'}), 
    },
    extra=1,
    
)




    