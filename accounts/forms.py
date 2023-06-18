from django import forms
from . import models

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
import datetime

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control required'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control required'}), label = "Confirm Password")
    
    clg_start = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class':'form-control required', 'id':'clg_start'}))
    clg_end = forms.DateField(initial=datetime.date.today)
    clg_type_choices = (('1','1일'),('5','5일'),('10','10일'),('20','20일'),('30','30일'),('50','50일'),('100','100일'))
    clg_type = forms.ChoiceField(choices=clg_type_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'clg_type'}))
    clg_iter_choices=(('1','1회'),('3','3회'),('5','5회'),('10','10회'),('20','20회'))
    clg_iter = forms.ChoiceField(choices=clg_iter_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'clg_iter'}))
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists.")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
    
    def save(self):
      
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        
        clg_start = self.cleaned_data.get("clg_start")
        #clg_end = self.cleaned_data.get("clg_end")
        clg_type = self.cleaned_data.get("clg_type")
        clg_iter = self.cleaned_data.get("clg_iter")

        user = models.User.objects.create_user(username, email, password)
        
        user.clg_start = clg_start
        #user.clg_end = clg_end
        user.clg_type = clg_type
        user.clg_iter = clg_iter

        user.save()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))

class CustomUserChangeForm(UserChangeForm):
    user = get_user_model()
    password = None
    
    clg_start = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control required', 'id':'clg_start'}))
    clg_end = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control required', 'id':'clg_end'}))

    
    clg_type_choices = (('1','1일'),('5','5일'),('10','10일'),('20','20일'),('30','30일'),('50','50일'),('100','100일'))
    clg_type = forms.ChoiceField(choices=clg_type_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'clg_type'}))
    
    clg_iter_choices=(('1','1회'),('3','3회'),('5','5회'),('10','10회'),('20','20회'))
    clg_iter = forms.ChoiceField(choices=clg_iter_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'clg_iter'}))
    
    noti_bool_choices = (('yes','켜기'),('no','끄기'))
    noti_bool = forms.ChoiceField(choices=noti_bool_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'noti_bool'}))
    
    noti_time_choices = (('07','07시'),('08','08시'),('09','09시'),('10','10시'),('11','11시'),('12','12시'),('13','13시'),('14','14시'),('15','15시'),('16','16시'),('17','17시'),('18','18시'),('19','19시'),('20','20시'),('21','21시'),('22','22시'),('23','23시'))
    noti_time = forms.ChoiceField(choices=noti_time_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'noti_time'}))
    
    user_gender_choices = (('male','남성'),('female','여성'))
    user_gender = forms.ChoiceField(choices=user_gender_choices, widget=forms.Select(attrs={'class':'form-control required', 'id':'user_gender'}))
    
    user_height = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control required', 'placeholder':'175'}))
    user_weight = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control required', 'placeholder':'70'}))    

    class Meta:
        model = get_user_model()
        fields =['clg_start','clg_end','clg_type','clg_iter','noti_bool','noti_time','user_gender','user_height','user_weight']
