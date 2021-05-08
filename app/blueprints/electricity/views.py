from flask import Blueprint, render_template, request
from flask_security import login_required
import sqlite3
from datetime import datetime
import time
import random
from app.models import Light_sturf, Light_sturf_update
from app import db 


electricity = Blueprint('electricity', __name__, 
    static_folder='static', static_url_path = '/static')



@electricity.route('/')
@login_required 
def where():
    return render_template("electricity/where.html")


#this route saves all date gotten as query parameters
@electricity.route('/BtfT2GB2h9s4kP_cjZdqkSv5Bps/api-save',methods=['GET'])
def api_save():
    #this function populates the light_sturf table
    def Light_list():
        location = request.args.get('location',  type = str)
        state = request.args.get('state',  type = str) 


        first = Light_sturf(
                        location = location,
                        state = state
                        )


        db.session.add(first)
        db.session.commit()


    #this function updates the light_sturf table which has only a single row
    def Light_update():
        
        location = request.args.get('location',  type = str)
        state = request.args.get('state',  type = str) 

        Light_update = Light_sturf_update.query.filter_by(location = location).first_or_404()

        Light_update.location = location
        Light_update.state = state


       
        db.session.commit()


 
    Light_list()
    Light_update()

    return render_template("electricity/testing.html", location = request.args.get('location',  type = str), state = request.args.get('state',  type = str))
    


# @electricity.route('/first/api-save',methods=['GET'])
# def api_save():
#     location = request.args.get('location',  type = str)
#     status = request.args.get('status',  type = str) 


#     Light_sturf.location = location
#     Light_sturf.status = status


#     light_sturf = Light_sturf(
#                     image_file = filename,
#                     title = title, 
#                     content =  content, 
#                     author = current_user)

 

#     return render_template("electricity/testing.html", location = location, status = status)



@electricity.route('/campus',methods=['GET'])
@login_required  
def campus():
    light = Light_sturf_update.query.filter_by(location = 'campus').first_or_404()
    pic = 'static/lightbulb.gif'
    color = "#79ff4d"
    status = "status"
    report = "report"
    t1 = "t1"
    t2 = "t2"
    title = "Campus"

    success_report = ['Cheers! the power has been restored','Hurray! there is power off campus',
        'The power is back!',
        'The power supply has been restored','The electricity is back!','Homes off campus are shining bright! '
        ]

    failure_report = ['oops! no light on campus','Unfornately the campus remains dark',
    'Sorry! but there is no electricity on campus','The power hasn\'t still been restored, please check back shortly ',
     'nope.....no power', 'Nothing! yet, please try again shortly']



    if light.state == 'on':
        status = random.choice(success_report)
        pic = 'static/lightbulb.gif'
        color = "#79ff4d"
        report = "The electricity was last restored around"
        t1 = ' #46BC28'
        t2 = '#79ff4d'

    else:
        status = random.choice(failure_report)
        pic = 'static/off.jpeg'
        color = "red"
        report = "The electricity was last interrupted at"
        t1 = 'red'
        t2 = 'red'



    return render_template("electricity/check.html",status = status, pic=pic,color=color,report = report,t1 = t1,t2 = t2, title = title, light = light)




@electricity.route('/off-campus',methods=['GET'])
@login_required  
def offcampus():
    light = Light_sturf_update.query.filter_by(location = 'offcampus').first_or_404()
    pic = 'static/lightbulb.gif'
    color = "#79ff4d"
    status = "status"
    report = "report"
    t1 = "t1"
    t2 = "t2"
    title = "Off campus"


    success_report = ['Cheers! the power has been restored','Hurray! there is power off campus',
        'The power is back!',
        'The power supply has been restored','The electricity is back!','Homes off campus are shining bright! '
        ]

    failure_report = ['oops! no light off campus','Unfornately the streets off campus remain dark',
    'Sorry! but there is no electricity off-campus','The power hasn\'t still been restored, please check back shortly ',
     'electricity is non-existent at the moment', 'Nothing! yet, please try again shortly']


    if light.state == 'on':
        status = random.choice(success_report)
        pic = 'static/lightbulb.gif'
        color = "#79ff4d"
        report = "The electricity was last restored around"
        t1 = ' #46BC28'
        t2 = '#79ff4d'

    else:
        status = random.choice(failure_report)
        pic = 'static/off.jpeg'
        color = "red"
        report = "The electricity was last interrupted at"
        t1 = 'red'
        t2 = 'red'



    return render_template("electricity/check.html",status = status, pic=pic,color=color,report = report,t1 = t1,t2 = t2, title = title, light = light)








