from contacts.views import (
    ContactsAPIView,
    ContactDetailsAPIView,
)
from django.urls import path

urlpatterns = [
    path("", ContactsAPIView.as_view(), name="contacts"),
    path("<int:id>", ContactDetailsAPIView.as_view(), name="contact"),
]
