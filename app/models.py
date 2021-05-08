from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, \
RoleMixin, login_required, current_user
from app import  db
from datetime import datetime,timedelta 
import json
from time import time
import sqlalchemy

# try:
#     db.metadata.remove("new_claimers") 
# except sqlalchemy.exc.InvalidRequestError:
#     pass











#define DATABSE models


# Database Tables
roles_users = db.Table('roles_users', 
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)




roomies = db.Table('roomies',
    db.Column('roomie_follower', db.Integer, db.ForeignKey('user.id')),
    db.Column('roomie_followed', db.Integer, db.ForeignKey('user.id'))
)


roomie_request = db.Table('roomie_request',
    db.Column('request_sender_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('requested_user_id', db.Integer, db.ForeignKey('user.id')),

)


new_claimers = db.Table('new_claimer', 
    db.Column('claimer_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('finder_id', db.Integer, db.ForeignKey('user.id')),
    # extend_existing=True
)

# new_claimers.extend_existing = True


# sqlalchemy.schema.MetaData.remove(claimers) 




class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11), unique = True)
    whatssap_number = db.Column(db.String(11), unique = True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.String(10))
    image_file = db.Column(db.String(355), nullable = False, default = 'default1.jpg')
    # admin = db.Column(db.Boolean, nullable=False, default=False)
    paid = db.Column(db.Boolean, nullable=False, default=False)

    generic = db.Column(db.Boolean, nullable=False, default=False)

    is_student = db.Column(db.Boolean, nullable=True, default=False)

    is_admin = db.Column(db.Boolean, nullable=True, default=False)

    allows_phone_number_to_be_seen = db.Column(db.Boolean, nullable=True, default=True)

    allows_email_to_be_seen = db.Column(db.Boolean, nullable=True, default=True)

    has_aceepted_terms_and_conditions = db.Column(db.Boolean, nullable=False, default=False)


    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())

    caption = db.Column(db.String(160),default='saying Hey there! i\'m a user of STURF')
    more_about = db.Column(db.String(30000))

    address =  db.Column(db.Text)


    seeks_roomate = db.Column(db.Boolean())


    

    confirmed_at = db.Column(db.DateTime(), nullable=True)





    #RELATIONSHIPS

    # followers table
    followed = db.relationship(

        'User', secondary=followers,

        primaryjoin=(followers.c.follower_id == id),

        secondaryjoin=(followers.c.followed_id == id),

        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')


    # roomies table, this relationship connects two roomies to the roomies to the roomies table such that it can expos the request sender and the requested user
    is_roomies_with = db.relationship(

        'User', secondary=roomies,

        primaryjoin=(roomies.c.roomie_follower == id),

        secondaryjoin=(roomies.c.roomie_followed == id),

        backref=db.backref('roomie_followers', lazy='dynamic'), lazy='dynamic')




    # roomie_request relationship, this relationship connects two roomies to the roomie requests table such that it can expos the request sender and the requested user



    has_requested_to_be_roomies_with = db.relationship(

        'User', secondary=roomie_request,

        primaryjoin=(roomie_request.c.request_sender_id == id),

        secondaryjoin=(roomie_request.c.requested_user_id == id),

        backref=db.backref('roomie_requesters', lazy='dynamic'), lazy='dynamic')


    # ...




    # clainers table
    followed_claimers = db.relationship(

        'User', secondary=new_claimers,

        primaryjoin=(new_claimers.c.claimer_id == id),

        secondaryjoin=(new_claimers.c.finder_id == id),

        backref=db.backref('claiming_followers', lazy='dynamic'), lazy='dynamic')




    # messages relationship that links to the message sender and reciever


    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')

    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')



    claim_messages_sent = db.relationship('Claimers_messages',
                                    foreign_keys='Claimers_messages.sender_id',
                                    backref='claimer_sender', lazy='dynamic')

    claim_messages_received = db.relationship('Claimers_messages',
                                        foreign_keys='Claimers_messages.recipient_id',
                                        backref='Claimer_recipient', lazy='dynamic')



    last_message_read_time = db.Column(db.DateTime())

    last_notifications_read_time = db.Column(db.DateTime())


    # for new_claimers_messages section
    last_claimers_messages_read_time = db.Column(db.DateTime())
    # ...



    posts = db.relationship('Post', backref='author',lazy=True)



    viewed_posts = db.relationship('Viewed_Posts', backref='viewer',lazy=True)



    reported_posts = db.relationship('Reported_Post', backref='reporter',lazy=True)


    specific_message_read_time = db.relationship('Specific_Message_Read_Time',
    foreign_keys='Specific_Message_Read_Time.message_sender_id',
     backref='messages_sender',lazy='dynamic')


    claimers_Specific_Message_Read_Time = db.relationship('Claimers_Specific_Message_Read_Time',
    foreign_keys='Claimers_Specific_Message_Read_Time.message_sender_id',
     backref='messages_sender',lazy='dynamic')







    roomies = db.relationship('Roomie', backref='candidate',lazy=True)

    comments = db.relationship('Comments', backref='commentor',lazy=True)







    # BUY STURF RELATIONSHIPS

    ads = db.relationship('E_commerce', backref='seller',lazy=True)



    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')








    roles = db.relationship('Role', secondary = roles_users, backref=db.backref('users', lazy='dynamic'))


    








    #DATABASE DEFINITIONS



    # NEW NOTIFICATIONS DEFINITIONS


    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, user=self, data = data)
        db.session.add(n)
        return n

    def new_notifications(self):
        last_notifications_read_time = self.last_notifications_read_time or datetime(1900, 1, 1)

        return Notification.query.filter_by(user_id=self.id).filter(
            Notification.timestamp > last_notifications_read_time).order_by( Notification.timestamp.desc() ).limit(50)


    def new_notifications_count(self):
        last_notifications_read_time = self.last_notifications_read_time or datetime(1900, 1, 1)
        return Notification.query.filter_by(user_id=self.id).filter(
            Notification.timestamp > last_notifications_read_time).count()







    # NEW POST VIEW DEFINITIONS
    def has_viewed_post(self, post_id):
        return Viewed_Posts.query.filter_by(viewer = self, post_id=post_id).count()>0


    def has_reported_post(self, post_id):
        return Reported_Post.query.filter_by(reporter = self, post_id=post_id).count()>0


    def has_tried_to_claim_post(self, post_id):
        return claimers.query.filter_by(claimer_id = self.id, post_id=post_id).count()>0





    # NEW MESSAGES COUNT DEFINITIONS
    def new_messages(self):

        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)

        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()


    def specific_new_messages_from(self, user):

        specifc_msg = Specific_Message_Read_Time.query.filter_by(messages_sender = user).first()
        # print(specifc_msg)


        last_read_time = datetime(1900, 1, 1)
        try:
            last_read_time = specifc_msg.last_read_time or datetime(1900, 1, 1)
    
        except AttributeError:
            pass

        # last_read_time = specifc_msg.last_read_time or datetime(1900, 1, 1)


        # print(Message.query.filter_by(recipient=self).filter(
        #     Message.timestamp > last_read_time).count())


        return Message.query.filter_by(author = user, recipient = self).filter(
            Message.timestamp > last_read_time).count()

























    # NORMAL FOLLOWER DEFINITIONS
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0


    def followed_posts(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id).order_by(
                    Post.date_posted.desc())

    def ordered_followed_posts(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id).join(User, (User.id == Post.user_id)).order_by(User.paid.desc()).order_by(
                    Post.date_posted.desc())

    def has_no_followed_posts(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id).join(User, (User.id == Post.user_id)).order_by(User.paid.desc()).order_by(
                    Post.date_posted.desc()).count() < 1


    # CLAIMER  DEFINITIONS
    def follow_finder(self, user):
        if not self.is_following_finder(user):
            self.followed_claimers.append(user)

    def unfollow_finder(self, user):
        if self.is_following_finder(user):
            self.followed_claimers.remove(user)

    def is_following_finder(self, user):
        return self.followed_claimers.filter(new_claimers.c.finder_id == user.id).count() > 0

    def is_following_finder_or_is_the_finder(self, user):
        return user in self.claiming_followers.union( self.followed_claimers)


    def claimer_author_instance(self,id):
        author = User.query.get(id)

        return author

    def has_tried_to_claim(self, id):
        return claimers.query.filter_by(claimer_id = self.id, post_id = id).count()>0






    def new_claimer_messages_count(self):

        last_read_time = self.last_claimers_messages_read_time or datetime(1900, 1, 1)

        return Claimers_messages.query.filter_by(Claimer_recipient=self).filter(
            Claimers_messages.date_of_message > last_read_time).count()


    def specific_new_claimer_messages_from(self, user, post_id):

        specifc_msg = Claimers_Specific_Message_Read_Time.query.filter_by(messages_sender = user).filter(Claimers_Specific_Message_Read_Time.post_id == post_id).first()

        last_read_time = datetime(1900, 1, 1)

        try:
            last_read_time = specifc_msg.last_read_time or datetime(1900, 1, 1)
    
        except AttributeError:
            pass


        return Claimers_messages.query.filter_by(claimer_sender = user, Claimer_recipient = self).filter(
            Claimers_messages.date_of_message > last_read_time).filter(Claimers_messages.post_id == post_id).count()







    # ROOMIE REQUESTS DEFINITIONS
    def request_roomie(self, user):
        if not self.has_sent_roomie_request_to(user):
            self.has_requested_to_be_roomies_with.append(user)

    def unrequest_roomie(self, user):
        if self.has_sent_roomie_request_to(user):
            self.has_requested_to_be_roomies_with.remove(user)

    def has_sent_roomie_request_to(self, user):
        return self.has_requested_to_be_roomies_with.filter(roomie_request.c.requested_user_id == user.id).count() > 0





    # ROOMIE FOLLOWER DEFINITIONS
    def follow_roomie(self, user):
        if not self.is_following_roomie(user):
            self.is_roomies_with.append(user)

    def unfollow_roomie(self, user):
        if self.is_following_roomie(user):
            self.is_roomies_with.remove(user)

    def is_following_roomie(self, user):
        return self.is_roomies_with.filter(roomies.c.roomie_followed == user.id).count() > 0

    def all_roomies_count(self):
        return self.roomie_followers.union(self.is_roomies_with).count()

    def is_following_or_followed_by(self, user):
        return user in self.roomie_followers.union( self.is_roomies_with)






















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











