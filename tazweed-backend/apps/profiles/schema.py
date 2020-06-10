from graphql import GraphQLError
import graphql_jwt
import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.appointments.schema import SlotNode, AppointmentNode
from apps.appointments.filters import SlotFilter, AppointmentFilter

from .models import User, Client, Seller
from .filters import UserFilter, ClientFilter, SellerFilter


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)



class SellerNode(DjangoObjectType):
    slots = DjangoFilterConnectionField(SlotNode, filterset_class=SlotFilter)
    appointments = DjangoFilterConnectionField(
        AppointmentNode, filterset_class=AppointmentFilter
    )

    class Meta:
        model = Seller
        interfaces = (graphene.relay.Node,)


class ClientNode(DjangoObjectType):
    reservations = DjangoFilterConnectionField(
        AppointmentNode, filterset_class=AppointmentFilter
    )

    class Meta:
        model = Client
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    seller = graphene.relay.Node.Field(SellerNode)
    sellers = DjangoFilterConnectionField(SellerNode, filterset_class=SellerFilter)

    client = graphene.relay.Node.Field(ClientNode)
    clients = DjangoFilterConnectionField(SellerNode, filterset_class=ClientFilter)

