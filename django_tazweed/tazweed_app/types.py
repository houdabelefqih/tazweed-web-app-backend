from graphene import relay
from graphene_mongo import MongoengineObjectType
from .models import Seller


class SellerType(MongoengineObjectType):
    class Meta:
        model = Seller
        interfaces = (relay.Node,)
