from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
)

class Seller(Document):
    meta = {"collection": "seller"}
    ID = ObjectIdField()
    name = StringField()

    def __str__(self):
        return self.name

# class Shop(models.Model):
#     name = models.CharField(max_length=100)
#     adress = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name



# class Slot(models.Model):
#     _id = models.ObjectIdField()
#     available = models.BooleanField(default = False)
#     seller = models.EmbeddedField(model_container=Seller)
#     date = models.DateField()
#     added = models.CharField(max_length=100)

#     def __str__(self):
#         return self.date.strftime('%Y-%m-%d')


