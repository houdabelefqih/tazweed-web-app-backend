from django.db import models
from graphql import GraphQLError
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

        elif not user.is_seller:
            raise Exception('You do not have permissions to add slots.')
        
        else:
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
        slot_uuid = graphene.UUID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user 

        if user.is_anonymous:
            raise Exception('Not logged in!')

        #get the logged in client
        client = Client.objects.get(user=user)

        #get the requested slot by uuid
        try:
            slot= Slot.objects.get(uuid=input.get('slot_uuid'))
        
        except Appointment.DoesNotExist:
            raise GraphQLError("This uuid does not exist.")
        
        if not slot.available:
            raise Exception('Slot is not available!')

        #get the seller object
        seller= slot.seller

        appointment= Appointment(slot=slot, seller=seller,client=client)

        appointment.save()

        #After creating the new appointment with default status pending, make corresponding slot unavailable
        slot.available= False
        slot.save()

        return AppointmentMutation(appointment=appointment)

class AppointmentUpdateMutation(graphene.relay.ClientIDMutation):
    appointment= graphene.Field(AppointmentNode)

    class Input:
        appointment_uuid = graphene.UUID()
        status = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user 

        if user.is_anonymous:
            raise Exception('Not logged in!')

        elif not user.is_seller:
            raise Exception("You do not have permissions to execute this action.")

        else:
            try:
                appointment= Appointment.objects.get(uuid=input.get('appointment_uuid'))
        
            except Appointment.DoesNotExist:
                raise GraphQLError("This uuid does not exist.")
            
            if appointment.client != user:
                raise Exception("You do not have permissions to execute this action.")

            appointment.status = input.get('status') 
            appointment.save()

            return AppointmentMutation(appointment=appointment)


class Mutation(graphene.AbstractType):
    create_slot= SlotMutation.Field()
    create_appointment = AppointmentMutation.Field()
    update_appointment = AppointmentUpdateMutation.Field()