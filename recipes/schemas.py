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


class Query(graphene.ObjectType):

    # RECIPE MODEL
    all_recipes = graphene.List(RecipeType)
    recipe_by_id = graphene.Field(RecipeType, id=graphene.Int())
    recipe_by_category = graphene.List(RecipeType, category=graphene.Int())
    recipe_by_difficulty = graphene.List(RecipeType, difficulty=graphene.Int())
    recipe_by_chef = graphene.List(RecipeType, chef=graphene.Int())

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_recipe_by_id(self, info, id):
        return Recipe.objects.get(pk=id)

    def resolve_recipe_by_category(self, info, category):
        return Recipe.objects.filter(category=category)

    def resolve_recipe_by_difficulty(self, info, difficulty):
        return Recipe.objects.filter(difficulty=difficulty)

    def resolve_recipe_by_chef(self, info, chef):
        return Recipe.objects.filter(chef=chef)

    # CATEGORY MODEL
    all_recipe_categories = graphene.List(RecipeCategoryType)
    recipe_category_by_id = graphene.Field(
        RecipeCategoryType, id=graphene.Int())

    def resolve_all_recipe_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_recipe_category_by_id(self, info, id):
        return Category.objects.get(pk=id)

    # DIFFICULTY MODEL
    all_recipe_difficulties = graphene.List(RecipeDifficultyType)
    recipe_difficulty_by_id = graphene.Field(
        RecipeDifficultyType, id=graphene.Int())

    def resolve_all_recipe_difficulties(self, info, **kwargs):
        return Difficulty.objects.all()

    def resolve_recipe_difficulty_by_id(self, info, id):
        return Difficulty.objects.get(pk=id)
