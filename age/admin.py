from django.contrib import admin
from .models import User,Food,FoodCategory,HomeElecApp,HomeElecAppCategory,Aniversary

# Register your models here.
admin.site.register(User)
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(HomeElecApp)
admin.site.register(HomeElecAppCategory)
admin.site.register(Aniversary)