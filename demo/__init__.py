from pyramid.config import Configurator
from sqlalchemy import engine_from_config

import tw.api

from .models import DBSession

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)

    config.add_route('movies.new', 'movies/new')
    config.scan('.views')

    app = config.make_wsgi_app()
    app = tw.api.make_middleware(
        app,
        {
            'toscawidgets.framework' : 'wsgi',
            'toscawidgets.middleware.inject_resources' : True,
        },
        stack_registry=True,
    )

    return app
