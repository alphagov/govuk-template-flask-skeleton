# govuk-template-flask-skeleton

This Python app creates a frontend skeleton based on Flask, Flask-Assets and the govuk_frontend_toolkit (and GOV.UK template). This renders pages with the GOV.UK style. Webpages can be coded using styles from GOV.UK Elements.

govuk_frontend_toolkit is pulled in as a git submodule.
To get the contents of the submodule run the following git commands.
 
    git submodule init
    git submodule update

### Installation

In a virtual environment, install the Python requirements:

    pip install -r requirements.txt

You will need sass installed:

    bundle install

### Running the app

To run the app:

    python app.py

Initial URL -

    http://localhost:5000/helloworld

(template for this page lives in /templates/hello-world.html, which adds a content block to govuk_template.html)
