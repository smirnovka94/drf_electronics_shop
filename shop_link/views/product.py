from rest_framework import generics
from shop_link.models import Product
from shop_link.serializers.product import ProductSerializer
from users.permissions import IsActiveUser


class ProductListAPIView(generics.ListAPIView):
    """Чтение списка продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductDetailAPIView(generics.RetrieveAPIView):
    """Чтение продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductCreateAPIView(generics.CreateAPIView):
    """Создание продукта"""
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Обновление продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Удаление продукта"""
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]
