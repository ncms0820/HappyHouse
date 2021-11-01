import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from notices.models import Notice
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
        manager = []
        for m in users:
            if m.manager is True:
                manager.append(m)

        seeder.add_entity(Notice, number, {"writer": lambda x: random.choice(manager)})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} notices created"))
