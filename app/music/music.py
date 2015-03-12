from os import path
from flask import Blueprint
from flask import render_template

import requests

from app import douban_base_url


music_blueprint = Blueprint('music', __name__)


@music_blueprint.route('/music/<string:id>')
def get_music_by_id(id):
    request_url = path.join(douban_base_url, 'music', id)
    print request_url
    r = requests.get(request_url)

    return render_template('music_details.html', music=r.json())
