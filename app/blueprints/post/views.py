from flask import Blueprint, session, render_template,redirect,url_for,request,flash,current_app, abort,jsonify
from flask_security import login_required, current_user,logout_user
from app import db 
from app.models import  Post, User, Comments, Viewed_Posts, Reported_Post,claimers, Claimers_messages, new_claimers, Claimers_Specific_Message_Read_Time
from app.forms import PostForm, EventForm , TitleForm, ContentForm, PhotoForm, VenueForm, BirthDayForm, LinkForm, CommentForm, LostForm, SearchingForm, ClaimerForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import secrets
import os
from datetime import datetime
from PIL import Image
import json
# import flask_whooshalchemy as wa




post_blueprint = Blueprint('post', __name__, 
    static_folder='static', static_url_path = '/static')






def cleaner(x):
    return list(dict.fromkeys(x))



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

















@post_blueprint.route('/',methods=['GET'])
@login_required 
def index():
    return render_template("post/post.html")






@post_blueprint.route('/test',methods=['GET'])
@login_required 
def test():
    return render_template("post/index.html")





@post_blueprint.route('/claim-item/<int:post_id>/<int:claimer_id>',methods=['GET','POST'])
@login_required 
def claim_item(post_id,claimer_id):

    post  = Post.query.get_or_404(post_id)
    claimer = User.query.get_or_404(claimer_id)

    if post.author == claimer:   
        abort(403)


    if current_user.has_tried_to_claim_post(post.id):
        flash(' sorry, you\'ve already tried to claim this item ')
        abort(403)

    form = ClaimerForm()

    if request.method == 'POST' and form.validate() :


        file = form.photo.data
        # claimer_profile_pic  =  form.photo.data

        #generate random string 8 digits long
        random_hex = secrets.token_hex(5)


        # check if the post request has the file part
        if not file:
            flash('NO PHOTO CHOSEN', 'error')
            return redirect(request.url)

        # check if the post request has the file part
        elif not  allowed_file(file.filename):
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg ONLY', 'error')
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
          
            uploads_path = os.path.join(current_app.root_path, 'static/claimers', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (250,250)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the post database along with other form data
            




            claimer_name  =  claimer.first_name + " " + claimer.last_name
            item_category  =  post.item_category
            email  =  claimer.email
            item_desription  =  form.content.data 
            post_id  =  post_id
            author_id  =  post.author.id
            claimer_id  =  claimer_id

            new_claim = claimers(
            claimer_profile_pic  =  filename,
            claimer_name  =  claimer_name,
            item_category  =  item_category,
            email  =  email,
            item_desription  =  item_desription,
            post_id  =  post_id,
            author_id  =  author_id,
            claimer_id  =  claimer_id
                        )


            db.session.add(new_claim)

            claimer.follow_finder(post.author)

            db.session.commit()


            flash('we will notify the author of this post about your claim  ', 'success')
            return redirect(url_for('post.post_view_page', post_id = post_id) ) 




    return render_template("post/claimer-details.html", form = form, post = post, claimer = claimer, val = "submit to item finder")

















@post_blueprint.route('/claim-attempts', methods=['GET','POST'])
@login_required  
def claim_attempts():

    page = request.args.get('page', 1, type = int)

    claim_attempts = claimers.query.filter_by(author_id = current_user.id).order_by(claimers.last_interaction_time.asc()).paginate(page = page, per_page = 10000  )

    posts = claim_attempts

    # print(claimers.query.filter_by(author_id = current_user.id).order_by(claimers.date_of_application.desc()).all())
    
    return render_template("post/claimer_list.html", posts = posts, page = page)
 








@post_blueprint.route('/my_claim_attempts', methods=['GET','POST'])
@login_required  
def my_claim_attempts():

    query = request.get_json() or {}

    try:

        page = int(query['page'])

        post_type = query['post_type']

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass


    val = ""

    if request.method == 'POST' and post_type == 'mine' :

        val = "mine"

        my_claim_attempts = claimers.query.filter_by(claimer_id = current_user.id).order_by(claimers.last_interaction_time.asc()).paginate(page = page, per_page = 10000  )

    
        posts = my_claim_attempts

        # print(posts)



    if request.method == 'POST' and post_type == 'others' :

        val = "others"

        claim_attempts = claimers.query.filter_by(author_id = current_user.id).order_by(claimers.last_interaction_time.asc()).paginate(page = page, per_page = 10000  )
    

        posts = claim_attempts
    
    return render_template("post/claimer_list_section.html", val =val, posts = posts, page = page)
 






# @post_blueprint.route('/claimer_message_list', methods=['GET','POST'])
# @login_required  
# def claimer_message_list():

#     page = request.args.get('page', 1, type = int)

#     messaged_users = current_user.claiming_followers.union(current_user.followed_claimers).all()

#     one = claimers.query.filter_by(author_id = current_user.id)
#     two = claimers.query.filter_by(claimer_id = current_user.id)

#     tad = one.union(two)



#     sub = claimers.query.join(Claimers_messages, (Claimers_messages.recipient_id == current_user.id) )

#     dom = claimers.query.join(Claimers_messages, (Claimers_messages.sender_id == current_user.id) )

#     tag = dom.union(sub).filter(Claimers_messages.recipient_id == current_user.id).order_by(claimers.last_interaction_time.asc()).all()

#     posts = tad.all()

#     return render_template("post/messagers_list.html", posts = posts, page = page)
 






@post_blueprint.route('/chat_with_claimers', methods=[ 'POST'])
@login_required  
def chat_with_claimers():


    query = request.get_json() or {}

    try:
        chat_body = query['chat_body']

        post_id = int(query['post_id'])

        recipient = int(query['recipient'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass

    user = User.query.get_or_404(recipient)

    reciever = claimers.query.filter_by(claimer_id = recipient).first()
    # print(reciever)




    # get the users last read time and update it
    try:
        old_message_read_time = Claimers_Specific_Message_Read_Time.query.filter_by(messages_sender = user).first()
        old_message_read_time.last_read_time =  datetime.utcnow()
        db.session.commit()
        
    except AttributeError :
        pass



    # adding the previous time the messages of a specific user was read
    added_specific_message = Claimers_Specific_Message_Read_Time.query.filter_by(messages_sender = user).first()


    # adding a new message
    msg = Claimers_messages(
                message_body = chat_body,
                post_id = post_id,
                claimer_sender = current_user,
                Claimer_recipient = user
                )


    # adding the new time the messages of a specific user was read
    new_specific_msg_time = Claimers_Specific_Message_Read_Time(

                messages_sender = user,
                post_id = post_id

                )



    if added_specific_message:
        db.session.delete(added_specific_message)
        db.session.add(new_specific_msg_time)
        db.session.commit()

    else:
        db.session.add( new_specific_msg_time)
        db.session.commit()



    db.session.add(msg)




# update the last interaction time of the reciever of the message

    streamlined_user = db.session.query(claimers).filter_by(claimer_id = recipient)

    post_id_of_msg = db.session.query(claimers).filter_by(post_id = post_id )

    reciever_of_msg = streamlined_user.union(post_id_of_msg).first()

    reciever_of_msg.last_interaction_time = datetime.utcnow()

    db.session.commit()




# get all the messages of the sender and the reciever

    sender_msg = db.session.query(Claimers_messages).filter(Claimers_messages.sender_id == current_user.id, Claimers_messages.recipient_id  == user.id)
    my_msg = db.session.query(Claimers_messages).filter(Claimers_messages.sender_id == user.id , Claimers_messages.recipient_id  == current_user.id )

    comments = sender_msg.union(my_msg).filter(Claimers_messages.post_id == post_id ).order_by(Claimers_messages.date_of_message.asc())

    # print(comments.all())
    # comments = Claimers_messages.query.filter_by(claimer_sender = current_user, Claimer_recipient  = user ).order_by(Claimers_messages.date_of_message.desc()) 

    post = Post.query.get_or_404(post_id)

    return render_template("post/post-view-page-claimer-section.html", post = post, comments = comments)











# route to view each post individually
@post_blueprint.route('/view-claimer-page/<int:post_id>/<int:claimer_id>', methods=['GET', 'POST'])
@login_required  
def view_claimer_page(post_id, claimer_id):

    if claimer_id == current_user.id:
        abort(403)



    claimer_man = claimer_id

    # print(post_id)

    found_item = Post.query.get_or_404(post_id)

    one = db.session.query(claimers).filter( claimers.claimer_id == claimer_id, claimers.author_id == current_user.id)

    two = db.session.query(claimers).filter(claimers.claimer_id == current_user.id , claimers.author_id == claimer_id )


    # sender_msg.union(my_msg).order_by(Claimers_messages.date_of_message.asc())

    post = one.union(two).filter(claimers.post_id == post_id).first()

    # print(post)

    user = User.query.get_or_404(claimer_id)



    if not user.is_following_finder_or_is_the_finder(current_user):
        abort(403)




# update the last read time of the particular user and the particular post
    actual_msg = db.session.query(Claimers_Specific_Message_Read_Time).filter(Claimers_Specific_Message_Read_Time.message_sender_id == user.id)

    post_id_of_msg =  db.session.query(Claimers_Specific_Message_Read_Time).filter(Claimers_Specific_Message_Read_Time.post_id == post_id)

    specifc_msg = actual_msg.union(post_id_of_msg).all()
    

    print(specifc_msg)

    try:
        specifc_msg.last_read_time = datetime.utcnow()
        db.session.commit()

    except AttributeError:
        pass
    




    sender_msg = db.session.query(Claimers_messages).filter(Claimers_messages.sender_id == current_user.id, Claimers_messages.recipient_id  == user.id)
    my_msg = db.session.query(Claimers_messages).filter(Claimers_messages.sender_id == user.id , Claimers_messages.recipient_id  == current_user.id )

    comments = sender_msg.union(my_msg).filter(Claimers_messages.post_id == post_id ).order_by(Claimers_messages.date_of_message.asc())


    return render_template("post/view-claimer-page.html", test = test, claimer_man = claimer_man, comments = comments, post = post, found_item = found_item, user =user)



















#main page with all the posts


@post_blueprint.route('/posts-page',methods=['GET','POST'])
@login_required  
def post():

    page = request.args.get('page', 1, type = int)
    post_type = request.args.get('post_type')


    query = request.get_json() or {}

 
    post_value = 'normal'


    posts = Post.query.join(User).order_by(User.paid.desc()).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 10000  )


    return render_template("post/post-page-jq.html", posts = posts, query = query, post_value = post_value, page = page)
 








@post_blueprint.route('my-posts/sort_your_posts', methods=['POST'])
@login_required
def sort_your_posts():



    query = request.get_json() or {}

    try:
        post_type = query['post_type']

        page = int(query['page'])  

        print('\n', json.dumps(query) )
        
    except KeyError:
        pass



    post_value = 'normal'



    if request.method == 'POST' and post_type == 'Lost Items' :
        # print('got it, its lost_and_searching')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'lost_and_searching'
        item_list = []
        

        for each in LostForm.x :
            item_list.append(str(each[0]))
        
        # item_list = item_list.sort()  



        # print(item_list)

        posts =  Post.query.filter_by(is_Lost_and_searching= True).filter_by(author = current_user).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 500  )



    elif request.method == 'POST' and post_type == 'Found Items' :
        # print('got it, its lost_and_searching')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 
        item_list = []

        

        for each in LostForm.x :
            item_list.append(str(each[0]))
            

        # item_list = item_list.sort()
        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'lost_and_found'

        # print(post_value)

        posts =  Post.query.filter_by(is_Lost_and_found= True).filter_by(author = current_user).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 500  )





    elif request.method == 'POST' and post_type == 'Events' :
        # print('got it, its normal')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 
        item_list = []

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'normal'

        # print(post_value)

        posts = Post.query.filter_by(is_event = True ).filter_by(author = current_user).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 500  )



    elif request.method == 'POST' and post_type == 'Regular Posts' :
        # print('got it, its normal')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 
        item_list = []

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'normal'

        # print(post_value)

        posts = Post.query.filter_by(is_event = False ).filter_by(author = current_user).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 500  )



    elif request.method == 'POST' and post_type == 'All' :
        # print('got it, its normal')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 
        item_list = []

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'normal'

        # print(post_value)

        posts = Post.query.filter_by(author = current_user).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 500  )







    return render_template("post/my-posts-section.html", user = user, post = posts )










