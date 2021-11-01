import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations.models import Reservation
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
            Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "place": lambda x: random.choice(
                    ["guest house", "hairsalon", "facility"]
                ),
                "guest": lambda x: random.choice(users),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created"))
