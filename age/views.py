from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Furn,HomeElecApp,Aniversary,Other,Clothes
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,ElecForm
from django.http import HttpResponse,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    FollowEvent, TextSendMessage,MessageEvent,TextMessage ,ImageMessage, AudioMessage
)
import os
from django.views import generic
from . import models

class index(TemplateView):
    template_name = "age/index.html"
class GalleryView(ListView):
    model = Furn
    template_name = "age/gallery.html"
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': HomeElecApp.objects.all(),
            'object_list3': Aniversary.objects.all(),
            'object_list4': Other.objects.all(),
            'object_list5': Clothes.objects.all(),

        })
        return context

    def get_queryset(self):
        return Furn.objects.all()
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


class FurnCreateView(CreateView,generic.edit.ModelFormMixin):
    model = Furn
    template_name = "age/furn_create.html"
    fields = ['furnname','favorite','birthday','story','picture1']
    success_url = reverse_lazy('age:list')

class FurnDeleteView(DeleteView):
    model = Furn
    template_name = "age/furn_delete.html"
    success_url = reverse_lazy('age:list')

class FurnUpdateView(UpdateView):
    model = Furn
    template_name = "age/furn_update.html"
    fields = ['furnname','favorite','story','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
    success_url = reverse_lazy('age:list')

#家電

class HomeelecDetailView(DetailView):
    model = HomeElecApp
    template_name = "age/homeelec_detail.html"
    success_url = reverse_lazy('age:list')


#class HomeelecCreateView(CreateView,generic.edit.ModelFormMixin):
#    model = HomeElecApp
#    template_name = "age/homeelec_create.html"
#    fields = ['HomeElecApp','ElecCategory','story','birthday','favorite','picture1']
#    success_url = reverse_lazy('age:list')

def eleccreate(request):
    if request.method == "POST":
        form = ElecForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:gallery')
    else:
        form = ElecForm()

    context = {'form':form}
    return render(request, 'age/homeelec_create.html', context)

class HomeelecDeleteView(DeleteView):
    model = HomeElecApp
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')

class HomeelecUpdateView(UpdateView):
    model = HomeElecApp
    template_name = "age/homeelec_update.html"
    fields = ['HomeElecApp','ElecCategory','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
    success_url = reverse_lazy('age:list')

    #記念日


class AnnivDetailView(DetailView):
    model = Aniversary
    template_name = "age/anniv_detail.html"
    success_url = reverse_lazy('age:list')


class AnnivCreateView(CreateView):
    model = Aniversary
    template_name = "age/anniv_create.html"
    fields = ['annivapp','story','favorite','didday','picture1']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'imageform': ImageForm(**self.get_form_kwargs()),
        })
        return context
    success_url = reverse_lazy('age:list')

class AnnivDeleteView(DeleteView):
    model = Aniversary
    template_name = "age/anniv_delete.html"
    success_url = reverse_lazy('age:list')

class AnnivUpdateView(UpdateView):
    model = Aniversary
    template_name = "age/anniv_update.html"
    fields = ['annivapp','story','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
    success_url = reverse_lazy('age:list')
#ファッション
class ClothesDetailView(DetailView):
    model = Clothes
    template_name = "age/clothes_detail.html"
    success_url = reverse_lazy('age:list')


class ClothesCreateView(CreateView):
    model = Clothes
    template_name = "age/clothes_create.html"
    fields = ['fashionapp','story','fashioncategory','favorite','birthday','picture1']
    success_url = reverse_lazy('age:list')

class ClothesDeleteView(DeleteView):
    model = Clothes
    template_name = "age/clothes_delete.html"
    success_url = reverse_lazy('age:list')

class ClothesUpdateView(UpdateView):
    model = Clothes
    template_name = "age/clothes_update.html"
    fields = ['fashionapp','story','fashioncategory','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
    success_url = reverse_lazy('age:list')
#他
class OtherDetailView(DetailView):
    model = Other
    template_name = "age/other_detail.html"
    success_url = reverse_lazy('age:list')


class OtherCreateView(CreateView):
    model = Other
    template_name = "age/other_create.html"
    fields = ['otherapp','story','othercategory','favorite','birthday','picture1']
    success_url = reverse_lazy('age:list')

class OtherDeleteView(DeleteView):
    model = Other
    template_name = "age/other_delete.html"
    success_url = reverse_lazy('age:list')

class OtherUpdateView(UpdateView):
    model = Other
    template_name = "age/other_update.html"
    fields = ['otherapp','story','othercategory','favorite','picture1','picture2','picture3','picture4','picture5','picture6','picture7','picture8','picture9','picture10']
    success_url = reverse_lazy('age:list')
#新規登録
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('age:complete')
    template_name = 'age/signup.html'

def SignupComplete(request):
    return HttpResponse('<p>あなた宛てに認証用のメールを送信しました</p>')

#def gallery(request):
#    images = ElecImage.objects.all()
#    context = {'images':images}
#    return render(request, 'age/gallery.html', context)

line_bot_api = LineBotApi(
    'BgIceHXEglDdSNcoKGWIxrTAxV3fjtGmutHrIRmECG+nQRyz4kia4yc0a5KsLR23jZ+Je5fQAvaMHoe2vJvL7tqNiUBqBJfZ91OES+2pzBlouySfC9ZMBSnNWyvPIzm7s2HqX53HcQ7ChMti95PgYwdB04t89/1O/w1cDnyilFU='
)

handler = WebhookHandler('7ff9f107074b10d0aa0168d546285585')

@csrf_exempt
def webhook(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        # 署名の検証を行い、成功した場合にhandleされたメソッドを呼び出す
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    return HttpResponse('OK')

@handler.add(MessageEvent, message=TextMessage)
def text_message_handler(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage('test'))

if __name__ == '__main__':
    pass