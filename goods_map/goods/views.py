from goods_map.goods.models import GoodsModel
from goods_map.goods.serializers import GoodsSerializers
from rest_framework import generics


class GoodsList(generics.ListAPIView):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializers


class ProductDetail(generics.RetrieveAPIView):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializers


class ProductUpdate(generics.UpdateAPIView):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializers


class ProductDestroy(generics.DestroyAPIView):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializers
