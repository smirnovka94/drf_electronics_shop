from django.urls import path
from shop_link.apps import ShopLinkConfig
from shop_link.views.link import LinkListAPIView, LinkDetailAPIView, LinkCreateAPIView, LinkDestroyAPIView, \
    LinkUpdateAPIView
from shop_link.views.product import ProductCreateAPIView, ProductListAPIView, ProductDetailAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView

app_name = ShopLinkConfig.name

urlpatterns = [
    path('link/create/', LinkCreateAPIView.as_view(), name='link_create'),
    path('link/', LinkListAPIView.as_view(), name='link_list'),
    path('link/<int:pk>/', LinkDetailAPIView.as_view(), name='link_get'),
    path('link/update/<int:pk>/', LinkUpdateAPIView.as_view(), name='link_update'),
    path('link/delete/<int:pk>/', LinkDestroyAPIView.as_view(), name='link_delete'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_get'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
]
