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


class EventInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=True)
    location = graphene.String(required=True)
    duration = graphene.Int(required=True)
    max_participants = graphene.Int(required=True)
    date_hosted = graphene.String(required=False)
    cover_photo = graphene.String(required=True)
    category_id = graphene.Int(name="category")


class CreateEvent(graphene.Mutation):

    class Arguments:
        eventData = EventInput(required=True)

    # EVENT MODEL
    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, self, info, eventData):
        event = Event(**eventData, host=info.context.user)
        event.save()
        return CreateEvent(event=event)


class UpdateEvent(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        eventData = EventInput(required=True)

    # EVENT MODEL
    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, self, info, id, eventData):
        event = Event.objects.get(id=id)
        for key, value in eventData.items():
            setattr(event, key, value)
        event.save()
        return UpdateEvent(event=event)


class DeleteEvent(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    # EVENT MODEL
    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, self, info, id):
        event = Event.objects.get(id=id)
        event.delete()
        return DeleteEvent(event=event)


class CreateEventCategory(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    # CATEGORY MODEL
    category = graphene.Field(EventCategoryType)

    @classmethod
    def mutate(cls, self, info, name):
        category = Category(name=name)
        category.save()
        return CreateEventCategory(category=category)


class UpdateEventCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    # CATEGORY MODEL
    category = graphene.Field(EventCategoryType)

    @classmethod
    def mutate(cls, self, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateEventCategory(category=category)


class DeleteEventCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    # CATEGORY MODEL
    category = graphene.Field(EventCategoryType)

    @classmethod
    def mutate(cls, self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteEventCategory(category=category)


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()

    create_event_category = CreateEventCategory.Field()
    update_event_category = UpdateEventCategory.Field()
    delete_event_category = DeleteEventCategory.Field()
