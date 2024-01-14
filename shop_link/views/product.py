from rest_framework import generics
from shop_link.models import Product
from shop_link.serializers.product import ProductSerializer
from users.permissions import IsActiveUser


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]

class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]

class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]
