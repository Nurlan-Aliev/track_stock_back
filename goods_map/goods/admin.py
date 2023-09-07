from django.contrib import admin
from .models import GoodsModel


@admin.register(GoodsModel)
class GoodsAdmin(admin.ModelAdmin):
    pass
