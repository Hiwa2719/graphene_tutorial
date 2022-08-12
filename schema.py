import json

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

schema = graphene.Schema(query=Query)

result = schema.execute(
    """
    {
        isAdmin 
    }
    """
)

result_dict = dict(result.data.items())
print(json.dumps(result_dict, indent=4))
