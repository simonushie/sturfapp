from flask import Blueprint
from flask import render_template


example = Blueprint('example', __name__,
    static_folder='static', static_url_path = 'com')

@example.route('/')
def index():
    return "THIS IS AN EXAMPLE APP WITH BLUEPRINTS"


@example.route('/com')
def com():
    return "THIS IS THE COM ROUTE"



@example.route('/exam')                                                 
def this():
    return render_template("example/example_blueprint.html")