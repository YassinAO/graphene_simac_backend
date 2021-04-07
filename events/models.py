from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

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
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title
