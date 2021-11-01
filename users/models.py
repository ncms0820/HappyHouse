from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    APARTMENT_A1 = "a1"
    APARTMENT_A2 = "a2"
    APARTMENT_A3 = "a3"
    APARTMENT_B1 = "b1"
    APARTMENT_B2 = "b2"
    APARTMENT_B3 = "b3"
    APARTMENT_C2 = "c2"
    APARTMENT_C3 = "c3"
    APARTMENT_C4 = "c4"
    APARTMENT_C5 = "c5"
    GUEST = "guest"

    APARTMENT_CHOICES = (
        (GUEST, "guest"),
        (APARTMENT_A1, "A1"),
        (APARTMENT_A2, "A2"),
        (APARTMENT_A3, "A3"),
        (APARTMENT_B1, "B1"),
        (APARTMENT_B2, "B2"),
        (APARTMENT_B3, "B3"),
        (APARTMENT_C2, "C2"),
        (APARTMENT_C3, "C3"),
        (APARTMENT_C4, "C4"),
        (APARTMENT_C5, "rooftop house"),
    )

    avatar = models.ImageField(upload_to="avatar", blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    manager = models.BooleanField(default=False)
    cart = models.ManyToManyField("products.Product", blank=True)
    apartment = models.CharField(choices=APARTMENT_CHOICES, max_length=40)
