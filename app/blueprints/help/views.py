from flask import Blueprint
from flask import render_template, request
from flask_security import login_required


help_blueprint = Blueprint('help', __name__, 
    static_folder='static', static_url_path = '/static')


@help_blueprint.route('/',methods=['GET'])
@login_required   
def index():
    return render_template("help/help.html")
