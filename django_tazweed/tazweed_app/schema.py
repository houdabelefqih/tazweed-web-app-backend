import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import Seller
from .types import SellerType


class Query(graphene.ObjectType):
    node = Node.Field()
    sellers = MongoengineConnectionField(SellerType)


schema = graphene.Schema(query=Query, types=[SellerType])
