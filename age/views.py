from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Food
from django.urls import reverse_lazy

class index(TemplateView):
    template_name = "age/index.html"

class FoodListView(ListView):
    model = Food
    template_name = "age/foodlist.html"

class FoodDetailView(DetailView):
    model = Food
    template_name = "age/food_detail.html"

class FoodCreateView(CreateView):
    model = Food
    template_name = "age/food_create.html"
    fields = ['foodname','foodcategory']
    success_url = reverse_lazy('foodlist')

class FoodDeleteView(DeleteView):
    model = Food
    template_name = "age/food_delete.html"
    success_url = reverse_lazy('foodlist')

class FoodUpdateView(UpdateView):
    model = Food
    template_name = "age/food_update.html"
    fields = ['foodname','foodcategory']
    success_url = reverse_lazy('foodlist')
