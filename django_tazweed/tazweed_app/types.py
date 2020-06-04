from graphene import relay
from graphene_mongo import MongoengineObjectType
from .models import User,Seller,Slot,Appointment,Client,Shop

class SellerType(MongoengineObjectType):
    class Meta:
        model = Seller
        interfaces = (relay.Node,)

class ClientType(MongoengineObjectType):
    class Meta:
        model = Client
        interfaces = (relay.Node,)

class UserType(MongoengineObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)       

class SlotType(MongoengineObjectType):
    class Meta:
        model = Slot
        interfaces = (relay.Node,)

class ShopType(MongoengineObjectType):
    class Meta:
        model = Shop
        interfaces = (relay.Node,)

class AppointmentType(MongoengineObjectType):
    class Meta:
        model = Appointment
        interfaces = (relay.Node,)