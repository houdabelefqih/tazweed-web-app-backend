from graphql import GraphQLError
import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Slot, Appointment
from .filters import SlotFilter, AppointmentFilter



class SlotNode(DjangoObjectType):
    class Meta:
        model = Slot
        interfaces = (graphene.relay.Node,)


class AppointmentNode(DjangoObjectType):
    class Meta:
        model = Appointment
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    slot = graphene.relay.Node.Field(SlotNode)
    slots = DjangoFilterConnectionField(SlotNode, filterset_class=SlotFilter)

    appointment = graphene.relay.Node.Field(AppointmentNode)
    appointments = DjangoFilterConnectionField(
        AppointmentNode, filterset_class=AppointmentFilter
    )

