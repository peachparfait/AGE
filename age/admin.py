from django.contrib import admin
from .models import CustomUser,Furn,HomeElecApp,HomeElecAppCategory,Aniversary,Other,OtherCategory,Clothes,ClothCategory
from .models import ElecImage,FurnImage,AnnivImage,ClothImage,OtherImage

admin.site.register(ElecImage)
admin.site.register(FurnImage)
admin.site.register(AnnivImage)
admin.site.register(ClothImage)
admin.site.register(OtherImage)
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Furn)
admin.site.register(Clothes)
admin.site.register(ClothCategory)
admin.site.register(HomeElecApp)
admin.site.register(HomeElecAppCategory)
admin.site.register(Aniversary)
admin.site.register(Other)
admin.site.register(OtherCategory)