from flask import Blueprint
from flask import render_template, request
from flask_security import login_required
from app.models import Light_sturf
import sqlite3


history_blueprint = Blueprint('history', __name__, 
    static_folder='static', static_url_path = '/static')


@history_blueprint.route('/',methods=['GET'])
@login_required 
def history():
    rows = Light_sturf.query.order_by(Light_sturf.period.desc()).limit(10)
    
    return render_template("history/history.html", rows = rows)





@history_blueprint.route('/paginated_history',methods=['GET'])
@login_required 
def history_paginated():

	page = request.args.get('page', 1, type = int)
	rows = Light_sturf.query.order_by(Light_sturf.period.desc()).paginate(page = page, per_page = 10 )

	return render_template("history/history_paginated.html", rows = rows)