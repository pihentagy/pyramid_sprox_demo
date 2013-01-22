from pyramid.config import Configurator
from sqlalchemy import engine_from_config

import tw2.core
from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('movies_new', '/')
    config.scan()

    app = config.make_wsgi_app()
    app = tw2.core.make_middleware(
        app,
        {
            'toscawidgets.framework' : 'wsgi',
            'toscawidgets.middleware.inject_resources' : True,
        },
        stack_registry=True,
    )

    return app
