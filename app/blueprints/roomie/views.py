from flask import Blueprint, session, render_template,redirect,url_for,request,flash,redirect,current_app, abort

from flask_security import login_required, current_user,logout_user
from app import db 
from app.models import  Roomie, User, Message, Specific_Message_Read_Time, Comments
from app.forms import RoomieRegisterForm, BasedForm, ReligionForm, LevelForm, MessageForm, BudgetForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import secrets
import os
from datetime import datetime
from PIL import Image
from sqlalchemy import desc



roomie_blueprint = Blueprint('roomie', __name__, 
    static_folder='static', static_url_path = '/static')



@roomie_blueprint.route('/find-a-roomie', methods=['GET'])
@login_required
def find_a_roomie():
    if not current_user.seeks_roomate:
        abort(403)

    page = request.args.get('page', 1, type = int) 
    sort = request.args.get('sort')

    sort_value = 'normal'

    roomies = Roomie.query


    if page != None:

        if sort == 'normal':
            sort_value = 'normal'
            # roomies = Roomie.query.order_by(Roomie.date_joined.desc()).paginate(page = page, per_page = 10  )
            roomies = Roomie.query.join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )

        elif sort == 'Christianity':
            sort_value = 'Christianity'
            roomies =  Roomie.query.filter_by(religion = 'Christianity').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )

        elif sort == 'Islam':
            sort_value = 'Islam'
            roomies =  Roomie.query.filter_by(religion = 'Islam').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )

        elif sort == 'religion-other':
            sort_value = 'religion-other'
            roomies =  Roomie.query.filter_by(religion = 'Other').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )



        elif sort == '100L':
            sort_value = '100L'
            roomies =  Roomie.query.filter_by(level = '100L').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )


        elif sort == '200L':
            sort_value = '200L'
            roomies =  Roomie.query.filter_by(level = '200L').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )


        elif sort == '300L':
            sort_value = '300L'
            roomies =  Roomie.query.filter_by(level = '300L').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )


        elif sort == '400L':
            sort_value = '400L'
            roomies =  Roomie.query.filter_by(level = '400L').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )



        elif sort == '500L':
            sort_value = '500L'
            roomies =  Roomie.query.filter_by(level = '500L').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )



        elif sort == 'gidan-kwano':
            sort_value = 'gidan-kwano'
            roomies =  Roomie.query.filter_by(based = 'Gidan Kwano').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )



        elif sort == 'bosso':       
            sort_value = 'bosso'
            roomies =  Roomie.query.filter_by(based = 'Bosso').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )



        elif sort == 'based-other':
            sort_value = 'based-other'
            roomies =  Roomie.query.filter_by(based = 'Other').join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 10  )




    return render_template("roomie/find-a-roomie.html", roomies = roomies, sort_value = sort_value)












@roomie_blueprint.route('/roomie-template/<email>', methods=['GET'])
@login_required
def roomie_template(email):
    user = User.query.filter_by(email = email).first_or_404()

    roomie = Roomie.query.filter_by(user_id = user.id).first_or_404()

    budget = roomie.budget
    print (budget)


    p = roomie.candidate.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))

    return render_template("roomie/roomie-template.html", roomie = roomie, img = img, budget = budget)


























@roomie_blueprint.route('/send-roomie-request/<int:id>/<request_type>', methods=['GET','POST'])
@login_required
def send_roomie_request(id, request_type):
    
    user = User.query.filter_by(id = id).first_or_404()

    if user == current_user:
        abort(403)

    u1 = current_user
    u2 = user

    if request_type == 'request_roomie':
        u1.request_roomie(u2)
        flash('Your request has been sent to {}'.format(user.first_name), 'success')
        u2.add_notification('you_recieved_new_roomie_request', user.roomie_requesters.count())
        db.session.commit()

    elif request_type == 'unrequest_roomie':
        u1.unrequest_roomie(u2)
        flash('Your request to {} has been cancelled'.format(user.first_name), 'success')
        db.session.commit()


    return  redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))







@roomie_blueprint.route('/remove_roomie/<int:id>/<request_type>', methods=['GET','POST'])
@login_required
def remove_roomie(id,request_type):
    
    user = User.query.filter_by(id = id).first_or_404()

    u1 = current_user
    u2 = user

    if u2 == current_user:
        abort(403)


    if request_type == 'remove':
        if u2.is_following_roomie(u1):
            u2.unfollow_roomie(u1)
            flash(' {} stopped following you because you removed them '.format(user.first_name), 'success')
            db.session.commit()

        elif u1.is_following_roomie(u2):
            u1.unfollow_roomie(u2)
            flash(' you stopped following {}  because you removed them '.format(user.first_name), 'success')
            db.session.commit()



    return  redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))




