from rest_framework import generics
from shop_link.models import Link
from shop_link.serializers.link import LinkSerializer, LinkDetailSerializer


class LinkListAPIView(generics.ListAPIView):
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()


class LinkDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()
    

class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer
    
    
class LinkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    

class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
    