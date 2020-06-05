from mongoengine import Document, EmbeddedDocument, CASCADE
from mongoengine.fields import (
    StringField,
    BinaryField,
    EmailField,
    ListField,
    IntField,
    BooleanField,
    ObjectIdField,
    ReferenceField,
    EmbeddedDocumentField,
     DateTimeField,

)

class Shop(Document):
    meta = {"collection": "shop"}
    name = StringField()
    address = StringField() 
    start_hour = IntField(min_value= 0, max_value=23)
    end_hour = IntField(min_value= 0, max_value=23)

    def __str__(self):
        return self.name

class Slot(EmbeddedDocument):
    meta = {"collection": "slot"}
    available = BooleanField(default=False)
    datetime = DateTimeField()
    duration = IntField(min_value= 1, max_value=4)

    def __str__(self):
        return self.datetime


class Appointment(EmbeddedDocument):
    meta = {"collection": "appointment"}
    seller_id = ObjectIdField()
    client_id = ObjectIdField()
    slot =  EmbeddedDocumentField(Slot)
    approved = BooleanField(default=False)

class User(Document):
    meta = {"collection": "user", 'allow_inheritance': True, 'abstract': True}
    name = StringField(max_length=200)
    username = StringField(max_length=100)
    password= StringField()
    phone = StringField()
    email = EmailField()

    def __str__(self):
        return self.name

class Seller(User):
    meta = {"collection": "seller",}
    shop = ReferenceField(Shop)
    available_slots =  ListField(EmbeddedDocumentField(Slot))
    appointments = ListField(EmbeddedDocumentField(Appointment))

class Client(User):
    meta = {"collection": "client"}
    reservations =  ListField(EmbeddedDocumentField(Appointment))


