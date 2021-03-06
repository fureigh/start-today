from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

print os.environ['APP_SETTINGS']

if __name__ == '__main__':
    app.run()
