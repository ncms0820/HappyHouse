import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User


class Command(BaseCommand):

    help = "This command will create users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many usersdo you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        seeder.add_entity(
            Review,
            number,
            {
                "value": lambda x: random.randint(0, 5),
                "user": lambda x: random.choice(users),
                "place": lambda x: random.choice(
                    ["guest house", "hairsalon", "facility", "general"]
                ),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created"))
