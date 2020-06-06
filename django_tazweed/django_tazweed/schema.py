import graphene
import apps.profiles.schema


class Query(apps.profiles.schema.Query, graphene.ObjectType):
    pass


# class Mutation(expenses.schema.Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)