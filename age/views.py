from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Food,HomeElecApp,Aniversary,Other
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponse
class index(TemplateView):
    template_name = "age/index.html"

class FoodListView(ListView):
    model = Food
    template_name = "age/foodlist.html"
    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': HomeElecApp.objects.all(),
            'object_list3': Aniversary.objects.all(),
            'object_list4': Other.objects.all(),
        })
        return context

    def get_queryset(self):
        return Food.objects.all()

class FoodDetailView(DetailView):
    model = Food
    template_name = "age/food_detail.html"
    success_url = reverse_lazy('age:foodlist')


class FoodCreateView(CreateView):
    model = Food
    template_name = "age/food_create.html"
    fields = ['foodname','foodcategory']
    success_url = reverse_lazy('age:foodlist')

class FoodDeleteView(DeleteView):
    model = Food
    template_name = "age/food_delete.html"
    success_url = reverse_lazy('age:foodlist')

class FoodUpdateView(UpdateView):
    model = Food
    template_name = "age/food_update.html"
    fields = ['foodname','foodcategory']
    success_url = reverse_lazy('age:foodlist')

#家電

class HomeelecDetailView(DetailView):
    model = HomeElecApp
    template_name = "age/homeelec_detail.html"
    success_url = reverse_lazy('age:foodlist')


class HomeelecCreateView(CreateView):
    model = HomeElecApp
    template_name = "age/homeelec_create.html"
    fields = ['HomeElecApp','ElecCategory','story']
    success_url = reverse_lazy('age:foodlist')

class HomeelecDeleteView(DeleteView):
    model = HomeElecApp
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:foodlist')

class HomeelecUpdateView(UpdateView):
    model = HomeElecApp
    template_name = "age/homeelec_update.html"
    fields = ['HomeElecApp','ElecCategory','story']
    success_url = reverse_lazy('age:foodlist')

    #記念日


class AnnivDetailView(DetailView):
    model = Aniversary
    template_name = "age/anniv_detail.html"
    success_url = reverse_lazy('age:foodlist')


class AnnivCreateView(CreateView):
    model = Aniversary
    template_name = "age/anniv_create.html"
    fields = ['annivapp','story']
    success_url = reverse_lazy('age:foodlist')

class AnnivDeleteView(DeleteView):
    model = Aniversary
    template_name = "age/anniv_delete.html"
    success_url = reverse_lazy('age:foodlist')

class AnnivUpdateView(UpdateView):
    model = Aniversary
    template_name = "age/anniv_update.html"
    fields = ['annivapp','story']
    success_url = reverse_lazy('age:foodlist')
#他
class OtherDetailView(DetailView):
    model = Other
    template_name = "age/other_detail.html"
    success_url = reverse_lazy('age:foodlist')


class OtherCreateView(CreateView):
    model = Other
    template_name = "age/other_create.html"
    fields = ['otherapp','story','othercategory']
    success_url = reverse_lazy('age:foodlist')

class OtherDeleteView(DeleteView):
    model = Other
    template_name = "age/other_delete.html"
    success_url = reverse_lazy('age:foodlist')

class OtherUpdateView(UpdateView):
    model = Other
    template_name = "age/other_update.html"
    fields = ['otherapp','story','othercategory']
    success_url = reverse_lazy('age:foodlist')
#新規登録
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('age:complete')
    template_name = 'age/signup.html'

def SignupComplete(request):
    return HttpResponse('<p>あなた宛てに認証用のメールを送信しました</p>')