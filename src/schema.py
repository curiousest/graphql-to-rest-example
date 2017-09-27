import os
from functools import partial

import graphene

from graphql_to_rest import ExternalRESTField

HOST = os.getenv('HOST', 'http://test')


class YourObject(graphene.ObjectType):
    base_url = '{}/your-objects'.format(HOST)

    id = graphene.ID()
    name = graphene.String(name='name')

    # Data you want to use from the REST endpoint must be declared in this class,
    # otherwise it is discarded.
    # We need the related object ids in order to resolve the related objects (via another REST call).
    related_object_ids = graphene.List(graphene.Int)
    # a list of YourObject
    related_objects = graphene.List(
        # This is how you use other ObjectType classes before they're declared.
        # See: https://github.com/curiousest/graphql-to-rest/blob/90be702969d8fcbcfc96234e5684ca9e0e5163ae/graphql_to_rest/types.py#L35
        partial(lambda: YourObject)
    )


class Query(graphene.ObjectType):

    your_objects = ExternalRESTField(
        YourObject,
        id=graphene.Argument(graphene.ID),
        is_top_level=True,
        many=True
    )

schema = graphene.Schema(query=Query)
