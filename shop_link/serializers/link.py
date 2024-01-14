from rest_framework import serializers
from shop_link.models import Product
from shop_link.models import Link

from shop_link.validators import Status_Link_In_LinkValidator, Debt_In_LinkValidator


class LinkDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = '__all__'

    def get_products(self, obj):
        """Получаем список продуктов"""
        products = Product.objects.filter(link=obj)
        products_list = []
        products_dict = {}

        for product in products:
            products_dict["name"] = product.name
            products_dict["model"] = product.model
            products_dict["data"] = product.data
            products_list.append(products_dict)
        return products_list


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'
        validators = [Status_Link_In_LinkValidator(),
                      Debt_In_LinkValidator()
                      ]


class LinkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'
        validators = [Status_Link_In_LinkValidator(),
                      Debt_In_LinkValidator()
                      ]

    def validate(self, data):
        if 'debt' in data:  # проверяем, был ли изменен параметр "debt"
            raise serializers.ValidationError("Вы не можете изменять параметр debt ")
        return data
