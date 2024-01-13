from rest_framework import generics
from shop_link.models import Contact
from shop_link.serializers.contact import ContactSerializer


class ContactListAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactSerializer


class ContactUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactDestroyAPIView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
