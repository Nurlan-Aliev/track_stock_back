from django.db import models
from goods_map.stock.models import StoreHall, StoreBack, StoreUp


class GoodsModel(models.Model):
    name = models.CharField(max_length=50)
    # cost_price = models.PositiveSmallIntegerField(null=True)
    wholesale_price = models.PositiveSmallIntegerField(null=True)
    retail_price = models.PositiveSmallIntegerField(null=True)
    # weight = models.FloatField(null=True)
    store_hall = models.ForeignKey(StoreHall, on_delete=models.PROTECT,
                                   related_name='store_hall', null=True)
    store_back = models.ForeignKey(StoreBack, on_delete=models.PROTECT,
                                   related_name='store_back', null=True)
    store_up = models.ForeignKey(StoreUp, on_delete=models.PROTECT,
                                 related_name='store_up', null=True)
    # stock = models.ManyToManyField(StockModel)

    def __str__(self):
        return self.name
