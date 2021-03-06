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

    # RECIPE MODEL
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

    # RECIPE MODEL
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

    # RECIPE MODEL
    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, self, info, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return DeleteRecipe(recipe=recipe)


class CreateRecipeCategory(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    # CATEGORY MODEL
    category = graphene.Field(RecipeCategoryType)

    @classmethod
    def mutate(cls, self, info, name):
        category = Category(name=name)
        category.save()
        return CreateRecipeCategory(category=category)


class UpdateRecipeCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    # CATEGORY MODEL
    category = graphene.Field(RecipeCategoryType)

    @classmethod
    def mutate(cls, self, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateRecipeCategory(category=category)


class DeleteRecipeCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    # CATEGORY MODEL
    category = graphene.Field(RecipeCategoryType)

    @classmethod
    def mutate(cls, self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteRecipeCategory(category=category)


class CreateRecipeDifficulty(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    # DIFFICULTY MODEL
    difficulty = graphene.Field(RecipeDifficultyType)

    @classmethod
    def mutate(cls, self, info, name):
        difficulty = Difficulty(name=name)
        difficulty.save()
        return CreateRecipeDifficulty(difficulty=difficulty)


class UpdateRecipeDifficulty(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    # DIFFICULTY MODEL
    difficulty = graphene.Field(RecipeDifficultyType)

    @classmethod
    def mutate(cls, self, info, name, id):
        difficulty = Difficulty.objects.get(id=id)
        difficulty.name = name
        difficulty.save()
        return UpdateRecipeDifficulty(difficulty=difficulty)


class DeleteRecipeDifficulty(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    # DIFFICULTY MODEL
    difficulty = graphene.Field(RecipeDifficultyType)

    @classmethod
    def mutate(cls, self, info, id):
        difficulty = Difficulty.objects.get(id=id)
        difficulty.delete()
        return DeleteRecipeDifficulty(difficulty=difficulty)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()

    create_recipe_category = CreateRecipeCategory.Field()
    update_recipe_category = UpdateRecipeCategory.Field()
    delete_recipe_category = DeleteRecipeCategory.Field()

    create_recipe_difficulty = CreateRecipeDifficulty.Field()
    update_recipe_difficulty = UpdateRecipeDifficulty.Field()
    delete_recipe_difficulty = DeleteRecipeDifficulty.Field()
