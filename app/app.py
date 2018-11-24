# python modules
import os

# flask imports
from flask import Flask

# flask extensions
from flask_simplelogin import SimpleLogin
from flaskext.markdown import Markdown
# my modules
from . import (db, admin, core, context_processors, filters)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.configure(app)
    SimpleLogin(app)
    Markdown(app)

    filters.configure(app)
    context_processors.configure(app)

    admin.configure(app)
    core.configure(app)

    return app
