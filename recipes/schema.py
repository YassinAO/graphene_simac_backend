import graphene
from graphene_django.types import DjangoObjectType
from .models import Recipe, Category, Difficulty
from django.contrib.auth.models import User


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = '__all__'


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class DifficultyType(DjangoObjectType):
    class Meta:
        model = Difficulty
        fields = ('id', 'name',)


class ChefType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username',)


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
    all_categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.Int())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category_by_id(self, info, id):
        return Category.objects.get(pk=id)

    # DIFFICULTY MODEL
    all_difficulties = graphene.List(DifficultyType)
    difficulty_by_id = graphene.Field(DifficultyType, id=graphene.Int())

    def resolve_all_difficulties(self, info, **kwargs):
        return Difficulty.objects.all()

    def resolve_difficulty_by_id(self, info, id):
        return Difficulty.objects.get(pk=id)


class RecipeInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=True)
    total_servings = graphene.Int(required=True)
    preparation_time = graphene.Int(required=True)
    rating = graphene.Int(required=True)
    category_id = graphene.Int(name="category")
    difficulty_id = graphene.Int(name="difficulty")


class CreateRecipe(graphene.Mutation):

    class Arguments:
        recipeData = RecipeInput(required=True)

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, self, info, recipeData):
        recipe = Recipe(**recipeData, chef=info.context.user)
        recipe.save()
        return CreateRecipe(recipe=recipe)


class UpdateRecipe(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        recipeData = RecipeInput(required=True)

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, self, info, id, recipeData):
        recipe = Recipe.objects.get(id=id)
        for key, value in recipeData.items():
            setattr(recipe, key, value)
        recipe.save()
        return UpdateRecipe(recipe=recipe)


class DeleteRecipe(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, self, info, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return DeleteRecipe(recipe=recipe)


class CreateCategory(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    # CATEGORY MODEL
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, self, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    # CATEGORY MODEL
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, self, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    # CATEGORY MODEL
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteCategory(category=category)


class CreateDifficulty(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    # DIFFICULTY MODEL
    difficulty = graphene.Field(DifficultyType)

    @classmethod
    def mutate(cls, self, info, name):
        difficulty = Difficulty(name=name)
        difficulty.save()
        return CreateDifficulty(difficulty=difficulty)


class UpdateDifficulty(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    # DIFFICULTY MODEL
    difficulty = graphene.Field(DifficultyType)

    @classmethod
    def mutate(cls, self, info, name, id):
        difficulty = Difficulty.objects.get(id=id)
        difficulty.name = name
        difficulty.save()
        return UpdateDifficulty(difficulty=difficulty)


class DeleteDifficulty(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    # DIFFICULTY MODEL
    difficulty = graphene.Field(DifficultyType)

    @classmethod
    def mutate(cls, self, info, id):
        difficulty = Difficulty.objects.get(id=id)
        difficulty.delete()
        return DeleteDifficulty(difficulty=difficulty)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_difficulty = CreateDifficulty.Field()
    update_difficulty = UpdateDifficulty.Field()
    delete_difficulty = DeleteDifficulty.Field()
