import graphene
from recipes.schema import Query as recipes_query
from recipes.schema import Mutation as recipes_mutation
from events.schema import Query as events_query


class Query(recipes_query, events_query):
    pass


class Mutation(recipes_mutation):
    pass


schema = graphene.Schema(query=Query)
