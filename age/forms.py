import bootstrap_datepicker_plus as datetimepicker
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser,Furn, HomeElecApp,Aniversary,Clothes,Other,ElecHistory,FurnHistory,AnivHistory,ClothHistory,OtherHistory,FurnImage,ElecImage,AnivImage,ClothImage,OtherImage

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
        fields = ['name','category','story','favorite','picture1']
class FurnForm(forms.ModelForm):
    class Meta:
        model = Furn
        fields = ['name','story','birthday','favorite','picture1']
class FurnupdForm(forms.ModelForm):
    class Meta:
        model = Furn
        fields = ['name','story','favorite','picture1']
class AnivForm(forms.ModelForm):
    class Meta:
        model = Aniversary
        fields = ['annivapp','story','didday','favorite','picture1']
class AnivupdForm(forms.ModelForm):
    class Meta:
        model = Aniversary
        fields = ['annivapp','story','favorite','picture1']
class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['name','category','story','birthday','favorite','picture1']
class OtherupdForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['name','category','story','favorite','picture1']
class ClothForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name','category','story','birthday','favorite','picture1']
class ClothupdForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name','category','story','favorite','picture1']
class ElecHistoryForm(forms.ModelForm):
    class Meta:
        model = ElecHistory
        fields = ['history1','historyday1']
class FurnHistoryForm(forms.ModelForm):
    class Meta:
        model = FurnHistory
        fields = ['history1','historyday1']
class AnivHistoryForm(forms.ModelForm):
    class Meta:
        model = AnivHistory
        fields = ['history1','historyday1']
class ClothHistoryForm(forms.ModelForm):
    class Meta:
        model = ClothHistory
        fields = ['history1','historyday1']
class OtherHistoryForm(forms.ModelForm):
    class Meta:
        model = OtherHistory
        fields = ['history1','historyday1']
class ElecImageForm(forms.ModelForm):
    class Meta:
        model = ElecImage
        fields = ['picture']
class FurnImageForm(forms.ModelForm):
    class Meta:
        model = FurnImage
        fields = ['picture']
class AnivImageForm(forms.ModelForm):
    class Meta:
        model = AnivImage
        fields = ['picture']
class ClothImageForm(forms.ModelForm):
    class Meta:
        model = ClothImage
        fields = ['picture']
class OtherImageForm(forms.ModelForm):
    class Meta:
        model = OtherImage
        fields = ['picture']
class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label