import os
from flask import Flask, render_template
from flask.ext import assets
from flask.ext.assets import Environment, Bundle
#from flask.ext.scss import Scss
#from flask.ext.sass import sass
from webassets.filter import get_filter


app = Flask(__name__)
#Scss(app, static_dir='static', asset_dir='assets/stylesheets')
#sass(app, input_dir='assets/stylesheets', output_dir='static')

app.config['ASSETS_DEBUG'] = True

env = assets.Environment(app)

env.config['sass_bin'] = '/usr/local/bin/sass'

# Tell flask-assets where to look for our sass files.
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'assets/stylesheets'),
    os.path.join(os.path.dirname(__file__), 'assets'),
    os.path.join(os.path.dirname(__file__), 'assets/stylesheets/govuk_frontend_toolkit')
]


scss = get_filter('scss', as_output=True)

env.register(
    'css_all',
    assets.Bundle(
        'main.scss',
        filters='scss',
        output='static/css_all.css'
    )
)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)