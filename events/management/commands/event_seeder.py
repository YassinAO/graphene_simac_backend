from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from events.models import Category, Event
import random
from django.utils import timezone
import datetime

CATEGORIES = [
    "Cooking",
    "Baking",
    "Mindfulness",
    "Wellness",
    "VR"
]

EVENTS = [
    "Cooking workshop",
    "Baking workshop",
    "Barbecue workshop",
    "Walk in the park",
    "Yoga exercises",
    "Gym workout",
    "Mindfulness",
    "Game night",
    "Storytelling",
    "Virtual reality dancing"
]


class Provider(faker.providers.BaseProvider):
    def event_category(self):
        return self.random_element(CATEGORIES)

    def event_title(self):
        return self.random_element(EVENTS)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["nl_NL"])
        fake.add_provider(Provider)

        for _ in range(10):
            event_category = fake.event_category()
            category, created = Category.objects.get_or_create(
                name=event_category)

            if created:
                category.save()
                print(f'{category} has been created')

        for _ in range(10):
            event_title = fake.event_title()
            event_description = fake.text(max_nb_chars=30)
            event_location = fake.city()
            event_duration = random.randint(60, 240)
            event_max_participants = random.randint(6, 20)
            event_date_hosted = datetime.datetime.now(tz=timezone.utc)
            category_id = random.randint(1, 5)
            host_id = random.randint(1, 100)

            event, created = Event.objects.get_or_create(title=event_title, description=event_description, location=event_location,
                                                         duration=event_duration, max_participants=event_max_participants, date_hosted=event_date_hosted, category_id=category_id, host_id=host_id)

            if created:
                event.save()
                print(f'{event} has been created')

        print('Seeding completed')
