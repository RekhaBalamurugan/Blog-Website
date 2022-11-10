from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Loginuser

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields=('username','email','password')
    
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

    def __init__(self,*args,**kwargs):
        super(UserProfileInfoForm,self).__init__(*args,**kwargs)
        self.fields['portfolio_site'].widget.attrs['class']='form-control'
        self.fields['profile_pic'].widget.attrs['class']='form-control'


class Login(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta():
        model=Loginuser
        fields= ('username','password')




  