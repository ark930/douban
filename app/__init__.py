from flask import Flask

douban_base_url = 'https://api.douban.com/v2'
app = Flask(__name__)

from book.views import book_blueprint
from movie.views import movie_blueprint
from movie.celebrity import celebrity_blueprint
from music.music import music_blueprint

app.register_blueprint(book_blueprint)
app.register_blueprint(movie_blueprint)
app.register_blueprint(celebrity_blueprint)
app.register_blueprint(music_blueprint)


@app.route('/')
def index():
    from flask import render_template
    return render_template('index.html')