from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from recipes.models import Category, Difficulty, Recipe, Enrollment
import random

CATEGORIES = [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Simac"
]

DIFFICULTIES = [
    "Easy",
    "Medium",
    "Hard"
]

RECIPES = [
    "Creamy White Chili",
    "Banana Bread",
    "Cheeseburger Soup",
    "Amish Breakfast Casserole",
    "Pumpkin Spice Cupcakes",
    "Chicken Potpie",
    "Chicken Fajitas",
    "Apple Pie",
    "Enchilada Casser-Ole",
    "Cauliflower Soup"
]


class Provider(faker.providers.BaseProvider):
    def recipe_category(self):
        return self.random_element(CATEGORIES)

    def recipe_difficulty(self):
        return self.random_element(DIFFICULTIES)

    def recipe_title(self):
        return self.random_element(RECIPES)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["nl_NL"])
        fake.add_provider(Provider)

        for _ in range(10):
            recipe_category = fake.recipe_category()
            category, created = Category.objects.get_or_create(
                name=recipe_category)

            if created:
                category.save()
                print(f'{category} has been created')

        for _ in range(10):
            recipe_difficulty = fake.recipe_difficulty()
            difficulty, created = Difficulty.objects.get_or_create(
                name=recipe_difficulty)

            if created:
                difficulty.save()
                print(f'{difficulty} has been created')

        for _ in range(10):
            recipe_title = fake.recipe_title()
            recipe_description = fake.text(max_nb_chars=30)
            recipe_total_servings = random.randint(1, 6)
            recipe_preparation_time = random.randint(60, 240)
            recipe_rating = random.randint(1, 5)
            category_id = random.randint(1, 4)
            difficulty_id = random.randint(1, 3)
            chef_id = random.randint(1, 100)

            recipe, created = Recipe.objects.get_or_create(title=recipe_title, description=recipe_description, total_servings=recipe_total_servings,
                                                           preparation_time=recipe_preparation_time, rating=recipe_rating, category_id=category_id, difficulty_id=difficulty_id, chef_id=chef_id)

            if created:
                recipe.save()
                print(f'{recipe} has been created')

        print('Seeding completed')
