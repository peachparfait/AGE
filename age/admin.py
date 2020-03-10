from django.contrib import admin
from .models import CustomUser,Furn,HomeElecApp,HomeElecAppCategory,Aniversary,Other,OtherCategory

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Furn)
admin.site.register(HomeElecApp)
admin.site.register(HomeElecAppCategory)
admin.site.register(Aniversary)
admin.site.register(Other)
admin.site.register(OtherCategory)