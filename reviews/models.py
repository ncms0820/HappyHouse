from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    GUESTHOUSE = "guesthouse"
    HAIRSALON = "hairsalon"
    FACILITY = "facility"
    GENERAL = "general"
    PLACE_CHOICES = (
        (GUESTHOUSE, "guest house"),
        (HAIRSALON, "hairsalon"),
        (FACILITY, "facility"),
        (GENERAL, "general"),
    )

    title = models.CharField(max_length=80)
    review = models.TextField(max_length=255)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    place = models.CharField(max_length=20, choices=PLACE_CHOICES, default=GENERAL)

    def __str__(self):
        return self.title
