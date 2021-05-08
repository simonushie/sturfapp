from flask import Blueprint
from flask import render_template, request
from flask_security import login_required


rent_blueprint = Blueprint('rent', __name__, 
    static_folder='static', static_url_path = '/static')


@rent_blueprint.route('/',methods=['GET'])
@login_required 
def index():
    return render_template("rent/rent.html")
