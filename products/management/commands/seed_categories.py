from django.core.management.base import BaseCommand
from products.models import Category


class Command(BaseCommand):

    help = "This command will create categories"

    def handle(self, *args, **options):
        categories = [
            "Make up",
            "Body care",
            "Hair care",
            "Nail care",
            "Fragrance",
            "Gels",
        ]

        for c in categories:
            Category.objects.create(name=c)
        self.stdout.write(self.style.SUCCESS("Categories created"))
