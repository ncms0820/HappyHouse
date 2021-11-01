import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from products import models as product_models


class Command(BaseCommand):

    help = "This command will create users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many usersdo you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_categories = product_models.Category.objects.all()
        all_sellers = User.objects.all()
        managers = []
        for s in all_sellers:
            if s.manager is True:
                managers.append(s)
        seeder.add_entity(
            product_models.Product,
            number,
            {
                "seller": lambda x: random.choice(managers),
                "category": lambda x: random.choice(all_categories),
                "price": lambda x: random.randint(0, 100),
                "quantity": lambda x: random.randint(0, 100),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            product = product_models.Product.objects.get(pk=pk)
            for i in range(3, random.randint(5, 8)):
                product_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    photo=f"product_photos/{random.randint(1, 31)}.webp",
                    product=product,
                )
        self.stdout.write(self.style.SUCCESS(f"{number}Users created"))
