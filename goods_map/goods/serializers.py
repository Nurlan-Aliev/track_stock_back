from rest_framework import serializers
from goods_map.goods.models import GoodsModel


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsModel
        fields = ['id',
                  'name',
                  # 'cost_price',
                  'wholesale_price',
                  'retail_price',
                  # 'weight',
                  'store_hall',
                  'store_back',
                  'store_up',
                  # 'stock'
                  ]
