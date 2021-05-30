from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import faker.providers
import random
User = get_user_model()


class Provider(faker.providers.BaseProvider):
    pass


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["nl_NL"])
        fake.add_provider(Provider)

        user, created = User.objects.get_or_create(
            username="yassin", email="yassin@company.com", is_superuser=True, is_staff=True, is_active=True)
        if created:
            user.set_password("yassin")
            user.save()

        for _ in range(100):
            username = fake.unique.first_name().lower()
            email = fake.unique.ascii_company_email()
            user, created = User.objects.get_or_create(
                username=username, email=email, is_superuser=False, is_staff=False, is_active=True)
            if created:
                user.set_password(username)
                user.save()
                print(f'{user} has been created')

        print('Seeding completed')
