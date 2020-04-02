from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Furn,HomeElecApp,Aniversary,Other,Clothes,FurnHistory,ElecHistory,AnivHistory,ClothHistory,OtherHistory,History
from django.urls import reverse_lazy,reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,ElecForm,ElecupdForm,FurnForm,FurnupdForm,AnivForm,AnivupdForm,OtherForm,OtherupdForm,ClothForm,ClothupdForm,HistoryForm
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
import requests

webhook_url = 'https://discordapp.com/api/webhooks/693136691346669640/g7AluYkGKBzc1p_ri9GPEKtuesSVl7rE_edxKEiKnbFLxfG5oXu0AGg5i4JV0KtGcymi'
 
main_content = {
  "content": "起動しました"
}
requests.post(webhook_url,main_content)
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
class FurnHistoryView(CreateView):
    model = FurnHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10','mdl']
    def get_success_url(self):
        return reverse_lazy('age:furndetail', kwargs={'pk': self.object.pk})
class FurnHistoryupdView(UpdateView):
    model = FurnHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10']
    def get_success_url(self):
        return reverse_lazy('age:furndetail', kwargs={'pk': self.object.pk})
class FurnDetailView(DetailView):
    model = Furn
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(FurnDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': FurnHistory.objects.filter(pk=self.kwargs['pk']),
            'type':'furn',
        })
        return context

    def get_queryset(self):
        return Furn.objects.all()
    success_url = reverse_lazy('age:list')


def furncreate(request):
    if request.method == "POST":
        form = FurnForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = FurnForm()

    context = {'form':form}
    return render(request, 'age/furn_create.html', context)

class FurnDeleteView(DeleteView):
    model = Furn
    template_name = "age/furn_delete.html"
    success_url = reverse_lazy('age:list')

def history(request,num):
    print(HomeElecApp.objects.get(pk=num))
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            historykey = History.objects.count() + 1
            form.save()
            print(historykey)
            form2 = History.objects.get(pk=historykey)
            form2.mdl=HomeElecApp.objects.get(pk=num)
            form2.save()
            return redirect('age:homeelecdetail', kwargs={'pk': num})
    else:
        form = HistoryForm()

    context = {'form':form}
    return render(request, 'age/historycreate.html', context)
def furnupdate(request,pk):
    if request.method == "POST":
        form = FurnupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = FurnupdForm()
    context = {'form':form}
    return render(request, 'age/homeelec_update.html', context)

#家電
class ElecHistoryView(CreateView):
    model = ElecHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10']
    def get_success_url(self):
        return reverse_lazy('age:homeelecdetail', kwargs={'pk': self.object.pk})
class ElecHistoryupdView(UpdateView):
    model = History
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10']
    def get_success_url(self):
        return reverse_lazy('age:list')
class HomeelecDetailView(DetailView):
    model = HomeElecApp
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(HomeelecDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': History.objects.filter(mdl__pk=self.object.pk),
            'type':'elec',
        })
        return context

    def get_queryset(self):
        return HomeElecApp.objects.all()
    success_url = reverse_lazy('age:list')




def eleccreate(request):
    if request.method == "POST":
        form = ElecForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = ElecForm()

    context = {'form':form}
    return render(request, 'age/homeelec_create.html', context)

class HomeelecDeleteView(DeleteView):
    model = HomeElecApp
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')


def elecupdate(request,pk):
    if request.method == "POST":
        form = ElecupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = ElecupdForm()
    context = {'form':form}
    return render(request, 'age/homeelec_update.html', context)
    #記念日


class AnnivDetailView(DetailView):
    model = Aniversary
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(AnnivDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': AnivHistory.objects.filter(pk=self.kwargs['pk']),
            'type':'aniv',
        })
        return context

    def get_queryset(self):
        return Aniversary.objects.all()
    success_url = reverse_lazy('age:list')
class AnivHistoryView(CreateView):
    model = AnivHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10','mdl']
    def get_success_url(self):
        return reverse_lazy('age:anivdetail', kwargs={'pk': self.object.pk})
class AnivHistoryupdView(UpdateView):
    model = AnivHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10']
    def get_success_url(self):
        return reverse_lazy('age:anivdetail', kwargs={'pk': self.object.pk})

def anivcreate(request):
    if request.method == "POST":
        form = AnivForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = AnivForm()

    context = {'form':form}
    return render(request, 'age/anniv_create.html', context)

class AnnivDeleteView(DeleteView):
    model = Aniversary
    template_name = "age/anniv_delete.html"
    success_url = reverse_lazy('age:list')

def anivupdate(request,pk):
    if request.method == "POST":
        form = AnivupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = AnivupdForm()

    context = {'form':form}
    return render(request, 'age/anniv_update.html', context)
#ファッション
class ClothesDetailView(DetailView):
    model = Clothes
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(ClothesDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': ClothHistory.objects.filter(pk=self.kwargs['pk']),
            'type':'cloth',
        })
        return context

    def get_queryset(self):
        return Clothes.objects.all()
    success_url = reverse_lazy('age:list')
class ClothHistoryView(CreateView):
    model = ClothHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10','mdl']
    def get_success_url(self):
        return reverse_lazy('age:fashiondetail', kwargs={'pk': self.object.pk})
class ClothHistoryupdView(UpdateView):
    model = ClothHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10']
    def get_success_url(self):
        return reverse_lazy('age:fashiondetail', kwargs={'pk': self.object.pk})
def clothcreate(request):
    if request.method == "POST":
        form = ClothForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = ClothForm()

    context = {'form':form}
    return render(request, 'age/clothes_create.html', context)

class ClothesDeleteView(DeleteView):
    model = Clothes
    template_name = "age/clothes_delete.html"
    success_url = reverse_lazy('age:list')

def clothupdate(request,pk):
    if request.method == "POST":
        form = ClothupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = ClothupdForm()

    context = {'form':form}
    return render(request, 'age/clothes_update.html', context)
#他
class OtherDetailView(DetailView):
    model = Other
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(OtherDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': OtherHistory.objects.filter(pk=self.kwargs['pk']),
            'type':'other',
        })
        return context

    def get_queryset(self):
        return Other.objects.all()
    success_url = reverse_lazy('age:list')

class OtherHistoryView(CreateView):
    model = OtherHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10','mdl']
    def get_success_url(self):
        return reverse_lazy('age:otherdetail', kwargs={'pk': self.object.pk})
class OtherHistoryupdView(UpdateView):
    model = OtherHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1','history2','historyday2','history3','historyday3','history4','historyday4','history5','historyday5','history6','historyday6','history7','historyday7','history8','historyday8','history9','historyday9','history10','historyday10']
    def get_success_url(self):
        return reverse_lazy('age:otherdetail', kwargs={'pk': self.object.pk})
def othercreate(request):
    if request.method == "POST":
        form = OtherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = OtherForm()

    context = {'form':form}
    return render(request, 'age/other_create.html', context)

class OtherDeleteView(DeleteView):
    model = Other
    template_name = "age/other_delete.html"
    success_url = reverse_lazy('age:list')

def otherupdate(request,pk):
    if request.method == "POST":
        form = OtherupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = OtherupdForm()

    context = {'form':form}
    return render(request, 'age/other_update.html', context)
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
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    return HttpResponse('OK')

@handler.add(MessageEvent, message=TextMessage)
def text_message_handler(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage('test'))

if __name__ == '__main__':
    pass