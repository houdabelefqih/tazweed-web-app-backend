from graphql import GraphQLError
import graphql_jwt
from .models import User,Client,Seller
import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from apps.appointments.schema import SlotNode, AppointmentNode, SlotFilter, AppointmentFilter


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {'first_name': ['exact', 'icontains', 'istartswith'],
                  'last_name': ['exact', 'icontains', 'istartswith'],}

class UserNode(DjangoObjectType):

    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class SellerFilter(django_filters.FilterSet):
    class Meta:
        model = Seller
        fields = {'shop': ['exact', 'icontains', 'istartswith'],}


class SellerNode(DjangoObjectType):
    slots = DjangoFilterConnectionField(SlotNode, filterset_class=SlotFilter)
    appointments = DjangoFilterConnectionField(AppointmentNode, filterset_class=AppointmentFilter)

    class Meta:
        model = Seller
        interfaces = (graphene.relay.Node,)


class ClientNode(DjangoObjectType):
    reservations = DjangoFilterConnectionField(AppointmentNode, filterset_class=AppointmentFilter)

    class Meta:
        model = Client
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    seller = graphene.relay.Node.Field(SellerNode)
    sellers = DjangoFilterConnectionField(SellerNode, filterset_class=SellerFilter)

    client = graphene.relay.Node.Field(ClientNode)
    clients = graphene.List(ClientNode)

    def resolve_clients(self, info):
        return Client.objects.all()

    