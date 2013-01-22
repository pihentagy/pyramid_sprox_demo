from pyramid.response import Response
from pyramid.view import view_config

from sprox.formbase import AddRecordForm

from .models import (
    DBSession,
    Movie,
)

class NewMovieForm(AddRecordForm):
    __model__ = Movie

@view_config(
    route_name='movies_new',
    renderer='demo:templates/new_movies.pt',
)
def new_movies_view(request):
    new_movie_form = NewMovieForm(DBSession)
    return {
        'form': new_movie_form,
        'values': {},
    }
