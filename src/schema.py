import os
from functools import partial

import graphene

from graphql_to_rest import ExternalRESTObject

HOST = os.getenv('HOST', 'http://test')


class YourObject(graphene.ObjectType):
    endpoint = '{}/your-object'.format(HOST)

    id = graphene.Int()
    name = graphene.String(name='name')
    related_object = graphene.List(
        partial(lambda: YourObject)
    )


class Query(graphene.ObjectType):

    your_object = graphene.List(
        YourObject,
        id=graphene.Argument(graphene.ID)
    )

    def resolve_your_object(self, args, context, info):
        pass

schema = graphene.Schema(query=Query)
