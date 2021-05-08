from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, \
RoleMixin, login_required, current_user
from app import  db
from datetime import datetime,timedelta 
import json
from time import time












#######################################################################################################################################################################
########################################################################## LIGHT STURF MODELS #########################################################################
#######################################################################################################################################################################






# the historical database that stores all the light fluctuatioin events in the databasee for the light sturf route
class Light_sturf(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    location = db.Column(db.String(150), nullable = False)
    period = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    state =  db.Column(db.String(150), default='off')

    
    def __repr__(self):
        return f" Light_sturf('{self.location}', '{self.period}') "





# the single row database that updates the light sturf routes with the current state of electricity
class Light_sturf_update(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    location = db.Column(db.String(150), nullable = False)
    period = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    state =  db.Column(db.String(150), default='off')

    
    def __repr__(self):
        return f" Light_sturf_update('{self.location}', '{self.period}') "







