from datetime import datetime

from tinydb_serialization import Serializer, SerializationMiddleware
from tinymongo import TinyMongoClient

class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime

    def __init__(self, format='%Y-%m-%dT%H:%M:%S', *args, **kwargs):
        super(DateTimeSerializer, self).__init__(*args, **kwargs)
        self._format = format

    def encode(self, obj):
        return obj.strftime(self._format)

    def decode(self, s):
        return datetime.strptime(s, self._format)

class CustomClient(TinyMongoClient):
    @property
    def _storage(self):
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), 'DateTime')
        # register other custom serializers
        return serialization


def configure(app):
    connection = CustomClient()

    # either creates a new database file or accesses an existing one named `my_tiny_database`
    app.db = connection.my_blog
