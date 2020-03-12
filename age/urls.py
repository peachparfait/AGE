from django.urls import path
from . import views
from .views import SignUpView,SignupComplete

app_name = 'age'

urlpatterns = [
    path('', views.index.as_view(),name="index"),
    #新規登録
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('complete',views.SignupComplete,name='complete'),
    #食べ物
    path('list/', views.FurnListView.as_view(),name="list"),
    path('furndetail/<int:pk>/', views.FurnDetailView.as_view(),name="furndetail"),
    path('furncreate/', views.FurnCreateView.as_view(),name="furncreate"),
    path('furndelete/<int:pk>/', views.FurnDeleteView.as_view(),name="furndelete"),
    path('furnupdate/<int:pk>/', views.FurnUpdateView.as_view(),name="furnupdate"),
    #家電
    path('homeelecdetail/<int:pk>/', views.HomeelecDetailView.as_view(),name="homeelecdetail"),
    path('homeeleccreate/', views.HomeelecCreateView.as_view(),name="homeeleccreate"),
    path('homeelecdelete/<int:pk>/', views.HomeelecDeleteView.as_view(),name="homeelecdelete"),
    path('homeelecupdate/<int:pk>/', views.HomeelecUpdateView.as_view(),name="homeelecupdate"),
    #記念日
    path('annivdetail/<int:pk>/', views.AnnivDetailView.as_view(),name="annivdetail"),
    path('annivcreate/', views.AnnivCreateView.as_view(),name="annivcreate"),
    path('annivdelete/<int:pk>/', views.AnnivDeleteView.as_view(),name="annivdelete"),
    path('annivupdate/<int:pk>/', views.AnnivUpdateView.as_view(),name="annivupdate"),
    #ファッション
    path('fashiondetail/<int:pk>/', views.ClothesDetailView.as_view(),name="clothesdetail"),
    path('fashioncreate/', views.ClothesCreateView.as_view(),name="clothescreate"),
    path('fashiondelete/<int:pk>/', views.ClothesDeleteView.as_view(),name="clothesdelete"),
    path('fashionupdate/<int:pk>/', views.ClothesUpdateView.as_view(),name="clothesupdate"),
    #その他
    path('otherdetail/<int:pk>/', views.OtherDetailView.as_view(),name="otherdetail"),
    path('othercreate/', views.OtherCreateView.as_view(),name="othercreate"),
    path('otherdelete/<int:pk>/', views.OtherDeleteView.as_view(),name="otherdelete"),
    path('otherupdate/<int:pk>/', views.OtherUpdateView.as_view(),name="otherupdate"),
    #ギャラリー
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.upload, name='upload'),
]

