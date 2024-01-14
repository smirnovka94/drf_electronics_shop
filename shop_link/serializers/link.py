from rest_framework import serializers
from shop_link.models import Contact, Product
from shop_link.models import Link
from shop_link.serializers.contact import ContactSerializer
from shop_link.serializers.product import ProductSerializer
from shop_link.validators import Status_Link_In_LinkValidator


class LinkDetailSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = '__all__'

    def get_contacts(self, obj):
        """Получаем список контактов"""
        contacts = Contact.objects.filter(link=obj)
        return ContactSerializer(contacts, many=True).data

    def get_products(self, obj):
        """Получаем список продуктов"""
        products = Product.objects.filter(link=obj)
        return ProductSerializer(products, many=True).data


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'
        validators = [Status_Link_In_LinkValidator()]