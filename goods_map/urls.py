from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('stock/', include('goods_map.stock.urls')),
    # path('count/', include('goods_map.count.urls')),
    path('goods/', include('goods_map.goods.urls')),
    # path('image/', include('goods_map.gallery.urls')),
    # path('login/', views.Login.as_view(), name='login'),
    # path('logout/', views.Logout.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
