import os
from flask import Flask, render_template
from flask.ext import assets

app = Flask(__name__)

env = assets.Environment(app)

# Tell flask-assets where to look for our sass files.
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'sass')
]




env.register(
    'css_all',
    assets.Bundle(
        'all.sass',
        filters='sass',
        output='css_all.css'
    )
)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)