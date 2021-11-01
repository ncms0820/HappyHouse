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

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categories"


class Product(core_models.TimeStampedModel):

    """Product Model Definition"""

    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default="0")
    description = models.TextField(max_length=255, default="")
    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="product"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="product"
    )
    quantity = models.PositiveIntegerField(default="0")

    def __str__(self):
        return self.name