@roomie_blueprint.route('/accept-roomie-request/<int:id>', methods=['GET','POST'])
@login_required
def accept_roomie_request(id):
    
    user = User.query.filter_by(id = id).first_or_404()

    requested_user = current_user
    request_sender = user

    if request_sender == current_user:
        abort(403)

    if not request_sender.has_sent_roomie_request_to(requested_user):
        abort(403)

    request_sender.unrequest_roomie(requested_user)

    request_sender.follow_roomie(requested_user)

    request_sender.add_notification('the_other_user_accepted_your_roomie_request', str(requested_user.first_name) )

    db.session.commit()
    flash('you accepted {} \'s request, you can chat them up now'.format(request_sender.first_name), 'success')

    return  redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))








@roomie_blueprint.route('/roomie-requests/<request_type>', methods=['GET'])
@login_required
def roomie_requests(request_type):

    roomie_type = 'requesters'

    if request_type == 'requesters':
        requesters = current_user.roomie_requesters
        roomie_type = 'requesters'

        # the piece of code below sorts the roomie requesters 
        # by their id since the association table 'roomies' has no date_joined 
        # field but only the two ids of the two users who are roomies 
        # ......this is the only way i found to sort by the latest request
        r = sorted(requesters, key = lambda x: x.id)


    elif request_type == 'roomies':

        requesters = current_user.roomie_followers.union( current_user.is_roomies_with)

        roomie_type = 'roomies'

              

        # the piece of code below sorts the roomie requesters 
        # by their id since the association table 'roomies' has no date_joined 
        # field but only the two ids of the two users who are roomies 
        # ......this is the only way i found to sort by the latest request
        r = sorted(requesters, key = lambda x: x.id)

    return render_template("roomie/roomie-requests.html",requesters = requesters, r=r, request_type = request_type)







@roomie_blueprint.route('/polaroid-person/<email>', methods=['GET'])
@login_required
def polaroid_person(email):
    user = User.query.filter_by(email = email).first_or_404()
    p = user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))
    return render_template("roomie/polaroid-person.html", user = user,img = img)







# the route that renders the page to create anouncement post
@roomie_blueprint.route('/roomie-details', methods=['GET', 'POST'])
@login_required
def roomie_details():
    
    form = RoomieRegisterForm()

    if current_user.seeks_roomate:
        abort(403)


    # logic for other post fields
    if  request.method == 'POST' and form.validate() :
    # logic for uploading profile pic only
        #the request.files object intance
        religion = form.religion.data
        level = form.level.data
        based_in =  form.based_in.data
        budget = form.budget.data
     
        
        new_roomie = Roomie(
                religion = religion,
                level = level, 
                based =  based_in,
                budget =  budget,
                date_joined = datetime.utcnow(), 
                candidate = current_user)

        current_user.seeks_roomate = True

        db.session.add(new_roomie)
        db.session.commit()


        flash('Weldone!, henceforth those seeking a roomate will  see you', 'success')
        return redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))


            
    return render_template('roomie/roomie-details.html',  form = form, page_title = "Hello new roomie, we need the following info to proceed ", val = 'Add Me')







# the route that renders the page to create anouncement post
@roomie_blueprint.route('/roomie-details-update/<id>', methods=['GET', 'POST'])
@login_required
def roomie_details_update(id):
    

    basedForm = BasedForm()
    religionForm = ReligionForm()
    levelForm = LevelForm()

    roomie = Roomie.query.filter_by(user_id = id).first_or_404()

    



    if not current_user == roomie.candidate:
        abort(403)


    if not current_user.seeks_roomate:
        abort(403)


    # logic for other post fields
    if  request.method == 'POST' and basedForm.validate() :
    # logic for uploading profile pic only
        #the request.files object intance

        based_in =  BasedForm.based_in.data
           

        roomie.based_in = based_in

        db.session.commit()

        flash('CURRENT LOCATION UPDATED SUCESSFULLY ', 'success')
        return redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))


    if  request.method == 'POST' and religionForm.validate() :
    # logic for uploading profile pic only
        #the request.files object intance

        religion =  religionForm.religion.data
           

        roomie.religion = religion

        db.session.commit()

        flash('RELIGION UPDATED SUCESSFULLY ', 'success')
        return redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))


    if  request.method == 'POST' and levelForm.validate() :
    # logic for uploading profile pic only
        #the request.files object intance

        level =  levelForm.level.data
           

        roomie.level = level

        db.session.commit()

        flash('YOUR CURRENT LEVEL HAS BEEN UPDATED ', 'success')
        return redirect(url_for('roomie.find_a_roomie', page = 1, sort = 'normal'))



    



    elif request.method == 'GET':    
        religionForm.religion.data =   roomie.religion
        levelForm.level.data = roomie.level
        basedForm.based_in.data = roomie.based
        


            
    return render_template('roomie/roomie-details-update.html',basedForm =  basedForm, levelForm = levelForm, religionForm = religionForm,   page_title = "Update your Roomie Profile ", roomie = roomie, val = 'Update')





