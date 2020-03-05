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
    path('list/', views.FoodListView.as_view(),name="foodlist"),
    path('fooddetail/<int:pk>/', views.FoodDetailView.as_view(),name="fooddetail"),
    path('foodcreate/', views.FoodCreateView.as_view(),name="foodcreate"),
    path('fooddelete/<int:pk>/', views.FoodDeleteView.as_view(),name="fooddelete"),
    path('foodupdate/<int:pk>/', views.FoodUpdateView.as_view(),name="foodupdate"),
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
]

