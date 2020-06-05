import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import Seller,Slot,Appointment,Client,Shop
from .types import SellerType, ClientType, SlotType, ShopType, AppointmentType


class Query(graphene.ObjectType):
    seller = Node.Field(SellerType)
    client = Node.Field(ClientType)
    shop = Node.Field(ShopType)

    sellers = MongoengineConnectionField(SellerType)
    clients = MongoengineConnectionField(ClientType)
    shops = MongoengineConnectionField(ShopType)



schema = graphene.Schema(query=Query, types=[SellerType, ClientType, SlotType, ShopType, AppointmentType])