@roomie_blueprint.route('/delete-roomie/<email>', methods=['GET', 'POST'])
@login_required
def delete_roomie(email):
    user = User.query.filter_by(email = email).first_or_404()

    roomie = Roomie.query.filter_by(user_id = user.id).first_or_404()

    user.seeks_roomate = False
    db.session.delete(roomie)
    db.session.commit()

    flash('YOU ARE NO LONGER SEARCHING FOR A ROOMATE', 'success')
    return redirect(url_for('home.roomie'))







@roomie_blueprint.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()

    db.session.commit()

    user = User.query.filter_by(id = 5).first_or_404()


    # messages = current_user.messages_received.order_by(Message.timestamp.desc())
    roomies = current_user.roomie_followers.union( current_user.is_roomies_with)
    r = sorted(roomies, key = lambda x: x.id)


    my_sent_msgs = current_user.messages_received.filter_by(sender_id = 5).all()

    my_recieved_msgs = current_user.messages_sent.filter_by(recipient_id = 5).all()


    # qry = Comments.query.filter_by(author = current_user).all()
    # qry = user in roomies.all()
    # qry = roomies.all()
    # qry = user

   

    return render_template('roomie/messages.html', msgs = messages, r = r, my_sent_msgs =my_sent_msgs, my_recieved_msgs = my_recieved_msgs)








@roomie_blueprint.route('/send_message/<int:recipient_id>', methods=['GET', 'POST'])
@login_required
def send_message(recipient_id):

    current_user.last_message_read_time = datetime.utcnow()
    # current_user.last_notifications_read_time = datetime.utcnow()
    db.session.commit()

    user = User.query.filter_by(id = recipient_id).first_or_404()



    if not (current_user.is_following_roomie(user) or user.is_following_roomie(current_user) ):
        abort(403)



    try:
        old_message_read_time = Specific_Message_Read_Time.query.filter_by(messages_sender = user).first()
        old_message_read_time.last_read_time =  datetime.utcnow()
        db.session.commit()
        
    except AttributeError :
        pass


    
    form = MessageForm()
 

    sender_msg = db.session.query(Message).filter(Message.sender_id == user.id, Message.recipient_id == current_user.id)
    my_msg = db.session.query(Message).filter(Message.sender_id == current_user.id, Message.recipient_id == user.id )

    all_msgs = sender_msg.union(my_msg).order_by(Message.timestamp.asc())





    added_specific_message = Specific_Message_Read_Time.query.filter_by(messages_sender = user).first()


    if request.method == 'POST' and form.validate():

        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)


        # adding a the new time the messages of a specific user were read
        new_specific_msg_time = Specific_Message_Read_Time(messages_sender = user)

        
        if added_specific_message:
            # print('\n\n\n-------------------------')
            # print('meesage was found')
            # print(added_specific_message)
            # print('\n\n\n-------------------------')
            db.session.delete(added_specific_message)
            db.session.add( new_specific_msg_time)
            db.session.commit()

        else:
            # print('\n\n\n-------------------------')
            # print('meesage not found')
            # print('\n\n\n-------------------------')
            db.session.add( new_specific_msg_time)
            db.session.commit()


        db.session.add(msg)

        # add notifivstion to recipient
        user.add_notification('unread_message_count_from_roomie_section', user.new_messages())
        db.session.commit()

        flash(('Your message has been sent.'))
        
        return redirect(request.url)

    return render_template('roomie/send-messages.html',form=form, recipient = user, msgs = all_msgs)









