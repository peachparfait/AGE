from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Furn,HomeElecApp,Aniversary,Other,Clothes,FurnHistory,ElecHistory,AnivHistory,ClothHistory,OtherHistory,FurnImage,ElecImage,AnivImage,ClothImage,OtherImage,CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,ElecForm,ElecupdForm,FurnForm,FurnupdForm,AnivForm,AnivupdForm,OtherForm,OtherupdForm,ClothForm,ClothupdForm,ElecHistoryForm,FurnHistoryForm,AnivHistoryForm,ClothHistoryForm,OtherHistoryForm,ElecImageForm,FurnImageForm,AnivImageForm,ClothImageForm,OtherImageForm,LoginForm
from django.http import HttpResponse,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
import schedule
import time
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from linebot.models import (
    FollowEvent, TextSendMessage,MessageEvent,TextMessage ,ImageMessage, AudioMessage
)
import os
from django.views import generic
from . import models
import requests
import json
from itertools import chain
from django.contrib.auth.views import LoginView, LogoutView
df=0
with open('age/key.json') as f:
    df = json.load(f)
webhook_url = df["webhook_url"]
print(df)
main_content = {
  "content": "起動しました"
}
requests.post(webhook_url,main_content)
def job():
    now = datetime.date.today()
    for i in chain(HomeElecApp.objects.all(),Other.objects.all(),Clothes.objects.all(),Furn.objects.all()):
        elecage = i.birthday
        print(elecage)
        if now.day == elecage.day: #今日が誕生日！！！！！！
            main_content = {
                "content": "今日は" + str(i.name) + "の誕生日です！"
            }
            requests.post(webhook_url,main_content)
    for i in Aniversary.objects.all():
        anivage = i.didday
        print(anivage)
        if now.day == anivage.day: #今日が誕生日！！！！！！
            main_content = {
                "content": "今日は" + str(i.annivapp) + "です！"
            }
            requests.post(webhook_url,main_content)
User=get_user_model()
noticeuser = User.objects.get(pk=1)
ntctime = str(noticeuser.noticetime)
print(ntctime)
schedule.every().day.at(ntctime).do(job)
class index(TemplateView):
    template_name = "age/index.html"
class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
class GalleryView(LoginRequiredMixin, ListView):
    model = Furn
    template_name = "age/gallery.html"
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': HomeElecApp.objects.filter(user=self.request.user),
            'object_list3': Aniversary.objects.filter(user=self.request.user),
            'object_list4': Other.objects.filter(user=self.request.user),
            'object_list5': Clothes.objects.filter(user=self.request.user),
            'pictures': FurnImage.objects.all(),
            'pictures2': ElecImage.objects.all(),
            'pictures3': AnivImage.objects.all(),
            'pictures4': OtherImage.objects.all(),
            'pictures5': ClothImage.objects.all()
        })
        return context
    def get_queryset(self):
        return Furn.objects.filter(user=self.request.user)
class FurnListView(LoginRequiredMixin,ListView):
    model = Furn
    template_name = "age/list.html"
    def get_context_data(self, **kwargs):
        context = super(FurnListView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': HomeElecApp.objects.filter(user=self.request.user),
            'object_list3': Aniversary.objects.filter(user=self.request.user),
            'object_list4': Other.objects.filter(user=self.request.user),
            'object_list5': Clothes.objects.filter(user=self.request.user),

        })
        return context

    def get_queryset(self):
        return Furn.objects.filter(user=self.request.user)
@login_required
def furnhistory(request,num):
    print(Furn.objects.get(pk=num))
    if request.method == "POST":
        form = FurnHistoryForm(request.POST)
        if form.is_valid():
            historykey = FurnHistory.objects.count() + 1
            form.save()
            print(historykey)
            form2 = FurnHistory.objects.get(pk=historykey)
            form2.mdl=Furn.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = FurnHistoryForm()

    context = {'form':form}
    return render(request, 'age/historycreate.html', context)
@login_required
def furnimage(request,num):
    print(Furn.objects.get(pk=num))
    if request.method == "POST":
        form = FurnImageForm(request.POST, request.FILES)
        if form.is_valid():
            historykey = FurnImage.objects.count() + 1
            form.save()
            print(historykey)
            form2 = FurnImage.objects.get(pk=historykey)
            form2.mdl=Furn.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = FurnImageForm()

    context = {'form':form}
    return render(request, 'age/imagecreate.html', context)
class FurnHistoryupdView(LoginRequiredMixin,UpdateView):
    model = FurnHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1']
    def get_success_url(self):
        return reverse_lazy('age:list')
class FurnDetailView(LoginRequiredMixin,DetailView):
    model = Furn
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(FurnDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': FurnHistory.objects.filter(mdl__pk=self.object.pk),
            'object3': FurnImage.objects.filter(mdl__pk=self.object.pk),
            'type':'furn',
        })
        return context

    def get_queryset(self):
        return Furn.objects.all()
    success_url = reverse_lazy('age:list')

