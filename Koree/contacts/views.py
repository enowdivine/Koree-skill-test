from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from contacts.serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
from contacts.models import Contact
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# function to handle both post and get request
class ContactsAPIView(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["id", "username", "gender", "address", "phoneNumber", "email"]
    search_fields = ["id", "username", "gender", "address", "phoneNumber", "email"]
    ordering_fields = ["id", "username", "gender", "address", "phoneNumber", "email"]

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(username=self.request.user)


# function to handle retrieve, update and delete request at once
class ContactDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(username=self.request.user)
