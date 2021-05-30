import graphene
from graphene_django.types import DjangoObjectType
from .models import Recipe, Category, Difficulty, Event
from django.contrib.auth.models import User


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class RecipeDifficultyType(DjangoObjectType):
    class Meta:
        model = Difficulty
        fields = ('id', 'name',)


class RecipeChefType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username',)


class RecipeEventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ('title',)