@login_required
def furncreate(request):
    if request.method == "POST":
        form = FurnForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form2 = Furn.objects.get(pk=Furn.objects.all().count())
            form2.user=request.user
            form2.save()
            return redirect('age:list')
    else:
        form = FurnForm()

    context = {'form':form}
    return render(request, 'age/furn_create.html', context)

class FurnDeleteView(LoginRequiredMixin,DeleteView):
    model = Furn
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')

@login_required
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
@login_required
def elechistory(request,num):
    print(HomeElecApp.objects.get(pk=num))
    if request.method == "POST":
        form = ElecHistoryForm(request.POST)
        if form.is_valid():
            historykey = ElecHistory.objects.count() + 1
            form.save()
            print(historykey)
            form2 = ElecHistory.objects.get(pk=historykey)
            form2.mdl=HomeElecApp.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = ElecHistoryForm()

    context = {'form':form}
    return render(request, 'age/historycreate.html', context)
@login_required
def elecimage(request,num):
    print(HomeElecApp.objects.get(pk=num))
    if request.method == "POST":
        form = ElecImageForm(request.POST, request.FILES)
        if form.is_valid():
            historykey = ElecImage.objects.count() + 1
            form.save()
            print(historykey)
            form2 = ElecImage.objects.get(pk=historykey)
            form2.mdl=HomeElecApp.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = ElecImageForm()

    context = {'form':form}
    return render(request, 'age/imagecreate.html', context)
class ElecHistoryupdView(LoginRequiredMixin,UpdateView):
    model = ElecHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1']
    def get_success_url(self):
        return reverse_lazy('age:list')
class HomeelecDetailView(LoginRequiredMixin,DetailView):
    model = HomeElecApp
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(HomeelecDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': ElecHistory.objects.filter(mdl__pk=self.object.pk),
            'object3': ElecImage.objects.filter(mdl__pk=self.object.pk),
            'type':'elec',
        })
        return context

    def get_queryset(self):
        return HomeElecApp.objects.all()
    success_url = reverse_lazy('age:list')



@login_required
def eleccreate(request):
    if request.method == "POST":
        form = ElecForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form2 = HomeElecApp.objects.get(pk=HomeElecApp.objects.all().count())
            form2.user=request.user
            form2.save()
            return redirect('age:list')
    else:
        form = ElecForm()

    context = {'form':form}
    return render(request, 'age/homeelec_create.html', context)

class HomeelecDeleteView(LoginRequiredMixin,DeleteView):
    model = HomeElecApp
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')

@login_required
def elecupdate(request,pk):
    if request.method == "POST":
        a = HomeElecApp.objects.get(pk=pk)
        form = ElecupdForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = ElecupdForm()
    context = {'form':form}
    return render(request, 'age/homeelec_update.html', context)
    #記念日


class AnnivDetailView(LoginRequiredMixin,DetailView):
    model = Aniversary
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(AnnivDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': AnivHistory.objects.filter(mdl__pk=self.object.pk),
            'object3': AnivImage.objects.filter(mdl__pk=self.object.pk),
            'type':'aniv',
        })
        return context

    def get_queryset(self):
        return Aniversary.objects.all()
    success_url = reverse_lazy('age:list')
@login_required
def anivhistory(request,num):
    print(Aniversary.objects.get(pk=num))
    if request.method == "POST":
        form = AnivHistoryForm(request.POST)
        if form.is_valid():
            historykey = AnivHistory.objects.count() + 1
            form.save()
            print(historykey)
            form2 = AnivHistory.objects.get(pk=historykey)
            form2.mdl=Aniversary.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = AnivHistoryForm()

    context = {'form':form}
    return render(request, 'age/historycreate.html', context)
@login_required
def anivimage(request,num):
    print(Aniversary.objects.get(pk=num))
    if request.method == "POST":
        form = AnivImageForm(request.POST, request.FILES)
        if form.is_valid():
            historykey = AnivImage.objects.count() + 1
            form.save()
            print(historykey)
            form2 = AnivImage.objects.get(pk=historykey)
            form2.mdl=aniversary.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = AnivImageForm()

    context = {'form':form}
    return render(request, 'age/imagecreate.html', context)
class AnivHistoryupdView(LoginRequiredMixin,UpdateView):
    model = AnivHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1']
    def get_success_url(self):
        return reverse_lazy('age:list')
@login_required
def anivcreate(request):
    if request.method == "POST":
        form = AnivForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form2 = Aniversary.objects.get(pk=Aniversary.objects.all().count())
            form2.user=request.user
            form2.save()
            return redirect('age:list')
    else:
        form = AnivForm()

    context = {'form':form}
    return render(request, 'age/anniv_create.html', context)

class AnnivDeleteView(LoginRequiredMixin,DeleteView):
    model = Aniversary
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')
@login_required
def anivupdate(request,pk):
    if request.method == "POST":
        form = AnivupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = AnivupdForm()

    context = {'form':form}
    return render(request, 'age/homeelec_update.html', context)
