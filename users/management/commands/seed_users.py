import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from products.models import Product


class Command(BaseCommand):

    help = "This command will create users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many usersdo you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        products = Product.objects.all()
        seeder.add_entity(
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        created_users = seeder.execute()
        created_clean = flatten(list(created_users.values()))
        for pk in created_clean:
            user = User.objects.get(pk=pk)
            for i in products:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    user.cart.add(i)
        self.stdout.write(self.style.SUCCESS("Users created"))
