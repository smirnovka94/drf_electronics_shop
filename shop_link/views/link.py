from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from shop_link.models import Link
from shop_link.serializers.link import LinkSerializer, LinkDetailSerializer, LinkUpdateSerializer
from users.permissions import IsActiveUser


class LinkListAPIView(generics.ListAPIView):
    """Чтение списка продуктов"""
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [IsActiveUser]


class LinkDetailAPIView(generics.RetrieveAPIView):
    """Чтение звена торговой сети"""
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]


class LinkCreateAPIView(generics.CreateAPIView):
    """Создание звена торговой сети"""
    serializer_class = LinkSerializer
    permission_classes = [IsActiveUser]


class LinkUpdateAPIView(generics.UpdateAPIView):
    """Обновление звена торговой сети"""
    serializer_class = LinkUpdateSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]


class LinkDestroyAPIView(generics.DestroyAPIView):
    """Удаление звена торговой сети"""
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]
