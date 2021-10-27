from django.db import models
from core import models as core_models

# Shopping Model definition


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to="product_photos")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="photo"
    )

    def __str__(self):
        return self.caption

    def seller(self):
        return self.product.seller


class Category(core_models.TimeStampedModel):

    """category Model Definition"""

    category = models.CharField(max_length=20)
    product = models.ManyToManyField("Product", related_name="category")

    def __str__(self):
        return self.category


class Product(core_models.TimeStampedModel):

    """Product Model Definition"""

    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default="0")
    description = models.TextField(max_length=255, default="")
    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="product"
    )
    quantity = models.PositiveIntegerField(default="0")

    def __str__(self):
        return self.name