#######################################################################################################################################################################
######################################################################### ROOMIE STURF MODELS #########################################################################
#######################################################################################################################################################################


# database for people who are looking for a roomate
class Roomie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date_joined = db.Column(db.DateTime(), nullable = False)
    religion =  db.Column(db.String(150), default='unset')
    level =  db.Column(db.String(150), default='unset')
    based =  db.Column(db.String(150), default='unset')
    budget =  db.Column(db.String(150))


    birth_day = db.Column(db.String(20),default='unset')
    likes =  db.Column(db.String(150),default='unset')
    dislikes =  db.Column(db.String(150),default='unset')


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

    # __searchable__ = ['title']

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

    last_interaction_time = db.Column(db.DateTime(), nullable = True, default = datetime.utcnow())


    #RELATIONSHIP

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    claimer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)



    def __repr__(self):
        return '<CLAIMERS ---> id   {},  {},   post_id {}>'.format( self.claimer_id, self.claimer_name, self.post_id )




# stores all messages sent and recieved for thise trying to claim to an item
class Claimers_messages(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    message_body = db.Column(db.String(140))

    date_of_message = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    post_id =  db.Column(db.Integer, unique = False, nullable = False)


    def __repr__(self):
        return '\n<Message {}>'.format(self.message_body)




class Claimers_Specific_Message_Read_Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_read_time = db.Column(db.DateTime(), default = datetime.utcnow())
    post_id =  db.Column(db.Integer, unique = False, nullable = False)

    def __repr__(self):
        return f" claimer_Specific_Message_Read_Time('{self.message_sender_id}', '{self.last_read_time}') "





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











#############################################################################################################################################################################
############################################################################# ECOMMERCE MODEL ##############################################################################
#############################################################################################################################################################################



class E_commerce(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    
    title =  db.Column(db.String(1500), nullable = True)

    image_files = db.Column( db.ARRAY(db.String(1500)) )

    date_of_post = db.Column(db.DateTime(), nullable = True, default = datetime.utcnow())

    price =  db.Column(db.Integer,  nullable = True)

    brand =  db.Column(db.String(1500), nullable = True)

    condition =  db.Column(db.String(1500), nullable = True)

    ram =  db.Column(db.String(1500), nullable = True)

    screen_size =  db.Column(db.String(1500), nullable = True)

    colour =  db.Column(db.String(1500), nullable = True)

    camera =  db.Column(db.String(1500), nullable = True)

    description = db.Column(db.Text)    

    storage_capacity =  db.Column(db.String(1500), nullable = True)

    operating_system =  db.Column(db.String(1500), nullable = True)

    type = db.Column(db.String(1500), nullable = True)

    subtype =  db.Column(db.String(1500), nullable = True)

    processor =  db.Column(db.String(1500), nullable = True)

    number_of_cores =  db.Column(db.String(1500), nullable = True)

    graphics_card =  db.Column(db.String(1500), nullable = True)

    graphics_card_memory =  db.Column(db.String(1500), nullable = True)

    storage_type =  db.Column(db.String(1500), nullable = True)

    operating_system =  db.Column(db.String(1500), nullable = True)

    make =  db.Column(db.String(1500), nullable = True)

    platform =  db.Column(db.String(1500), nullable = True)

    format =  db.Column(db.String(1500), nullable = True) 

    gender =  db.Column(db.String(1500), nullable = True)

    size =  db.Column(db.String(1500), nullable = True)

    style =  db.Column(db.String(1500), nullable = True)

    upper_material =  db.Column(db.String(1500), nullable = True)

    outsole_material =  db.Column(db.String(1500), nullable = True)   

    material =  db.Column(db.String(1500), nullable = True)

    closure =  db.Column(db.String(1500), nullable = True) 

    main_material =  db.Column(db.String(1500), nullable = True)

    main_stone =  db.Column(db.String(1500), nullable = True) 

    formulation =  db.Column(db.String(1500), nullable = True)

    scent =  db.Column(db.String(1500), nullable = True)

    volume =  db.Column(db.String(1500), nullable = True)

    tone =  db.Column(db.String(1500), nullable = True) 

    target_area =  db.Column(db.String(1500), nullable = True) 

    skin_type = db.Column(db.String(1500), nullable = True)

    benefits = db.Column(db.String(1500), nullable = True) 

    level =  db.Column(db.String(1500), nullable = True)

    duration =  db.Column(db.String(1500), nullable = True)

    service_features =  db.Column(db.String(1500), nullable = True)

    round_the_clock_service = db.Column(db.Boolean())

    type_of_service =  db.Column(db.String(1500), nullable = True)  

    service_include =  db.Column(db.String(1500), nullable = True)  

    year_of_manufacture =  db.Column(db.String(1500), nullable = True)

    transmission =  db.Column(db.String(1500), nullable = True)

    mileage =  db.Column(db.String(1500), nullable = True) 

    ad_type = db.Column(db.String(1500), nullable = True)





#RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < E_commerce  ('{self.id}', {self.price},'{self.title}', {self.description}', '{self.condition}', '{self.camera}',  '{self.screen_size}') > \n\n"






