from django.contrib import admin
from .models import GuideRegisterModel, TouristRegisterModel

# Register your models here.

admin.site.register(GuideRegisterModel)
admin.site.register(TouristRegisterModel)