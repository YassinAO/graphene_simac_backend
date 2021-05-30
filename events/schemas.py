import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Category
from django.contrib.auth.models import User


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = '__all__'


class EventCategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class EventHostType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username',)
