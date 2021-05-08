from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, \
RoleMixin, login_required, current_user
from app import  db
from datetime import datetime,timedelta 
import json
from time import time






#######################################################################################################################################################################
######################################################################### ROOMIE STURF MODELS #########################################################################
#######################################################################################################################################################################


# database for people who are looking for a roomate
class Roomie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date_joined = db.Column(db.DateTime(), nullable = False)
    religion =  db.Column(db.String(150), default='EMPTY')
    level =  db.Column(db.String(150), default='EMPTY')
    based =  db.Column(db.String(150), default='EMPTY')
    budget =  db.Column(db.String(150))


    #RELATIONSHIP
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return f" Roomie('{self.level}', '{self.date_joined}', '{self.budget}') "







# TRACKS HE LAST TIME A ROOMIE READ ANOTHER ROOMIE'S MESSAGE AND THAT ROOMIE IS STORED HERE AS THE message_sender_id
class Specific_Message_Read_Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_read_time = db.Column(db.DateTime(), default = datetime.utcnow())

    def __repr__(self):
        return f" Specific_Message_Read_Time('{self.message_sender_id}', '{self.last_read_time}') "


# stores all messages sent and recieved for roomie sturf
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)




