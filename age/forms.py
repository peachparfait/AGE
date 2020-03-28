import bootstrap_datepicker_plus as datetimepicker
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser,Furn, HomeElecApp,Aniversary,Clothes,Other

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','birthday','gender',)
class ElecForm(forms.ModelForm):
    class Meta:
        model = HomeElecApp
        fields = ['name','category','story','birthday','favorite','picture1']
class ElecupdForm(forms.ModelForm):
    class Meta:
        model = HomeElecApp
        fields = ['name','category','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
class FurnForm(forms.ModelForm):
    class Meta:
        model = Furn
        fields = ['name','story','birthday','favorite','picture1']
class FurnupdForm(forms.ModelForm):
    class Meta:
        model = Furn
        fields = ['name','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
class AnivForm(forms.ModelForm):
    class Meta:
        model = Aniversary
        fields = ['annivapp','story','didday','favorite','picture1']
class AnivupdForm(forms.ModelForm):
    class Meta:
        model = Aniversary
        fields = ['annivapp','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['name','category','story','birthday','favorite','picture1']
class OtherupdForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['name','category','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
class ClothForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name','category','story','birthday','favorite','picture1']
class ClothupdForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name','category','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']