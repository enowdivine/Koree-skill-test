from rest_framework.serializers import ModelSerializer
from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id",
            "username",
            "gender",
            "address",
            "phoneNumber",
            "email",
            "image",
        )
