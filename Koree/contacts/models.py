from django.db import models

# from auth.models import User


class Contact:
    username = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
