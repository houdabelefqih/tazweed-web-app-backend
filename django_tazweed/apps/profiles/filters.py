from graphql import GraphQLError
import graphql_jwt
import graphene
import django_filters
from django_filters import OrderingFilter

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User, Client, Seller


class UserFilter(django_filters.FilterSet):

    order_by = OrderingFilter(
        fields=(
            ("first_name", "first_name"),
            ("last_name", "last_name"),
            ("username", "username"),
        )
    )

    class Meta:
        model = User
        fields = {
            "first_name": ["iexact", "icontains", "istartswith"],
            "last_name": ["iexact", "icontains", "istartswith"],
            "is_seller": ["iexact"],
        }


class SellerFilter(django_filters.FilterSet):

    order_by = OrderingFilter(
        fields=(
            ("user__first_name", "user__first_name"),
            ("user__last_name", "user__last_name"),
            ("user__username", "user__username"),
            ("shop", "shop")
        )
    )
    class Meta:
        model = Seller
        fields = {
            "user__first_name": ["iexact", "icontains", "istartswith"],
            "user__last_name": ["iexact", "icontains", "istartswith"],
            "user__username": ["iexact", "icontains", "istartswith"],
            "user__email": ["iexact", "icontains", "istartswith"],
            "shop": ["exact", "icontains", "istartswith"],
        }


class ClientFilter(django_filters.FilterSet):

    order_by = OrderingFilter(
    fields=(
        ("user__first_name", "user__first_name"),
        ("user__last_name", "user__last_name"),
        ("user__username", "user__username"),
    )
    )

    class Meta:
        model = Client
        fields = {
            "user__first_name": ["iexact", "icontains", "istartswith"],
            "user__last_name": ["iexact", "icontains", "istartswith"],
            "user__username": ["iexact", "icontains", "istartswith"],
            "user__email": ["iexact", "icontains", "istartswith"],
        }
