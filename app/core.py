from datetime import datetime

from flask import (Blueprint, current_app, redirect,
                   render_template, request, url_for)


bp = Blueprint('core', __name__)


@bp.route('/')
def index():
    posts = current_app.db.posts.find(sort=[('pubdate', -1)])
    return render_template('index.html', posts=posts)


@bp.route('/post/<string:id>')
def post(id):
    post = current_app.db.posts.find_one({"_id": id})
    return render_template('post.html', post=post)


@bp.route('/tag/<string:tagname>')
def tag(tagname):
    posts = current_app.db.posts.find(sort=[('pubdate', -1),])
    tag_posts = list(filter(lambda p: tagname in p['tags'], posts))
    return render_template('index.html', posts=tag_posts)


@bp.route('/cat/<string:catname>')
def category(catname):
    posts = current_app.db.posts.find(
        {'category': catname}, sort=[('pubdate', -1)])
    return render_template('index.html', posts=posts)


def configure(app):
    app.register_blueprint(bp)
