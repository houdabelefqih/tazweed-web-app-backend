from graphql import GraphQLError
import graphene
import django_filters
from django_filters import OrderingFilter
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Slot, Appointment


class SlotFilter(django_filters.FilterSet):

    order_by = OrderingFilter(
            fields=[("date", "date"), ("start", "start"), ("end", "end")]
        )

    class Meta:
        model = Slot
        fields = {
            "uuid": ["exact"],
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
                "hour__gte",
            ],
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
                "hour__gte",
            ],
            "available": ["exact",],
        }

        


class AppointmentFilter(django_filters.FilterSet):

    order_by = OrderingFilter(
            fields=(
                ("slot__date", "slot__date"),
                ("slot__start", "slot__start"),
                ("slot__end", "slot__end"),
            )
        )

    class Meta:
        model = Appointment
        fields = {
            "uuid": ["exact"],
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
                "hour__gte",
            ],
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
                "hour__gte",
            ],
        }

       
