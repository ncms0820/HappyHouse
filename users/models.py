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

    APPARTMENT_A1 = "a1"
    APPARTMENT_A2 = "a2"
    APPARTMENT_A3 = "a3"
    APPARTMENT_B1 = "b1"
    APPARTMENT_B2 = "b2"
    APPARTMENT_B3 = "b3"
    APPARTMENT_C2 = "c2"
    APPARTMENT_C3 = "c3"
    APPARTMENT_C4 = "c4"
    APPARTMENT_C5 = "c5"

    APPARTMENT_CHOICES = (
        (APPARTMENT_A1, "A1"),
        (APPARTMENT_A2, "A2"),
        (APPARTMENT_A3, "A3"),
        (APPARTMENT_B1, "B1"),
        (APPARTMENT_B2, "B2"),
        (APPARTMENT_B3, "B3"),
        (APPARTMENT_C2, "C2"),
        (APPARTMENT_C3, "C3"),
        (APPARTMENT_C4, "C4"),
        (APPARTMENT_C5, "rooftop house"),
    )

    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    manager = models.BooleanField(default=False)
    cart = models.ManyToManyField("products.Product", blank=True)
    appartment = models.CharField(
        choices=APPARTMENT_CHOICES, max_length=40, blank=True, null=True
    )
