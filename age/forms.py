import bootstrap_datepicker_plus as datetimepicker
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser,ElecImage,Furn, HomeElecApp,Aniversary,Clothes,Other

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','birthday','gender',)
class ElecImageForm(forms.ModelForm):
    class Meta:
        model = ElecImage
        fields = ['picture1']
class ElecForm(forms.ModelForm):
    class Meta:
        model = HomeElecApp
        fields = ['HomeElecApp','ElecCategory','story','favorite','birthday']
