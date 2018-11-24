
from datetime import datetime
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required, is_logged_in

from wtforms.fields import Field, SelectField, StringField, TextAreaField, DateTimeField
from wtforms.form import Form
from wtforms.validators import DataRequired
from wtforms.widgets import TextInput

from slugify import slugify_unicode


class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [slugify_unicode(x.strip()) for x in valuelist[0].split(',')]
        else:
            self.data = []


class BetterTagListField(TagListField):
    def __init__(self, label='', validators=None, remove_duplicates=True, **kwargs):
        super(BetterTagListField, self).__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates

    def process_formdata(self, valuelist):
        super(BetterTagListField, self).process_formdata(valuelist)
        if self.remove_duplicates:
            self.data = list(self._remove_duplicates(self.data))

    @classmethod
    def _remove_duplicates(cls, seq):
        """Remove duplicates in a case insensitive, but case preserving manner"""
        d = {}
        for item in seq:
            if item.lower() not in d:
                d[item.lower()] = True
                yield item


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[('news', 'News')])
    tags = BetterTagListField('Tags', description='tags are separed by comma.')
    pubdate = DateTimeField('Publish Date', default=datetime.now)


class PostModelView(ModelView):
    decorators = [login_required]
    column_list = ['pubdate', 'title', 'category']
    form = PostForm

    def is_accessible(self, ):
        if is_logged_in():
            return True
        return False
