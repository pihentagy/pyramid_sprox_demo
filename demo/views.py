from pyramid.view import view_config

from sprox.formbase import AddRecordForm

from .models import (
    DBSession,
    Movie,
)

class NewMovieForm(AddRecordForm):
    __model__ = Movie

@view_config(
    route_name='movies.new',
    renderer='demo:templates/new_movies.html.mako',
)
def new_movies_view(request):
    new_movie_form = NewMovieForm(DBSession)
    return {
        'form': new_movie_form,
        'values': {},
    }
