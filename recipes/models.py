from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from events.models import Event
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Difficulty'
        verbose_name_plural = 'Difficulties'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    total_servings = models.IntegerField(default=1)
    preparation_time = models.IntegerField(default=60)
    rating = models.IntegerField(default=5)
    date_posted = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    difficulty = models.ForeignKey(
        Difficulty, default=1, on_delete=models.DO_NOTHING)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, blank=True, through='Enrollment')

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = [['event', 'recipe']]
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

        # def __str__(self):
        #     return self.date_added
