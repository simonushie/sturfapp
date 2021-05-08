from flask import Blueprint, session, render_template,redirect,url_for,request,flash,redirect,current_app
from flask_security import login_required, current_user,logout_user
from flask_security.forms import LoginForm,RegisterForm
from app.models import User, Notification, Post
from app import db 
from flask_security.utils import hash_password, verify_and_update_password
from app.forms import MoreAboutForm,BirthDayForm,LikesForm,DislikesForm, PostForm, CaptionForm, EventForm, PhoneForm, PhotoForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import secrets
import os
from datetime import datetime
from PIL import Image
import json


from flask import jsonify




index_blueprint = Blueprint('home', __name__, 
    static_folder='static', static_url_path = '/static')



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])



# UPLOAD  PICTURE FUNTIONS

# funtion to check if the uploaded file is in the  allowed file extenion list
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# funtion that simply returns the file extenion 
def file_ext(filename):
    return str(filename.rsplit('.', 1)[1].lower()) 

# funtion prints the current time of posting in the format -- 'Saturday 17 October 2020'
def current_time():
    return str(datetime.now().strftime("%A %d %B %Y"))











@index_blueprint.route('/view-notifications')
@login_required
def notifications():
    notifications = current_user.new_notifications()

    return render_template("home/notifications.html", notifications = notifications)








@index_blueprint.route('/',methods=['GET']) 
def index():
    return render_template("home/splash.html")


@index_blueprint.route('/general',methods=['GET', 'POST'])  
def general():

    query = request.get_json() or {}

    posts = {}
    post_value = ''

    if current_user.is_authenticated:

        post_value = 'followed'
        posts = current_user.ordered_followed_posts().paginate(per_page = 1000)

    if current_user.is_authenticated and current_user.has_no_followed_posts():
        post_value = 'normal'
        posts = Post.query.join(User).order_by(User.paid.desc()).order_by(Post.date_posted.desc()).paginate( per_page = 10000  )


    try:
        action_type = query['action_type']

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass

    if request.method == 'POST' and action_type == 'sections' :

        return render_template("home/general-sections.html")


    elif request.method == 'POST' and action_type == 'feed' :

        return render_template("home/general-followed-posts.html", posts = posts, post_value = post_value )


    elif request.method == 'POST' and action_type == 'requests' :

        roomies = current_user.roomie_requesters

        requesters = sorted(roomies, key = lambda x: x.id)

        return render_template("home/general-requests.html", requesters = requesters)




    return render_template("home/general.html", posts = posts, post_value = post_value )





@index_blueprint.route('/vip',methods=['GET'])  
def vip():
    return render_template("home/vip.html")



@index_blueprint.route('/what_more',methods=['GET'])  
def what_more():
    return render_template("home/what_more.html")





@index_blueprint.route('/accept_terms/<email>/<string:answer>',methods=['POST']) 
@login_required 
def terms(email,answer):
    user = User.query.filter_by(email = email).first_or_404()
    user.has_aceepted_terms_and_conditions = bool(answer)
    db.session.commit()
    
    return redirect(url_for('home.general'))






@index_blueprint.route('/feed',methods=['GET'])  
def feed():
    return render_template("home/feed-section.html")





@index_blueprint.route('/sections',methods=['POST'])  
def sections():
    query = request.get_json() or {}

    try:
        action_type = query['action_type']

        print('\n', json.dumps(query) )
        
    except KeyError:
        pass

    # if request.method == 'POST' and post_type == 'Lost Items' :

    return render_template("home/feed-section.html")




@index_blueprint.route('/phone_visibility',methods=['POST']) 
@login_required 
def phone_visibility():

    query = request.get_json() or {}

    # print('\n', json.dumps(query) )

    try:
        user_id = query['user_id']

        phone_visibility = query['phone_visibility']

        # print('\n', json.dumps(query) )

        # print('\n', phone_visibility )
        
    except KeyError:
        pass

    info = 'nothing'

    user = User.query.get_or_404(user_id)


    if phone_visibility and phone_visibility == 'True':
        user.allows_phone_number_to_be_seen = True
        db.session.commit()
        info = ' Your number is now visible to everyone '

    elif phone_visibility and phone_visibility == 'False':
       
        info = ' Only you can see your number from now on'
        user.allows_phone_number_to_be_seen = False
        db.session.commit()

        
    return render_template("home/information.html",info = info )







@index_blueprint.route('/email_visibility',methods=['POST']) 
@login_required 
def email_visibility():

    query = request.get_json() or {}

    # print('\n', json.dumps(query) )

    try:
        user_id = query['user_id']

        email_visibility = query['email_visibility']

        # print('\n', json.dumps(query) )

        # print('\n', email )
        
    except KeyError:
        pass



    info = 'nothing'

    user = User.query.get_or_404(user_id)


    if email_visibility == 'True':
        user.allows_email_to_be_seen = True
        db.session.commit()
        info = ' Your email is now visible to everyone '

    elif email_visibility == 'False':
        print('block entered')
        info = ' Only you can see your email from now on'
        user.allows_email_to_be_seen = False
        db.session.commit()
        
    return render_template("home/information.html",info = info )





