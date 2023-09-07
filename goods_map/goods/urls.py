from django.urls import path
from goods_map.goods import views


urlpatterns = [
    path('', views.GoodsList.as_view(), name='good_list'),
    # path('create/', views.CreateGood.as_view(), name='create_good'),
    path('<int:pk>/update/', views.ProductUpdate.as_view(), name='update_good'),
    path('<int:pk>/delete/', views.ProductDestroy.as_view(), name='delete_good'),
    # path('<int:pk>/add_storage/', views.UpdateStorage.as_view(), name='add_storage'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='good_card'),
]