@post_blueprint.route('/posts-page-jq-update',methods=['GET','POST'])
@login_required  
def post_jq_update():


    query = request.get_json() or {}

    try:
        post_type = query['post_type']

        page = int(query['page'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass



    post_value = 'normal'


    # posts = Post.query.join(User).order_by(User.paid.desc()).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 10  )

    if request.method == 'POST' and post_type == 'followed' :
        # flash('{}'.format(post_type), 'success')
        # print('got it, its followed')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 

        item_list = []

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'followed'

        # print(post_value)

        posts = current_user.followed_posts().paginate(page = page, per_page = 50  )



    elif request.method == 'POST' and post_type == 'lost_and_searching' :
        # print('got it, its lost_and_searching')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'lost_and_searching'
        item_list = []
        

        for each in LostForm.x :
            item_list.append(str(each[0]))
        
        # item_list = item_list.sort()  



        # print(item_list)

        posts =  Post.query.filter_by(is_Lost_and_searching= True).join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 200  )



    elif request.method == 'POST' and post_type == 'lost_and_found' :
        # print('got it, its lost_and_searching')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 
        item_list = []

        

        for each in LostForm.x :
            item_list.append(str(each[0]))
            

        # item_list = item_list.sort()
        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'lost_and_found'

        # print(post_value)

        posts =  Post.query.filter_by(is_Lost_and_found= True).join(User).order_by(User.paid.asc()).paginate(page = page, per_page = 200  )




    elif request.method == 'POST' and post_type == 'normal' :
        # print('got it, its normal')

        recieved_page = query['page']  
        recieved_post_type = query['post_type'] 
        item_list = []

        # print('\n',  recieved_page)

        # print('\n', recieved_post_type  )


        post_value = 'normal'

        # print(post_value)

        posts = Post.query.join(User).order_by(User.paid.desc()).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 1000  )



    return render_template("post/post-page-jq-section.html", posts = posts, query = query, post_value = post_value, page = page, item_list = item_list)














