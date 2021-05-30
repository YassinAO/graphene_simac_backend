from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, default='uncategorized')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    duration = models.IntegerField(default=60)
    max_participants = models.IntegerField(default=10)
    date_hosted = models.DateTimeField(auto_now_add=False, auto_now=False)
    date_posted = models.DateTimeField(default=timezone.now)
    cover_photo = models.FilePathField(path=None, match=None, max_length=100)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title
