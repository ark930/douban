from os import path
from flask import Blueprint
from flask import render_template

import requests

from app import douban_base_url


celebrity_blueprint = Blueprint('celebriry', __name__)


@celebrity_blueprint.route('/celebrity/<string:id>')
def get_celebrity_works(id):
    request_url = path.join(douban_base_url, 'movie/celebrity', id)
    r = requests.get(request_url)

    return render_template('celebrity_details.html', celebrity=r.json())