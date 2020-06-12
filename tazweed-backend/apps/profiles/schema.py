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
    user = graphene.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    def resolve_user(self,info, **kwargs):
        user = info.context.user 

        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user
            


    seller = graphene.relay.Node.Field(SellerNode)
    sellers = DjangoFilterConnectionField(SellerNode, filterset_class=SellerFilter)

    client = graphene.relay.Node.Field(ClientNode)
    clients = DjangoFilterConnectionField(SellerNode, filterset_class=ClientFilter)

