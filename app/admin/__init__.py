import os

from flask_admin import Admin

from .postadmin import PostModelView


def configure(app):
    app.config['FLASK_ADMIN_SWATCH'] = os.environ.get('FLASK_ADMIN_SWATCH')

    admin = Admin(app, name='microblog admin', template_mode='bootstrap3')
    admin.add_view(PostModelView(app.db.posts, 'Post'))