#ファッション
class ClothesDetailView(LoginRequiredMixin,DetailView):
    model = Clothes
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(ClothesDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': ClothHistory.objects.filter(mdl__pk=self.object.pk),
            'object3': ClothImage.objects.filter(mdl__pk=self.object.pk),
            'type':'fashion',
        })
        return context

    def get_queryset(self):
        return Clothes.objects.all()
    success_url = reverse_lazy('age:list')
@login_required
def clothhistory(request,num):
    print(Clothes.objects.get(pk=num))
    if request.method == "POST":
        form = ClothHistoryForm(request.POST)
        if form.is_valid():
            historykey = ClothHistory.objects.count() + 1
            form.save()
            print(historykey)
            form2 = ClothHistory.objects.get(pk=historykey)
            form2.mdl=Clothes.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = ClothHistoryForm()

    context = {'form':form}
    return render(request, 'age/historycreate.html', context)
@login_required
def clothimage(request,num):
    print(Clothes.objects.get(pk=num))
    if request.method == "POST":
        form = ClothImageForm(request.POST, request.FILES)
        if form.is_valid():
            historykey = ClothImage.objects.count() + 1
            form.save()
            print(historykey)
            form2 = ClothImage.objects.get(pk=historykey)
            form2.mdl=Clothes.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = ClothImageForm()

    context = {'form':form}
    return render(request, 'age/imagecreate.html', context)
class ClothHistoryupdView(LoginRequiredMixin,UpdateView):
    model = ClothHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1']
    def get_success_url(self):
        return reverse_lazy('age:list')
@login_required
def clothcreate(request):
    if request.method == "POST":
        form = ClothForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form2 = Clothes.objects.get(pk=Clothes.objects.all().count())
            form2.user=request.user
            form2.save()
            return redirect('age:list')
    else:
        form = ClothForm()

    context = {'form':form}
    return render(request, 'age/clothes_create.html', context)

class ClothesDeleteView(LoginRequiredMixin,DeleteView):
    model = Clothes
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')
@login_required
def clothupdate(request,pk):
    if request.method == "POST":
        form = ClothupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = ClothupdForm()

    context = {'form':form}
    return render(request, 'age/homeelec_update.html', context)
#他
class OtherDetailView(LoginRequiredMixin,DetailView):
    model = Other
    template_name = "age/homeelec_detail.html"
    def get_context_data(self, **kwargs):
        context = super(OtherDetailView, self).get_context_data(**kwargs)
        context.update({
            'object2': OtherHistory.objects.filter(mdl__pk=self.object.pk),
            'object3': OtherImage.objects.filter(mdl__pk=self.object.pk),
            'type':'other',
        })
        return context

    def get_queryset(self):
        return Other.objects.all()
    success_url = reverse_lazy('age:list')
@login_required
def otherhistory(request,num):
    print(Other.objects.get(pk=num))
    if request.method == "POST":
        form = OtherHistoryForm(request.POST)
        if form.is_valid():
            historykey = OtherHistory.objects.count() + 1
            form.save()
            print(historykey)
            form2 = OtherHistory.objects.get(pk=historykey)
            form2.mdl=Other.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = OtherHistoryForm()

    context = {'form':form}
    return render(request, 'age/historycreate.html', context)
@login_required
def otherimage(request,num):
    print(Other.objects.get(pk=num))
    if request.method == "POST":
        form = OtherImageForm(request.POST, request.FILES)
        if form.is_valid():
            historykey = OtherImage.objects.count() + 1
            form.save()
            print(historykey)
            form2 = OtherImage.objects.get(pk=historykey)
            form2.mdl=Other.objects.get(pk=num)
            form2.save()
            return redirect('age:list')
    else:
        form = OtherImageForm()

    context = {'form':form}
    return render(request, 'age/imagecreate.html', context)
class OtherHistoryupdView(LoginRequiredMixin,UpdateView):
    model = OtherHistory
    template_name = "age/historycreate.html"
    fields = ['history1','historyday1']
    def get_success_url(self):
        return reverse_lazy('age:list')
@login_required
def othercreate(request):
    if request.method == "POST":
        form = OtherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form2 = Other.objects.get(pk=Other.objects.all().count())
            form2.user=request.user
            form2.save()
            return redirect('age:list')
    else:
        form = OtherForm()

    context = {'form':form}
    return render(request, 'age/other_create.html', context)

class OtherDeleteView(LoginRequiredMixin,DeleteView):
    model = Other
    template_name = "age/homeelec_delete.html"
    success_url = reverse_lazy('age:list')
@login_required
def otherupdate(request,pk):
    if request.method == "POST":
        form = OtherupdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('age:list')
    else:
        form = OtherupdForm()

    context = {'form':form}
    return render(request, 'age/homeelec_update.html', context)
#新規登録
class SignUpView(LoginRequiredMixin,CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('age:complete')
    template_name = 'age/signup.html'

def SignupComplete(request):
    return HttpResponse('<p>あなた宛てに認証用のメールを送信しました</p>')



line_bot_api = LineBotApi(
    df["token"]
)

handler = WebhookHandler(df["handler"])

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

