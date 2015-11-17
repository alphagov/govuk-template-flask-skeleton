import os
from flask import Flask, render_template
from flask.ext import assets
from flask.ext.scss import Scss

app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets/stylesheets')

env = assets.Environment(app)

# Tell flask-assets where to look for our sass files.
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'stylesheets')
]


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)