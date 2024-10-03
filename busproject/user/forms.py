from django import forms
from django.contrib.auth.models import User
from owner.models import Bus,Tickets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta: 
       model=User
       fields=['username','email','password1','password2']

       widgets={
       'username':forms.TextInput(attrs={"class":'form-control'}),
       'email':forms.EmailInput(attrs={"class":'form-control'}),
}
       

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
        'username':forms.TextInput(attrs={"class":'form-control', "placeholder": "Enter your username"}),

         'password':forms.PasswordInput(attrs={"class":'form-control',"placeholder": "Enter your password"}),
    }

class SearchBusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','destination','date']
        widgets={
            'source':forms.TextInput(attrs={"class":'form-control',"placeholder": "Enter your source"}),
            
            'destination':forms.TextInput(attrs={"class":'form-control',"placeholder": "Enter your destination"}),

           'date': forms.DateInput(attrs={"class": 'form-control', "type": "date"}), 
            
    }

class BookTicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('name', 'phone_number', 'email', 'seats')
        

    bus = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    source = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    destination = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'readonly': 'readonly'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'readonly': 'readonly'}))
    fare = forms.DecimalField(widget=forms.NumberInput(attrs={'readonly': 'readonly'}))









        
            

        
        
    # name = forms.CharField(label='Name', max_length=255)
    # phone_number = forms.CharField(label='Phone Number', max_length=20)
    # email = forms.EmailField(label='Email')
    # bus = forms.ModelChoiceField(queryset=Bus.objects.all(), label='Select Bus')

