from os import path
from flask import Blueprint
from flask import render_template
import requests

from app import douban_base_url

book_blueprint = Blueprint('book', __name__)


# example id: 1084336
@book_blueprint.route('/book/<string:id>')
def get_book_by_id(id):
    request_url = path.join(douban_base_url, 'book', id)
    r = requests.get(request_url)

    return render_template('book_details.html', book=r.json())


@book_blueprint.route('/book/isbn/<string:isbn>')
def get_book_by_isbn(isbn):
    request_url = path.join(douban_base_url, 'book/isbn', isbn)
    r = requests.get(request_url)

    return render_template('book_details.html', book=r.json())


# @book_blueprint.route('/book/search')
# def search_book():
#     request_url = path.join(douban_base_url, 'book/isbn')
#     request_url = path.join(request_url, isbn)
#     r = requests.get(request_url)
#
#     return render_template('book_details.html', book=r.json())