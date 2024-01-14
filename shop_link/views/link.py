from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from shop_link.models import Link
from shop_link.serializers.link import LinkSerializer, LinkDetailSerializer
from users.permissions import IsActiveUser


class LinkListAPIView(generics.ListAPIView):
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [IsActiveUser]

class LinkDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]

class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsActiveUser]
    
class LinkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]

class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]
