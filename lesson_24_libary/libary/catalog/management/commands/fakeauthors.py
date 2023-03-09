from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from catalog.models import Author


class Command(BaseCommand):
    help = "Create 10 random author"

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        fake = Faker()
        count_authors = options.get("count") or 10
        seeder.add_entity(
            model=Author,
            number=count_authors,
            customFieldFormatters={
                "first_name": lambda x: fake.first_name(),
                "last_name": lambda x: fake.last_name(),
                "pseudonym": lambda x: fake.user_name(),
                "country": lambda x: fake.country(),
                "date_of_birth": lambda x: fake.date_of_birth(),
                "date_of_death": lambda x: fake.date_this_century(),
            },
        )
        inserted_pks = seeder.execute()
        return f"Creating of {count_authors} random authors is successful: \n {inserted_pks}"

    def add_arguments(self, parser):
        parser.add_argument("-c", "--count", type=int, help="Number of random authors")
