from django.db import models
import graphene
from apps.profiles.models import Client, Seller
from .models import Slot, Appointment
from .schema import SlotNode, AppointmentNode
from datetime import datetime

class SlotMutation(graphene.relay.ClientIDMutation):
    slot = graphene.Field(SlotNode)

    class Input:
        date = graphene.Date(required=True) #ISO 8601
        start = graphene.Time(required=True)
        end = graphene.Time(required=True)

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


class AppointmentMutation(graphene.relay.ClientIDMutation):
    appointment= graphene.Field(AppointmentNode)

    class Input:
        slot_id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user 

        if user.is_anonymous:
            raise Exception('Not logged in!')

        #get the logged in client
        client = Client.objects.get(user=user)

        #get the requested slot from its id
        slot= Slot.objects.get(pk=input.get('slot_id'))

        #get the seller object
        seller= slot.seller

        appointment= Appointment(slot=slot, seller=seller,client=client)

        appointment.save()

        #After creating the new appointment with default status pending, make corresponding slot unavailable
        slot.available= False
        slot.save()

        return SlotMutation(appointment=appointment)

# class AppointmentUpdateMutation(graphene.relay.ClientIDMutation):
#     pass


class Mutation(graphene.AbstractType):
    create_slot= SlotMutation.Field()
    create_appointment = AppointmentMutation.Field()
    #update_appointment = AppointmentUpdateMutation.Field()