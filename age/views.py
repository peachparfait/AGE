from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Furn,HomeElecApp,Aniversary,Other,Clothes,Image
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,ImageForm
from django.http import HttpResponse
class index(TemplateView):
    template_name = "age/index.html"

class FurnListView(ListView):
    model = Furn
    template_name = "age/list.html"
    def get_context_data(self, **kwargs):
        context = super(FurnListView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': HomeElecApp.objects.all(),
            'object_list3': Aniversary.objects.all(),
            'object_list4': Other.objects.all(),
            'object_list5': Clothes.objects.all(),

        })
        return context

    def get_queryset(self):
        return Furn.objects.all()

class FurnDetailView(DetailView):
    model = Furn
    template_name = "age/furn_detail.html"
    success_url = reverse_lazy('age:list')


class FurnCreateView(CreateView):
    model = Furn
    template_name = "age/furn_create.html"
    fields = ['furnname']
    success_url = reverse_lazy('age:list')

class FurnDeleteView(DeleteView):
    model = Furn
    template_name = "age/furn_delete.html"
    success_url = reverse_lazy('age:list')

class FurnUpdateView(UpdateView):
    model = Furn
    template_name = "age/furn_update.html"
    fields = ['furnname']
    success_url = reverse_lazy('age:list')

#家電

class HomeelecDetailView(DetailView):
    model = HomeElecApp
    template_name = "age/homeelec_detail.html"
    success_url = reverse_lazy('age:list')


class HomeelecCreateView(CreateView):
    model = HomeElecApp
    template_name = "age/homeelec_create.html"
    fields = ['HomeElecApp','ElecCategory','story','favorite']
    success_url = reverse_lazy('age:list')

class HomeelecDeleteView(DeleteView):
    model = HomeElecApp
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')

class HomeelecUpdateView(UpdateView):
    model = HomeElecApp
    template_name = "age/homeelec_update.html"
    fields = ['HomeElecApp','ElecCategory','story','favorite']
    success_url = reverse_lazy('age:list')

    #記念日


class AnnivDetailView(DetailView):
    model = Aniversary
    template_name = "age/anniv_detail.html"
    success_url = reverse_lazy('age:list')


class AnnivCreateView(CreateView):
    model = Aniversary
    template_name = "age/anniv_create.html"
    fields = ['annivapp','story','favorite']
    success_url = reverse_lazy('age:list')

class AnnivDeleteView(DeleteView):
    model = Aniversary
    template_name = "age/anniv_delete.html"
    success_url = reverse_lazy('age:list')

class AnnivUpdateView(UpdateView):
    model = Aniversary
    template_name = "age/anniv_update.html"
    fields = ['annivapp','story','favorite']
    success_url = reverse_lazy('age:list')
#ファッション
class ClothesDetailView(DetailView):
    model = Clothes
    template_name = "age/clothes_detail.html"
    success_url = reverse_lazy('age:list')


class ClothesCreateView(CreateView):
    model = Clothes
    template_name = "age/clothes_create.html"
    fields = ['fashionapp','story','fashioncategory','favorite']
    success_url = reverse_lazy('age:list')

class ClothesDeleteView(DeleteView):
    model = Clothes
    template_name = "age/clothes_delete.html"
    success_url = reverse_lazy('age:list')

class ClothesUpdateView(UpdateView):
    model = Clothes
    template_name = "age/clothes_update.html"
    fields = ['fashionapp','story','fashioncategory','favorite']
    success_url = reverse_lazy('age:list')
#他
class OtherDetailView(DetailView):
    model = Other
    template_name = "age/other_detail.html"
    success_url = reverse_lazy('age:list')


class OtherCreateView(CreateView):
    model = Other
    template_name = "age/other_create.html"
    fields = ['otherapp','story','othercategory','favorite']
    success_url = reverse_lazy('age:list')

class OtherDeleteView(DeleteView):
    model = Other
    template_name = "age/other_delete.html"
    success_url = reverse_lazy('age:list')

class OtherUpdateView(UpdateView):
    model = Other
    template_name = "age/other_update.html"
    fields = ['otherapp','story','othercategory','favorite']
    success_url = reverse_lazy('age:list')
#新規登録
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('age:complete')
    template_name = 'age/signup.html'

def SignupComplete(request):
    return HttpResponse('<p>あなた宛てに認証用のメールを送信しました</p>')

def gallery(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'age/gallery.html', context)
def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:gallery')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'age/upload.html', context)