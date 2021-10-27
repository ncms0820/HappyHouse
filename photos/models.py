from django.db import models

# This is the model for the photos for the main page.


class Photo(models.Model):

    """Photo Model Definition for main page"""

    caption = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="main_photos")
