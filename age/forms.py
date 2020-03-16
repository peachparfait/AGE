import bootstrap_datepicker_plus as datetimepicker
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser,Image,Furn, HomeElecApp,Aniversary,Clothes,Other

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','birthday','gender',)
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture1', 'title']