#################################
#### USER AND PROFILE ROUTES ####
#################################


@index_blueprint.route('/user/<email>',methods=['GET'])
def user(email):
    user = User.query.filter_by(email = email).first_or_404()
    p = user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))
    return render_template("home/user-template.html", user = user, img = img)












@index_blueprint.route('/profile/<id>',methods=['GET','POST'])
@login_required
def profile(id):
    p = current_user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))
    user = User.query.get_or_404(id)


    return render_template("home/profile.html", user=user, img = img)
    



@index_blueprint.route('/view-profile-pic/<int:id>',methods=['GET','POST'])
@login_required
def view_profile(id):
    count = request.args.get('count')

    # print(count)

    p = current_user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))
    user = User.query.get_or_404(id)


    if user != current_user:
        abort(403)


    photoForm = PhotoForm(CombinedMultiDict((request.files, request.form)))

    # logic for pic upload fields
    if  request.method == 'POST' and photoForm.validate() :
    # logic for uploading profile pic only
    #the request.files object intance using flaskform
        file = photoForm.photo.data
     
        #generate random string 8 digits long
        random_hex = secrets.token_hex(5)


        # check if the post request has the file part
        if not file:
            flash('NO PHOTO CHOSEN', 'error')
            return redirect(request.url)

        # check if the post request has the file part
        elif not  allowed_file(file.filename):
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg FILES ONLY', 'error')
            return redirect(request.url)

     
        # the following if block performs all the required processing on the file
        #and its name after validating its name

        if file and allowed_file(file.filename) and file.filename != '':
            split_file_name = os.path.splitext(file.filename)
            name_list = list(split_file_name)
            ex = str(file_ext(file.filename))
            secure = secure_filename(file.filename)

            #funtion to generate random name
            def random_name(filename):
                random_hex = str(secrets.token_hex(8))
            #the return statement below returns a random name for each file with different parameters separated by underscores 
                return   current_user.first_name + '_' + current_user.last_name + '_' + name_list[0] + '__' + random_hex + '__' + current_time() + '.' + ex


            #the name of the file gets assigned to the randomly generated file name 
            filename  = random_name(file.filename)
          
            uploads_path = os.path.join(current_app.root_path, 'static/profile_pics/uploads', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (250,250)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the user database along with other form data
            

            user.image_file = filename
            db.session.commit()


            flash('POST PHOTO UPDATED', 'success')
            return redirect(request.url)

    elif request.method == 'GET':
        photoForm.photo.data = user.image_file




    pic_list = []
    for i in range(2, 11):
        pic_list.append(str(i))




    
    return render_template("home/view-profile.html", user=user, img = img, photoForm = photoForm, pic_list = pic_list, count = count )











@index_blueprint.route('/view-profile-pic/load_more_avatars',methods=['GET','POST'])
@login_required
def load_more_avatars():

    query = request.get_json() or {}

    try:
        count = int(query['count'])

        print('\n', json.dumps(query) )
        
    except KeyError:
        pass


    pic_list = []

    for i in range(2, int(count + 10) ):
        pic_list.append(str(i))




# when its at 40 display only the remaining two
    if count == 40:

        pic_list = []

        for i in range(2, int(count + 2) ):
            pic_list.append(str(i))

        count = int(count) + 2




    else:
        count = int(count) + 10

    
    return render_template("home/view-profile-avatar-section.html", pic_list = pic_list, count = count )









@index_blueprint.route('/edit-profile/<email>', methods=['GET', 'POST'])
@login_required
def edit_profile(email):
    Caption = CaptionForm(request.form)
    moreAbout = MoreAboutForm(request.form)
    birthDay = BirthDayForm(request.form)
    likesform = LikesForm(request.form)
    dislikesform = DislikesForm(request.form)
    phoneform = PhoneForm(request.form)


# logic for caption field only
    if request.method == 'POST' and Caption.validate() :
        user = User.query.filter_by(email = email).first_or_404()
        user.caption = Caption.caption.data.lower()
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR CAPTION', 'success')
        return redirect(request.url)

# logic for moreAbout field only
    if request.method == 'POST' and moreAbout.validate() :
        user = User.query.filter_by(email = email).first_or_404()
        user.more_about = moreAbout.more_about.data.lower()
        db.session.commit()
        flash('SUCESSFULLY UPDATED MORE ABOUT SECTION', 'success')
        return redirect(request.url)

# logic for birthDay field only
    if request.method == 'POST' and birthDay.validate() :
        user = User.query.filter_by(email = email).first_or_404()

        day = str(birthDay.day.data)
        month = str(birthDay.month.data)
        year =  str(birthDay.year.data)

        user.birth_day = day + ' ' + month + ' ' + year


        db.session.commit()
        flash('SUCESSFULLY UPDATED YOUR BIRTHDAY ', 'success')
        return redirect(url_for('home.edit_profile', email = current_user.email))

# logic for likes field only        
    if request.method == 'POST' and likesform.validate() :
        user = User.query.filter_by(email = email).first_or_404()
        user.likes = likesform.likes.data.lower()
        db.session.commit()
        flash('SUCESSFULLY UPDATED YOUR LIKES ', 'success')
        return redirect(url_for('home.edit_profile', email = current_user.email))

# logic for dislikes field only
    if request.method == 'POST' and dislikesform.validate() :
        user = User.query.filter_by(email = email).first_or_404()
        user.dislikes = dislikesform.dislikes.data.lower()
        db.session.commit()
        flash('SUCESSFULLY UPDATED YOUR DISLIKES', 'success')
        return redirect(url_for('home.edit_profile', email = current_user.email))


# logic for dislikes field only
    if request.method == 'POST' and phoneform.validate() :
        user = User.query.filter_by(email = email).first_or_404()
        user.phone = phoneform.phone.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED YOUR PHONENUMBER', 'success')
        return redirect(url_for('home.edit_profile', email = current_user.email))




# logic for uploading profile pic only
    if request.method == 'POST':
        user = User.query.filter_by(email = email).first_or_404()
        
        #the request.files object intance
        file = request.files['file']
        #generate random string 8 digits long
        random_hex = secrets.token_hex(5)




        # check if the post request has the file part
        if not file:
            flash('NO FILE CHOSEN', 'error')
            return redirect(request.url)

        # check if the post request has the file part
        elif not  allowed_file(file.filename):
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg ONLY', 'error')
            return redirect(request.url)


        

        
        # the following if block checks if user does 
        # not select file and therfore filename  is empty 
        # so the browser does nothing
        if file and allowed_file(file.filename) and file.filename != '':
            split_file_name = os.path.splitext(file.filename)
            name_list = list(split_file_name)
            ex = str(file_ext(file.filename))
            secure = secure_filename(file.filename)

            #funtion to generate random name
            def random_name(filename):
                random_hex = str(secrets.token_hex(8))
            #the return statement below returns a random name for each file with different parameters separated by underscores 
                return   current_user.first_name + '_' + current_user.last_name + '_' + name_list[0] + '__' + random_hex + '__' + current_time() + '.' + ex


            #the name of the file gets assigned to the randomly generated file name 
            filename  = random_name(file.filename)
          
            uploads_path = os.path.join(current_app.root_path, 'static/profile_pics/uploads', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (500,500)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the database
            user.image_file = filename
            db.session.commit()


            # print ('first element of the name_list is -->', name_list[0])
            # print ('the scrapped file extension is -->', ex)
            # print ( 'new randomly generated filename is -->', filename)

            flash('PROFILE PICTURE UPDATED SUCESSFULLY', 'success')
            return redirect(request.url)
        
    return render_template('home/edit_profile.html', moreAbout = moreAbout, birthDay = birthDay, likesform = likesform, dislikesform = dislikesform, Caption = Caption, phoneform = phoneform )










@index_blueprint.route('/set-avatar/<id>/<img>', methods=['GET', 'POST'])
@login_required
def set_avatar(id,img):
    user = User.query.get_or_404(id)
    user.image_file = img
    db.session.commit()
    flash('AVATAR UPDATED SUCESSFULLY', 'success')   
    return redirect(url_for('home.profile', id = current_user.id))



#############
#############
#### END ####
#############
#############
















@index_blueprint.route('/light-sturf',methods=['GET'])
@login_required  
def light():
    return render_template("home/light-sturf.html")



                 


@index_blueprint.route('/buy-sturf',methods=['GET'])
@login_required  
def buy():
    return render_template("home/buy-sturf.html")





@index_blueprint.route('/recharge-and-bills',methods=['GET'])
@login_required  
def recharge():
    return render_template("home/recharge-and-bills.html")
 




@index_blueprint.route('/rent-sturf',methods=['GET'])
@login_required  
def rent():
    return render_template("home/rent-sturf.html")























###########################
#### POST STURF ROUTES ####
###########################


@index_blueprint.route('/post-sturf',methods=['GET'])
@login_required  
def post_sturf():
    return render_template("home/post-sturf.html")





#############
#############
#### END ####
#############
#############






















#############################
#### ROOMIE STURF ROUTES ####
#############################


@index_blueprint.route('/roomie-sturf',methods=['GET'])
@login_required  
def roomie():
    return render_template("home/roomie-sturf.html")





#############
#############
#### END ####
#############
#############






