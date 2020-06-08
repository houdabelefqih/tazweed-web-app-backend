from graphql import GraphQLError
import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Slot, Appointment

class SlotFilter(django_filters.FilterSet):
    class Meta:
        model = Slot
        fields = {
            "date": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
                "year",
                "year__lt",
                "year__lte",
                "year__gt",
                "year__gte",
                "month",
                "month__lt",
                "month__lte",
                "month__gt",
                "month__gte",
                "day",
                "day__lt",
                "day__lte",
                "day__gt",
                "day__gte",
            ],

            "start": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
                "hour",
                "hour__lt",
                "hour__lte",
                "hour__gt",
                "hour__gte",],
            
            "end": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
                "hour",
                "hour__lt",
                "hour__lte",
                "hour__gt",
                "hour__gte",],

            "available": ["exact",]
        }


class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = {
            "status": ["iexact"],
            "slot__date": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
                "year",
                "year__lt",
                "year__lte",
                "year__gt",
                "year__gte",
                "month",
                "month__lt",
                "month__lte",
                "month__gt",
                "month__gte",
                "day",
                "day__lt",
                "day__lte",
                "day__gt",
                "day__gte",
            ],

            "slot__start": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
                "hour",
                "hour__lt",
                "hour__lte",
                "hour__gt",
                "hour__gte",],

            "slot__end": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
                "hour",
                "hour__lt",
                "hour__lte",
                "hour__gt",
                "hour__gte",],
        }


