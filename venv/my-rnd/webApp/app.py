from flask import Flask
import json
import datetime

app = Flask(__name__)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.name, obj.age, obj.timestamp
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)


class User:
    def __init__(self, name, age, timestamp):
        self.name = name
        self.age = age
        self.timestamp = timestamp

    def __str__(self):
        return self.name + self.age + self.timestamp


@app.route("/")
def hello():
    return "Hello Everyone!!"


@app.route("/hello/<name>")
def hello_user(name):
    new_user = User(name, 34, datetime.datetime(2019, 4, 4, 5, 20))
    return json.dumps(new_user, cls=DateTimeEncoder)


if __name__ == '__main__':
    app.run(debug=True)




