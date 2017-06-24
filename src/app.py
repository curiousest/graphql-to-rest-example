from flask import Flask
from flask_graphql import GraphQLView

from schema import schema


def create_app(path='/graphql', **kwargs):
    app = Flask(__name__)

    # !!!!!!!!!!!!!! Turn this off in production
    app.debug = True
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=schema, **kwargs))
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()
