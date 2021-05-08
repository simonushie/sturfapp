from flask import render_template, request, abort
from app import app, db  #,process_data
from app.forms import CustomLoginForm, ExtendedRegisterForm
import sqlite3
import time
import random
from flask_mail import Mail
from datetime import datetime,timedelta
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user
from flask_security.utils import hash_password
from app.models import User, Role, Post, Roomie

import random







app.debug = True
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True










# Mail Configuration

app.config['SECURITY_EMAIL_SENDER'] = 'simonushie99@gmail.com'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = app.config['SECURITY_EMAIL_SENDER']





mail = Mail(app)




















#setup Flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, login_form = CustomLoginForm,  register_form=ExtendedRegisterForm, confirm_register_form=ExtendedRegisterForm)


















# create a user to test with(first time only and for USER model only) 

# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='simonushie99@gmail.com', 
#         password = hash_password('zzzzzz'), \
#         phone = '08102640833', 
#         first_name = 'Simon', 
#         last_name = 'Ushie',
#         paid = False,
#         more_about = 'im rich, thats my superpower',
#         birth_day = '5-nov-1313',
#         likes = 'money',
#         dislikes = 'liars',
#         age = ''
#		  is_admin = True
#         )
#     db.session.commit()

# db.init_app(app)









@app.route('/admin')
def admin():

	if current_user.email != "simonushie99@gmail.com":
		abort(403)

	users = User.query.all()


	return render_template("admin_index.html")





@app.route('/admin/<request_type>')
def admin_ops(request_type):

	if current_user.email != "simonushie99@gmail.com":
		abort(403)

	users = User.query.all()

	report = "welcome to admin page simon "



	if request_type == "remove_seeks_roomate":
		for user in users:
			user.seeks_roomate = False
			report = "all seeks roomate removed sir! "
			db.session.commit()


	if request_type == "remove_all_phone_nos":
		for user in users:
			user.phone = None
			report = "all phone numbers removed sir! "
			db.session.commit()



	return render_template("admin.html", report = report)







# @app.route('/CtfT2GB2h9s4kP_cjZdqkSv5Bps/api-save',methods=['GET'])
# def api_save():
#     def lightStatus(status,timestamp,location):
#         msg="msg"
#         try:
#             sqliteConnection = sqlite3.connect('app/data/lightStatus.db',
#                                                detect_types=sqlite3.PARSE_DECLTYPES |
#                                                sqlite3.PARSE_COLNAMES)
#             cursor = sqliteConnection.cursor()
#             print("Connected to SQLite")
#             # update developer detail
#             sqlite_update = """UPDATE 'lightStatus'
#                           SET state = ?, period = ?
#                           WHERE  location = ?"""

#             data_tuple = (status,timestamp,location)
#             cursor.execute(sqlite_update, data_tuple)
#             sqliteConnection.commit()
#             print("Update added successfully \n")


#             # get date from database
#             sqlite_select_query = """SELECT period from lightStatus where location = ?"""
#             cursor.execute(sqlite_select_query, (location,))
#             records = cursor.fetchone()[0]

#             stamp = int(records)

#             date = datetime.fromtimestamp(stamp)

#             date_string = date.strftime("%A") + " " + date.strftime("%I") + ":" + date.strftime("%M")  + date.strftime("%p") 

#             # print (date_string)

#             # print(type(records))

#             cursor.close()

#         except sqlite3.Error as error:
#             print("Error while working with SQLite", error)
#         finally:
#             if (sqliteConnection):
#                 sqliteConnection.close()
#                 print("sqlite connection is closed")



#     # Second function that populates the records database
#     def populateRecords(status,era,location):
        
#         record_msg = "record msg"
#         error = 'error'

#         sqliteConnection = sqlite3.connect('app/blueprints/history/records.db',
#                                                detect_types=sqlite3.PARSE_DECLTYPES |
#                                                sqlite3.PARSE_COLNAMES)
        
#         cursor = sqliteConnection.cursor()

#         sqlite_add = """INSERT INTO records (state,period,location) VALUES (?,?,?)"""

#         data_tuple = (status,era,location)
#         cursor.execute(sqlite_add, data_tuple)
#         sqliteConnection.commit()
#         print("record added successfully \n \n \n ")
#         sqliteConnection.close()
#         print("connection to records db is closed \n \n ")


#     lightStatus(request.args.get('status'),int(time.time()),request.args.get('location'))
#     populateRecords(request.args.get('status'),datetime.now().strftime("%A " " %I:%M %p  %B " " %d "),request.args.get('location'))
#     msg = "seems like all went well"
#     record_msg = "seems like all went well recording those requests"
    


#     return render_template("testing.html", record_msg = record_msg, msg = msg)









#i use this route for testing purposes on the history route only

# @app.route('/list')
# def list():
#    con = sqlite3.connect("app/data/records.db")
#    con.row_factory =  sqlite3.Row
   
#    cur = con.cursor()
#    cur.execute("select * from records")
   
#    rows = cur.fetchall();
#    con.close()
#    print ("old connection closed")



#    return render_template("list.html",rows = rows)