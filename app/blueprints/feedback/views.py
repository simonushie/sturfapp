from flask import Blueprint
from flask import render_template, request
from flask_security import login_required


feedback_blueprint = Blueprint('feedback', __name__, 
    static_folder='static', static_url_path = '/static')


@feedback_blueprint.route('/',methods=['GET'])
@login_required  
def index():
    return render_template("feedback/feedback.html")
