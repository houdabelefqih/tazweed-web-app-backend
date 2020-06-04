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
    ID = ObjectIdField()
    name = StringField()
    adress = StringField() 
    start_hour = IntField(min_value= 0, max_value=23)
    end_hour = IntField(min_value= 0, max_value=23)

    def __str__(self):
        return self.name

class Slot(EmbeddedDocument):
    meta = {"collection": "slot"}
    ID = ObjectIdField()
    reserved = BooleanField(default=False)
    datetime = DateTimeField()
    duration = IntField(min_value= 1, max_value=4)


class Appointment(EmbeddedDocument):
    meta = {"collection": "client"}
    slot =  EmbeddedDocumentField(Slot)
    shop = ReferenceField(Shop)
    

class User(Document):
    meta = {"collection": "user", 'allow_inheritance': True, 'abstract': True}
    ID = ObjectIdField()
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


