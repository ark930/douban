from os import path
from flask import Blueprint
from flask import render_template

import requests

from app import douban_base_url


movie_blueprint = Blueprint('movie', __name__)


@movie_blueprint.route('/movie/subject/<string:id>')
def get_movie_subject(id):
    request_url = path.join(douban_base_url, 'movie/subject',  id)
    r = requests.get(request_url)

    return render_template('movie_details.html', movie=r.json())