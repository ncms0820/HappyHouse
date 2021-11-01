from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )
    GUESTHOUSE = "guesthouse"
    HAIRSALON = "hairsalon"
    FACILITY = "facility"

    PLACE_CHOICES = (
        (GUESTHOUSE, "guest house"),
        (HAIRSALON, "hairsalon"),
        (FACILITY, "facility"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    place = models.CharField(max_length=12, choices=PLACE_CHOICES, default="null")
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.guest}: {self.place} - {self.check_in}"

    def is_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    is_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
