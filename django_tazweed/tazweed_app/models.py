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
    _id = ObjectIdField()
    meta = {"collection": "shop"}
    name = StringField()
    address = StringField() 
    start_hour = IntField(min_value= 0, max_value=23)
    end_hour = IntField(min_value= 0, max_value=23)

    def __str__(self):
        return self.name

class Slot(EmbeddedDocument):
    meta = {"collection": "slot"}
    available = BooleanField(default=True)
    datetime = DateTimeField()
    duration = IntField(min_value= 1, max_value=4)

    def __str__(self):
        return self.datetime


class Appointment(Document):
    _id = ObjectIdField()
    STATUS_CHOICES= (('approved', 'approved'), ('denied', 'denied'),('pending', 'pending'),)
    meta = {"collection": "appointment"}
    slot= EmbeddedDocumentField(Slot)
    client= ReferenceField('Client')
    seller= ReferenceField('Seller')
    status = StringField(choices =STATUS_CHOICES,default='pending')

class User(Document):
    _id = ObjectIdField()
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
    appointments = ListField(ReferenceField(Appointment), reverse_delete_rule=CASCADE)

class Client(User):
    meta = {"collection": "client"}
    reservations = ListField(ReferenceField(Appointment), reverse_delete_rule=CASCADE)


