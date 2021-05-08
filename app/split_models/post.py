from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, \
RoleMixin, login_required, current_user
from app import  db
from datetime import datetime,timedelta 
import json
from time import time











#######################################################################################################################################################################
########################################################################## POST STURF MODELS ##########################################################################
#######################################################################################################################################################################




class Comments(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    comment_body = db.Column(db.Text)
    date_of_comment = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    post_id =  db.Column(db.Integer, unique = False, nullable = False)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self):
        return f" Comments ('{self.comment_body}', '{self.date_of_comment}') "







class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    image_file = db.Column(db.String(355), nullable = False, default = 'default_post.jpg')
    title = db.Column(db.String(100), unique = False, nullable = False)
    date_posted = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    content = db.Column(db.String(30000), unique = False, nullable = False)
    link = db.Column(db.String(30000), unique = False, nullable = True)
    venue = db.Column(db.String(100), unique = False, nullable = True)
    date = db.Column(db.DateTime(), nullable=True)
    is_event =  db.Column(db.Boolean, nullable=False, default=False)
    possession =  db.Column(db.Boolean, nullable=True, default=False)
    is_Lost_and_found =  db.Column(db.Boolean, nullable=True, default=False)
    is_Lost_and_searching =  db.Column(db.Boolean, nullable=True, default=False)
    item_category = db.Column(db.String(30000), nullable = True)


    #RELATIONSHIP
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def views_count(self):
        return Viewed_Posts.query.filter_by(post_id = self.id).count()




    def report_count(self):

        reported_post = Reported_Post.query.filter_by(post_id = self.id ).all()

        report_list = []

    
    # add all the rows in the database one by one

        for each in reported_post:
            if each.inappropriate_count is None:
                each.inappropriate_count = 0

            if each.offensive_count is None:
                each.offensive_count = 0

            if each.hate_speech_count is None:
                each.hate_speech_count = 0

            if each.inaccurate_info_count is None:
                each.inaccurate_info_count= 0

            add = each.inappropriate_count + each.offensive_count + each.hate_speech_count + each.inaccurate_info_count 
            val = int(add)
            report_list.append(val)

    # check if the number of reports is more than 10 and then delete the post 
        return sum(report_list)
    
    def __repr__(self):
        return f" Post('{self.title}', '{self.date_posted}') "




class Viewed_Posts(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    post_id =  db.Column(db.Integer, unique = False, nullable = False)

    #RELATIONSHIP
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return f" Post('{self.post_id}', '{self.user_id}') "



class Reported_Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    post_id =  db.Column(db.Integer, unique = False, nullable = False)
    report_type = db.Column(db.String(100), unique = False, nullable = False)

    inappropriate_count =  db.Column(db.Integer, unique = False)
    offensive_count =  db.Column(db.Integer, unique = False)    
    hate_speech_count =  db.Column(db.Integer, unique = False)
    inaccurate_info_count =  db.Column(db.Integer, unique = False)

    #RELATIONSHIP
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return f" Post('{self.post_id}', '{self.user_id}',  '{self.inappropriate_count}', '{self.offensive_count}') "










class claimers(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    claimer_profile_pic = db.Column(db.String(355), nullable = False, default = 'default_post.jpg')
    claimer_name = db.Column(db.String(100), unique = False, nullable = False)
    date_of_application = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    item_category = db.Column(db.String(30000), unique = False, nullable = False)
    email = db.Column(db.String(30000), unique = False, nullable = True)
    item_desription = db.Column(db.String(100), unique = False, nullable = True)
    post_id =  db.Column(db.Integer, unique = False, nullable = False)



    #RELATIONSHIP

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    claimer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)




# class Claimers_messages(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     message_body = db.Column(db.Text)
#     date_of_message = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
#     post_id =  db.Column(db.Integer, unique = False, nullable = False)
    
#     #RELATIONSHIP
#     claimer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


#     def __repr__(self):
#         return f" Comments ('{self.message_body}', '{self.date_of_message}') "






# stores all messages sent and recieved for roomie sturf
class Claimers_messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    message_body = db.Column(db.String(140))

    date_of_message = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    post_id =  db.Column(db.Integer, unique = False, nullable = False)


    def __repr__(self):
        return '<Message {}>'.format(self.body)




