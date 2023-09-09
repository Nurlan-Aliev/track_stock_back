from django.contrib import admin
from .models import StoreHall, StoreBack, StoreUp


@admin.register(StoreHall)
class GoodsAdmin(admin.ModelAdmin):
    pass


@admin.register(StoreBack)
class GoodsAdmin(admin.ModelAdmin):
    pass


@admin.register(StoreUp)
class GoodsAdmin(admin.ModelAdmin):
    pass
