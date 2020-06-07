from django.db import models
import graphene
from apps.profiles.models import Client, Seller
from .models import Slot, Appointment
from .schema import SlotNode, AppointmentNode
from datetime import datetime

class SlotMutation(graphene.relay.ClientIDMutation):
    slot = graphene.Field(SlotNode)

    class Input:
        date = graphene.Date() #ISO 8601
        start = graphene.Time()
        end = graphene.Time()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user 

        if user.is_anonymous:
            raise Exception('Not logged in!')

        seller = Seller.objects.get(user=user)

        slot = Slot(
            date=input.get('date'),
            start=input.get('start'),
            end=input.get('end'),
            seller=seller,
            available=True,
        )

        slot.save()

        return SlotMutation(slot=slot)


class Mutation(graphene.AbstractType):
    create_slot= SlotMutation.Field()