import json

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "world"


schema = graphene.Schema(query=Query)

result = schema.execute(
    """
    {
        hello 
    }
    """
)

result_dict = dict(result.data.items())
print(json.dumps(result_dict, indent=4))
