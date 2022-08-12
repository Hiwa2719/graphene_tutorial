import json
from datetime import datetime

import graphene


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit=None):
        return [
                   User(id="1", username='fred', created_at=datetime.now()),
                   User(id="2", username='john', created_at=datetime.now()),
               ][:limit]


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()

    def mutate(self, info, username):
        user = User(id="3", username=username, created_at=datetime.now())
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

result = schema.execute(
    """
    mutation {
        createUser(username: "jeff") {
            user {
                id
                username
                createdAt
            }
        }
    }
    """
)

print(result)
result_dict = dict(result.data.items())
print(json.dumps(result_dict, indent=4))
