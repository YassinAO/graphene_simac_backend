import graphene
from recipes.schema import Query as recipes_query
from recipes.schema import Mutation as recipes_mutation
from events.schema import Query as events_query
from events.schema import Mutation as events_mutation


class Query(recipes_query, events_query):
    pass


class Mutation(recipes_mutation, events_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
