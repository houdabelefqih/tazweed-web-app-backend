import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import User,Seller,Slot,Appointment,Client,Shop
from .types import SellerType, ClientType, UserType, SlotType, ShopType, AppointmentType


class Query(graphene.ObjectType):
    user = Node.Field(UserType)
    seller = Node.Field(SellerType)
    client = Node.Field(ClientType)
    shop = Node.Field(ShopType)

    users = MongoengineConnectionField(UserType)
    sellers = MongoengineConnectionField(SellerType)
    clients = MongoengineConnectionField(ClientType)
    shops = MongoengineConnectionField(ShopType)



schema = graphene.Schema(query=Query, types=[SellerType, ClientType, UserType, SlotType, ShopType, AppointmentType])
