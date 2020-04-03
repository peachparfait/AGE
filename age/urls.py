from django.urls import path
from . import views
from .views import SignUpView,SignupComplete
from django.conf import settings
from django.conf.urls.static import static

app_name = 'age'

urlpatterns = [
    path('', views.index.as_view(),name="index"),
    #新規登録
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('complete',views.SignupComplete,name='complete'),
    #家具
    path('list/', views.FurnListView.as_view(),name="list"),
    path('furndetail/<int:pk>/', views.FurnDetailView.as_view(),name="furndetail"),
    path('furnhistory/<int:num>/', views.furnhistory,name="furnhistory"),
    path('furnhistoryupd/<int:pk>/', views.FurnHistoryupdView.as_view(),name="furnhistoryupd"),
    path('furncreate/',views.furncreate,name="furncreate"),
    path('furndelete/<int:pk>/', views.FurnDeleteView.as_view(),name="furndelete"),
    path('furnupdate/<int:pk>/', views.furnupdate,name="furnupdate"),
    #家電
    path('homeelecdetail/<int:pk>/', views.HomeelecDetailView.as_view(),name="homeelecdetail"),
    path('elechistory/<int:num>/', views.elechistory,name="elechistory"),
    path('elechistoryupd/<int:pk>/', views.ElecHistoryupdView.as_view(),name="elechistoryupd"),
    path('homeeleccreate/', views.eleccreate,name="homeeleccreate"),
    path('homeelecdelete/<int:pk>/', views.HomeelecDeleteView.as_view(),name="homeelecdelete"),
    path('homeelecupdate/<int:pk>/', views.elecupdate,name="homeelecupdate"),
    #記念日
    path('anivdetail/<int:pk>/', views.AnnivDetailView.as_view(),name="anivdetail"),
    path('anivhistory/<int:num>/', views.anivhistory,name="anivhistory"),
    path('anivhistoryupd/<int:pk>/', views.AnivHistoryupdView.as_view(),name="anivhistoryupd"),
    path('anivcreate/', views.anivcreate,name="anivcreate"),
    path('anivdelete/<int:pk>/', views.AnnivDeleteView.as_view(),name="anivdelete"),
    path('anivupdate/<int:pk>/', views.anivupdate,name="anivupdate"),
    #ファッション
    path('fashiondetail/<int:pk>/', views.ClothesDetailView.as_view(),name="fashiondetail"),
    path('fashionhistory/<int:num>/', views.clothhistory,name="fashionhistory"),
    path('fashionhistoryupd/<int:pk>/', views.ClothHistoryupdView.as_view(),name="fashionhistoryupd"),
    path('fashioncreate/', views.clothcreate,name="fashioncreate"),
    path('fashiondelete/<int:pk>/', views.ClothesDeleteView.as_view(),name="fashiondelete"),
    path('fashionupdate/<int:pk>/', views.clothupdate,name="fashionupdate"),
    #その他
    path('otherdetail/<int:pk>/', views.OtherDetailView.as_view(),name="otherdetail"),
    path('otherhistory/<int:num>/', views.otherhistory,name="otherhistory"),
    path('otherhistoryupd/<int:pk>/', views.OtherHistoryupdView.as_view(),name="otherhistoryupd"),
    path('othercreate/', views.othercreate,name="othercreate"),
    path('otherdelete/<int:pk>/', views.OtherDeleteView.as_view(),name="otherdelete"),
    path('otherupdate/<int:pk>/', views.otherupdate,name="otherupdate"),
    #ギャラリー
    path('gallery/', views.GalleryView.as_view(),name="gallery"),
    path('webhook/', views.webhook, name='webhook'),
]

