from flask import Blueprint
from flask import render_template, request



about_us_blueprint = Blueprint('about_us', __name__, 
    static_folder='static', static_url_path = '/static')


@about_us_blueprint.route('/',methods=['GET'])
def index():
    return render_template("about_us/Developers.html")
