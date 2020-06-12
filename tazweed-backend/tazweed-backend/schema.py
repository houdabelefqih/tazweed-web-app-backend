import graphene
import graphql_jwt
import apps.profiles.schema
import apps.appointments.schema
import apps.appointments.mutations
import apps.profiles.mutations



class Query(apps.profiles.schema.Query, apps.appointments.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    apps.appointments.mutations.Mutation,
    apps.profiles.mutations.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
