import datetime
import transaction

from pyramid.view import view_config

from sprox.formbase import AddRecordForm

from .models import (
    DBSession,
    Movie,
    Genre,
    Director,
)


class NewMovieForm(AddRecordForm):
    __model__ = Movie
    __dropdown_field_names__ = {'directors':'title'}


@view_config(
    route_name='movies_new',
    renderer='demo:templates/new_movies.pt',
)
def new_movies_view(request):
    new_movie_form = NewMovieForm(DBSession)
    values = dict(request.POST)
    if request.method == 'POST''':
        try:
            new_movie_form.validate(params=request.POST)
            request.session.flash('validated')
            del values['sprox_id']
            values['genre'] = DBSession.query(Genre).get(values['genre'])
            values['directors'] = DBSession.query(Director).filter(
                Director.id.in_(request.POST.getall('directors'))).all()
            values['release_date'] = datetime.datetime.strptime(
                values['release_date'], '%Y-%m-%d')
            movie = Movie(**values)
            request.session.flash('about to insert')
            with transaction.manager:
                DBSession.add(movie)
                request.session.flash("Movie " + movie.title + " inserted")
        except Exception as e:
            request.session.flash("Something bad has happened ", str(e))
    return {
        'form': new_movie_form,
        'values': {},
    }
