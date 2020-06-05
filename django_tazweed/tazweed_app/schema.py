import graphene
from graphene.relay import Node, ClientIDMutation
from graphene_mongo.fields import MongoengineConnectionField
from graphql import GraphQLError
from .models import Seller,Slot,Appointment,Client,Shop
from .types import SellerType, ClientType, SlotType, ShopType, AppointmentType




class ClientMutation(ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    client = graphene.Field(ClientType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):

        id = input.get('id')

        try:
            client = Client.objects.get(_id=id)

        except Client.DoesNotExist:
            raise GraphQLError("This id does not exist.")

        client.name = input.get('name')
        client.save()

        return ClientMutation(client=client)



class Query(graphene.ObjectType):
    seller = Node.Field(SellerType)
    client = Node.Field(ClientType)
    shop = Node.Field(ShopType)
    appointment= Node.Field(AppointmentType)

    sellers = MongoengineConnectionField(SellerType)
    clients = MongoengineConnectionField(ClientType)
    shops = MongoengineConnectionField(ShopType)
    appointments=MongoengineConnectionField(AppointmentType)


class Mutation(graphene.ObjectType):
    update_client = ClientMutation.Field()

schema = graphene.Schema(query=Query, mutation= Mutation,types=[SellerType, ClientType, SlotType, ShopType, AppointmentType])
