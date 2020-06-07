from graphql import GraphQLError
import graphene
from .models import Slot,Appointment
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class SlotFilter(django_filters.FilterSet):
    class Meta:
        model = Slot
        fields = {'date': ['exact'],}


class SlotNode(DjangoObjectType):

    class Meta:
        model = Slot
        interfaces = (graphene.relay.Node,)


class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = {'status': ['iexact'],}


class AppointmentNode(DjangoObjectType):
    class Meta:
        model = Appointment
        interfaces = (graphene.relay.Node,)



class Query(graphene.ObjectType):
    slot = graphene.relay.Node.Field(SlotNode)
    slots = DjangoFilterConnectionField(SlotNode, filterset_class=SlotFilter)

    appointment = graphene.relay.Node.Field(AppointmentNode)
    appointments = DjangoFilterConnectionField(AppointmentNode, filterset_class=AppointmentFilter)