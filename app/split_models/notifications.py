
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, \
RoleMixin, login_required, current_user
from app import  db
from datetime import datetime,timedelta 
import json
from time import time










#############################################################################################################################################################################
############################################################################# NOTIFICATION MODEL ##############################################################################
#############################################################################################################################################################################



class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    data = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)


    def __repr__(self):
        return '<New notification {}>'.format(self.name)


