from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(),name="index"),
    path('foodlist/', views.FoodListView.as_view(),name="foodlist"),
    path('fooddetail/', views.FoodDetailView.as_view(),name="foodetail"),
    path('foodcreate/', views.FoodCreateView.as_view(),name="foodcreate"),
    path('fooddelete/', views.FoodDeleteView.as_view(),name="fooddelete"),
    path('foodupdate/', views.FoodUpdateView.as_view(),name="foodupdate"),
]
