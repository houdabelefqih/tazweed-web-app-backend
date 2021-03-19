from django.db import models
from graphql import GraphQLError
import graphene
from .models import User,Seller, Client
from .schema import UserNode, SellerNode, ClientNode
from datetime import datetime

class CreateUserMutation(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True) #ISO 8601
        email = graphene.String(required=True)
        phone=graphene.String(required=True)
        password = graphene.String(required=True)
        shop = graphene.String()
        isSeller = graphene.Boolean(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):

        isSeller = input.get('isSeller')

        user = User(
            username=input.get('username'),
            first_name= input.get('first_name'),
            last_name= input.get('last_name'),
            email=input.get('email'),
            phone=input.get('phone')
        )
        user.set_password(input.get('password'))
        user.save()

        #if new user is a seller, create a seller object otherwise create a client object

        if (isSeller):
            seller = Seller(user=user, shop=input.get('shop'))
            seller.save()
        
        else:
            client= Client(user=user)
            client.save()


        return CreateUserMutation(user=user)

class Mutation(graphene.AbstractType):
    create_user= CreateUserMutation.Field()
    # update_user = UserEditMutation.Field()