@post_blueprint.route('/posts-lost-item-category',methods=['POST'] )
@login_required  
def post_lost_item_category():


    query = request.get_json() or {}

    try:
        item_category = query['item_type'] 

        page = int(query['page'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass


    if request.method == 'POST' and item_category != None :
        # print('got it, its followed')

        item_category = item_category

        # post_value = 'lost_and_searching'

        # print(item_category)

        item_list = []

        for each in LostForm.x :
            item_list.append(str(each[0]))


        posts = Post.query.filter_by(is_Lost_and_searching = True).filter_by(item_category = item_category ).join(User).order_by(User.paid.desc()).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 10  )


    return render_template("post/post-page-jq-small-content.html", posts = posts, query = query, page = page, item_list = item_list)








@post_blueprint.route('/posts-found-category',methods=['POST'] )
@login_required  
def post_found_item_category():


    query = request.get_json() or {}

    try:
        item_category = query['item_type'] 

        page = int(query['page'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass


    if request.method == 'POST' and item_category != None :
        # print('got it, its followed')

        item_category = item_category

        # post_value = 'lost_and_searching'

        # print(item_category)

        item_list = []

        for each in LostForm.x :
            item_list.append(str(each[0]))


        posts = Post.query.filter_by(is_Lost_and_found = True).filter_by(item_category = item_category ).join(User).order_by(User.paid.desc()).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 10  )


    return render_template("post/post-page-jq-small-content.html", posts = posts, query = query, page = page, item_list = item_list)








# route to report a post 
@post_blueprint.route('/report-post/<int:post_id>/<report_type>', methods=['GET', 'POST'])
@login_required  
def report_post(post_id, report_type):

    post = Post.query.get_or_404(post_id)

    reports = post.report_count()


# check if the number of reports is more than 10 and then delete the post 
    if reports >= 29:
        db.session.delete(post)
        db.session.commit()
        flash(' we\'ve already deleteed that post because it was reported too many times  ')






    if current_user.has_reported_post(post.id):
        flash(' you\'ve already reported this post ')

    else:
        new_report = Reported_Post(
                    post_id = post_id,
                    reporter = current_user,
                    report_type = report_type
                    )


        if report_type == "Inappropriate" :
            reported_post = Reported_Post.query.filter_by(post_id = post_id, user_id = current_user.id).first_or_404()
            
            if reported_post.inappropriate_count is None:
                reported_post.inappropriate_count = 1
            else:
                reported_post.inappropriate_count += 1





        elif report_type == "Offensive" :
            reported_post = Reported_Post.query.filter_by(post_id = post_id, user_id = current_user.id).first_or_404()
            
            if reported_post.offensive_count is None:
                reported_post.offensive_count = 1
            else:
                reported_post.offensive_count += 1



        elif report_type == "Hate_speech" :
            reported_post = Reported_Post.query.filter_by(post_id = post_id, user_id = current_user.id).first_or_404()
            
            if reported_post.hate_speech_count is None:
                reported_post.hate_speech_count = 1
            else:
                reported_post.hate_speech_count += 1



        elif report_type == "Inaccurate" :
            reported_post = Reported_Post.query.filter_by(post_id = post_id, user_id = current_user.id).first_or_404()
            
            if reported_post.inaccurate_info_count is None:
                reported_post.inaccurate_info_count = 1
            else:
                reported_post.inaccurate_info_count += 1


    # if not current_user.has_reported_post(post.id) and report_type == "Inappropriate" :
    #     reported_post = Reported_Post.query.filter_by(post_id = post_id, user_id = current_user.id).first_or_404()
    #     reported_post.inappropriate_count += 1




        # current_user.view(post)

        db.session.add(new_report)
        db.session.commit()

        flash(' we\'ve received your complaint and the appropriate action will be taken, thanks! ', 'success')



    return redirect(url_for('post.post_view_page', post_id = post_id) ) 







# route to view each post individually
@post_blueprint.route('/post-view-page/<int:post_id>', methods=['GET', 'POST'])
@login_required  
def post_view_page(post_id):

    commentForm = CommentForm()


    post = Post.query.get_or_404(post_id)



    if current_user.has_viewed_post(post.id):
        pass

    else:
        post_view = Viewed_Posts(
                    post_id = post_id,
                    viewer = current_user
                    )

        # current_user.view(post)

        db.session.add(post_view)
        db.session.commit()


    # logic for CONTENT field only
    if request.method == 'POST' and commentForm.validate() :

        comment_body = commentForm.comment.data
        post_id = post_id

        comment = Comments(
                    comment_body = comment_body,
                    post_id = post_id,
                    commentor = current_user
                    )

        db.session.add(comment)
        db.session.commit()
        flash('COMMENT ADDED', 'success')
        return redirect(request.url)


    comments = Comments.query.filter_by(post_id = post_id).order_by(Comments.date_of_comment.asc()) 
    
    return render_template("post/post-view-page.html", post = post, commentForm = commentForm, comments = comments)













@post_blueprint.route('/add-comment', methods=[ 'POST'])
@login_required  
def add_comment():


    query = request.get_json() or {}

    try:
        comment_body = query['comment_body']

        post_id = int(query['post_id'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass

    comment = Comments(
                comment_body = comment_body,
                post_id = post_id,
                commentor = current_user
                )

    db.session.add(comment)
    db.session.commit()


    comments = Comments.query.filter_by(post_id = post_id).order_by(Comments.date_of_comment.asc()) 
    post = Post.query.get_or_404(post_id)
    return render_template("post/post-view-page-comment-section.html", post = post, comments = comments)












@post_blueprint.route('/delete-comment', methods=[ 'POST'])
@login_required  
def delete_comment():


    query = request.get_json() or {}

    try:
        comment_id = query['comment_id']

        post_id = query['post_id'] 

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass

    comment = Comments.query.get_or_404(comment_id)


    if comment.commentor != current_user:
        abort(403)


    db.session.delete(comment)
    db.session.commit()


    comments = Comments.query.filter_by(post_id = post_id).order_by(Comments.date_of_comment.desc()) 
    post = Post.query.get_or_404(post_id)
    
    return render_template("post/post-view-page-comment-section.html", post = post, comments = comments)




# route to follow a user
@post_blueprint.route('/follow-user', methods=['GET','POST'])
@login_required  
def follow_user():


    query = request.get_json() or {}

    try:
        email = query['email']

        post_id = int(query['post_id'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass


    u1 = current_user
    u2 = User.query.filter_by(email = email).first()
    post = Post.query.get_or_404(post_id)

    # this is so that a user cannot follow themselves
    if post.author == current_user:
        abort(403)


    u1.follow(u2)

    db.session.commit()

    return render_template("post/post-view-page-button-section.html", post = post )





# route to un-follow a user
@post_blueprint.route('/un-follow-user', methods=['GET','POST'])
@login_required  
def un_follow_user():


    query = request.get_json() or {}

    try:
        email = query['email']

        post_id = int(query['post_id'])  

        # print('\n', json.dumps(query) )
        
    except KeyError:
        pass


    u1 = current_user
    u2 = User.query.filter_by(email = email).first()
    post = Post.query.get_or_404(post_id)

    # this is so that a user cannot follow themselves
    if post.author == current_user:
        abort(403)


    u1.unfollow(u2)

    db.session.commit()

    return render_template("post/post-view-page-button-section.html", post = post )



   
 


#the page that simulates online payment that gives you the ability to post
@post_blueprint.route('/post-sturf-payment-page', methods=['GET', 'POST'])
@login_required  
def post_payment_page():
    if current_user.paid :
        abort(403)
        
    return render_template("post/post_sturf_payment.html")










#this route asks what kinda post you want to make so it knows what kinda form to give you
@post_blueprint.route('/post-type', methods=['GET', 'POST'])
@login_required  
def post_type():
    if not (current_user.paid or current_user.generic ):
        abort(403)


    return render_template("post/post-type.html")










#the route that simulates the proceessing of  an online payment that gives you the ability to post

@post_blueprint.route('/post-sturf-payment/<email>', methods=['GET', 'POST'])
@login_required  
def post_sturf_payment(email):
    user = User.query.filter_by(email = email).first_or_404()
    user.paid = True
    user.generic = False
    db.session.commit()
    flash (' YOU HAVE BEEN SUBSCRIBED TO VIP, ENJOY!', 'success')
    return redirect(url_for('post.post', post_type = 'normal', page = 1))





#the route that simulates the proceessing of  a free user, also gives you the ability to post

@post_blueprint.route('/post-sturf-generic/<email>', methods=['GET', 'POST'])
@login_required  
def post_sturf_generic(email):
    user = User.query.filter_by(email = email).first_or_404()
    user.generic = True
    user.paid = False
    db.session.commit()
    flash (' YOU HAVE BEEN REGISTERED AS A FREE USER, POST AT WILL!', 'success')
    return redirect(url_for('post.post', post_type = 'normal', page = 1))










@post_blueprint.route('/user-posts/<email>', methods=['GET'])
@login_required  
def user(email):

    user = User.query.filter_by(email = email).first_or_404()

    post = Post.query.filter_by(author = user).order_by(Post.date_posted.desc())

    post_count = Post.query.filter_by(author = user).all()


    p = user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))
    return render_template("post/user-posts.html", user = user, img = img, post = post,  post_count= post_count )






@post_blueprint.route('/my-posts/<int:id>', methods=['GET'])
@login_required
def my_posts(id):

    page = request.args.get('page', 1, type = int)


    user = User.query.get_or_404(id)

    post = Post.query.filter_by(author = user).order_by(Post.date_posted.desc())

    post_count = Post.query.filter_by(author = user).all()

    p = user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))


    item_list = []

    for each in LostForm.z :
        item_list.append(str(each[0]))



    return render_template("post/my-posts.html",item_list = item_list, user = user, img = img, post = post,  post_count= post_count, page = page )









# the route that renders the page to create anouncement post
@post_blueprint.route('/post/create/announcement', methods=['GET', 'POST'])
@login_required
def new_announcement():

    if not (current_user.paid or current_user.generic ):
        abort(403)
    #
    form = PostForm(CombinedMultiDict((request.files, request.form)))



    # logic for other post fields
    if  request.method == 'POST' and form.validate() :
    # logic for uploading profile pic only
        #the request.files object intance
        file = form.photo.data
        title = form.title.data.upper()
        content =  form.content.data.lower().lstrip()
     
        #generate random string 8 digits long
        random_hex = secrets.token_hex(5)


        # check if the post request has the file part
        if not file:
            flash('NO PHOTO CHOSEN', 'error')
            return redirect(request.url)

        # check if the post request has the file part
        elif not  allowed_file(file.filename):
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg ONLY', 'error')
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
          
            uploads_path = os.path.join(current_app.root_path, 'static/post_sturf', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (250,250)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the post database along with other form data
            

            post = Post(
                    image_file = filename,
                    title = title, 
                    content =  content, 
                    is_event =  False,
                    author = current_user)


            db.session.add(post)
            db.session.commit()


            flash('NEW POST ADDED', 'success')
            return redirect(url_for('post.post', page = 1 ,post_type = 'normal'))


            
    return render_template('post/post.html',  form = form, page_title = "create new post")















# the route that renders the page to create event post
@post_blueprint.route('/post/create/event', methods=['GET', 'POST'])
@login_required
def new_event():

    if not (current_user.paid or current_user.generic ):
        abort(403)

    #
    form = EventForm(CombinedMultiDict((request.files, request.form)))
    linkForm = LinkForm()



    # logic for other post fields
    if  request.method == 'POST' and form.validate() :
    # logic for uploading profile pic only
        #the request.files object intance
        file = form.photo.data
        title = form.title.data.upper()
        content =  form.content.data.lower().lstrip()
        venue = form.venue.data.lower()

        day = form.day.data
        month = form.month.data
        year = form.year.data


        date = day + ' ' + month + ' ' + year

        is_event = True






        #generate random string 8 digits long
        random_hex = secrets.token_hex(5)


        # check if the post request has the file part
        if not file:
            flash('NO PHOTO CHOSEN', 'error')
            return redirect(request.url)

        # check if the post request has the file part
        elif not  allowed_file(file.filename):
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg ONLY', 'error')
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
          
            uploads_path = os.path.join(current_app.root_path, 'static/post_sturf', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (250,250)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the post database along with other form data
            

            post = Post(
                    image_file = filename,
                    title = title, 
                    content =  content,
                    date =  date,
                    venue =  venue,
                    is_event =  is_event, 
                    author = current_user)

            db.session.add(post)
            db.session.commit()


            flash('NEW EVENT ADDED', 'success')
            return redirect(url_for('post.post', page = 1 ,post_type = 'normal'))


    # logic for link field only
    elif request.method == 'POST' and linkForm.validate() :
        post.link = linkForm.url.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR EVENT LINK', 'success')
        return redirect(request.url)

            
    return render_template('post/post-event.html', title = 'Create New Event', form = form, info = ' Add' , linkForm = linkForm)








# the route that renders the page to create event post
@post_blueprint.route('/post/create/lost_but_found', methods=['GET', 'POST'])
@login_required
def new_lost_but_found_item():

    if not (current_user.paid or current_user.generic ):
        abort(403)

    #
    form = LostForm(CombinedMultiDict((request.files, request.form)))
   


    # logic for other post fields
    if  request.method == 'POST' and form.validate() :
    # logic for uploading profile pic only
        #the request.files object intance
        file = form.photo.data
        item_name = form.item_name.data.upper()
        item_location =  form.item_location.data.lower()

        item_category =  form.item_category.data.lower()

        description = form.description.data.lower().lstrip()

        possession = form.possession.data

        if form.possession.data == "Yes" :
            possession = True

        elif form.possession.data == "No" :
            possession = False

        db.session.commit()

        is_Lost_and_found = True






        #generate random string 8 digits long
        random_hex = secrets.token_hex(5)


        # check if the post request has the file part
        if not file:
            flash('NO PHOTO CHOSEN', 'error')
            return redirect(request.url)

        # check if the post request has the file part
        elif not  allowed_file(file.filename):
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg ONLY', 'error')
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
          
            uploads_path = os.path.join(current_app.root_path, 'static/post_sturf', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (250,250)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the post database along with other form data
            

            post = Post(
                    image_file = filename,
                    title = item_name, 
                    content =  description,
                    item_category = item_category,
                    possession = possession,
                    venue =  item_location,
                    is_Lost_and_found =  is_Lost_and_found, 
                    author = current_user)

            db.session.add(post)
            db.session.commit()


            flash('THANK YOU FOR TAKING THE TIME TO POST THIS ITEM', 'success')
            return redirect(url_for('post.post', page = 1 ,post_type = 'normal'))



            
    return render_template('post/post-lost.html', title = 'Report A Found Item', form = form, info = ' Post')








# the route that renders the page to create event post
@post_blueprint.route('/post/create/lost_and_searching', methods=['GET', 'POST'])
@login_required
def new_lost_and_searching():

    if not (current_user.paid or current_user.generic ):
        abort(403)

    #
    form = SearchingForm(CombinedMultiDict((request.files, request.form)))
   



    if  request.method == 'POST' and form.validate() :

        item_name = form.item_name.data.upper()
        item_location =  form.item_location.data.lower()

        item_category =  form.item_category.data.lower()


        description = form.description.data.lower().lstrip()


        day = form.day.data
        month = form.month.data
        year = form.year.data


        date = day + ' ' + month + ' ' + year

        date = date

        is_Lost_and_searching = True



        post = Post(
                image_file = 'ic_error_48px.svg',
                title = item_name, 
                content =  description,
                date = date,
                item_category = item_category,
                venue =  item_location,
                is_Lost_and_searching =  is_Lost_and_searching, 
                author = current_user)



        db.session.add(post)
        db.session.commit()


        flash('WE WILL DISTRIBUTE THIS LOST ITEM TO EVERYONE', 'success')
        return redirect(url_for('post.post', page = 1 ,post_type = 'normal'))



            
    return render_template('post/post-searching.html', title = 'Report A Lost Item', form = form, info = ' Post')















@post_blueprint.route('/update_post_image/<int:post_id>',methods=['GET','POST'])
@login_required
def update_post_image(post_id):

    post = Post.query.get_or_404(post_id)
    img = url_for('static', filename='post_sturf/' + post.image_file )
    if post.author != current_user:
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
            flash('THE SELECTED FILE TYPE IS NOT ALLOWED, USE png OR jpg ONLY', 'error')
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
          
            uploads_path = os.path.join(current_app.root_path, 'static/post_sturf', filename)

            #the next four lines just resizes the image to the given dimensions e.g 125 by 125
            output_size = (250,250)
            i = Image.open(file)
            i.thumbnail(output_size)
            i.save(uploads_path)

            #save the newly generated filename to the post database along with other form data
            

            post.image_file = filename
            db.session.commit()


            flash('POST PHOTO UPDATED', 'success')
            return redirect(request.url)

    elif request.method == 'GET':
        photoForm.photo.data = post.image_file


    

    
    return render_template("post/update-post-image.html", post = post, img = img, photoForm = photoForm)
















# route to update each post individually
@post_blueprint.route('/post-announcement-update/<int:post_id>', methods=['GET', 'POST'])
@login_required  
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    titleForm = TitleForm()
    contentForm = ContentForm()
    linkForm = LinkForm()

    
    # logic for CONTENT field only
    if request.method == 'POST' and contentForm.validate() :
        post.content = contentForm.content.data.lower()
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR POST CONTENT', 'success')
        return redirect(request.url)


    # logic for TITLE field only
    elif request.method == 'POST' and titleForm.validate() :
        post.title = titleForm.title.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR POST TITLE', 'success')
        return redirect(request.url)


    # logic for link field only
    elif request.method == 'POST' and linkForm.validate() :
        post.link = linkForm.url.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR POST LINK', 'success')
        return redirect(request.url)






    

    elif request.method == 'GET':
        titleForm.title.data =   post.title
        contentForm.content.data = post.content
        linkForm.url.data = str(post.link)
     


    return render_template("post/post-announcement-update.html", post = post, page_title = "update your post", titleForm = titleForm, contentForm = contentForm, linkForm = linkForm)











# route to update each post individually
@post_blueprint.route('/post-event-update/<int:post_id>', methods=['GET', 'POST'])
@login_required  
def post_event_update(post_id):
    post = Post.query.get_or_404(post_id)
    post_type = 'event_update'
    
    if post.author != current_user:
        abort(403)
    form = EventForm(CombinedMultiDict((request.files, request.form)))
    linkForm = LinkForm()

    if  request.method == 'POST' and form.validate() :

        post.title = form.title.data.upper()
        post.content =  form.content.data.lower().lstrip()
        post.venue = form.venue.data.lower()

        day = form.day.data
        month = form.month.data
        year = form.year.data


        date = day + ' ' + month + ' ' + year

        post.date = date

          
        db.session.commit()


        flash('ALL CHANGES HAVE BEEN UPDATED', 'success')
        return redirect(request.url)



    # logic for link field only
    elif request.method == 'POST' and linkForm.validate() :
        post.link = linkForm.url.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR EVENT LINK', 'success')
        return redirect(request.url)
         

    elif request.method == 'GET':
        form.title.data =   post.title
        form.content.data = post.content
        form.venue.data = post.venue

        form.day.data = post.date.strftime("%d")
        form.month.data = post.date.strftime("%B")
        form.year.data = post.date.strftime("%Y")


        linkForm.url.data = str(post.link)

        if post.link is None:
            linkForm.url.data = "Add a URL if you wish"




    return render_template("post/post-event.html",title = "Update this event",  form = form, info = "Update", post_type = post_type, linkForm = linkForm)





















# route to delete each post individually
@post_blueprint.route('/post-event-delete/<int:post_id>', methods=['POST'])
@login_required  
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('YOUR POST HAS BEEN DELETED', 'success')
    return redirect(url_for('post.post'))








