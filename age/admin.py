from django.contrib import admin
from .models import CustomUser,Food,FoodCategory,HomeElecApp,HomeElecAppCategory,Aniversary,Other,OtherCategory

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(HomeElecApp)
admin.site.register(HomeElecAppCategory)
admin.site.register(Aniversary)
admin.site.register(Other)
admin.site.register(OtherCategory)