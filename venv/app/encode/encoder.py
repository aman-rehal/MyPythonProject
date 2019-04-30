import json
import datetime
from model.models import Author, Book


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Author):
            return obj.name, obj.email
        elif isinstance(obj, Book):
            return obj.title, obj.author, obj.year
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)

