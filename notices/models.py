from django.db import models
from core import models as core_models

# Create your models here.


class Notice(core_models.TimeStampedModel):

    """Notice Model Definition"""

    title = models.CharField(max_length=255)
    text = models.TextField(max_length=600)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(core_models.TimeStampedModel):

    """Comments Model Definition"""

    text = models.TextField(max_length=600)
    notice = models.ForeignKey("Notice", on_delete=models.CASCADE)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.created
