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


class Query(graphene.ObjectType):

    all_events = graphene.List(EventType)
    event_by_id = graphene.Field(EventType, id=graphene.Int())
    event_by_category = graphene.List(EventType, category=graphene.Int())
    event_by_host = graphene.List(EventType, host=graphene.Int())

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_event_by_id(self, info, id):
        return Event.objects.get(pk=id)

    def resolve_event_by_category(self, info, category):
        return Event.object.filter(category=category)

    def resolve_event_by_host(self, info, host):
        return Event.objects.filter(host=host)
