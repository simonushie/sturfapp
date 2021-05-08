from flask import Blueprint, session, render_template,redirect,url_for,request,flash,current_app, abort

from flask_security import login_required, current_user,logout_user
from app import db 
from app.models import  User, E_commerce

from app.forms import  EventForm , TitleForm, ContentForm, VenueForm, BirthDayForm, \
LinkForm, PhoneForm, CommentForm, StudentForm, AdForm, TabletAdForm, MultiPhotoForm, WhatssapForm, AddressForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import secrets
import os
from datetime import datetime
from PIL import Image


buy_blueprint = Blueprint('buy', __name__, 
    static_folder='static', static_url_path = '/static')








ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


# UPLOAD  PICTURE FUNTIONS

# funtion to check if the uploaded file is in the  allowed file extenion list
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# funtion that simply returns the file extenion 
def file_ext(filename):
    return str(filename.rsplit('.', 1)[1].lower()) 

# funtion prints the current time of buying in the format -- 'Saturday 17 October 2020'
def current_time():
    return str(datetime.now().strftime("%A %d %B %Y"))





















    
@buy_blueprint.route('/buy-user-details', methods=['GET', 'POST'])
@login_required
def buy_user_details():
    
    studentform = StudentForm()

    whatssapForm = WhatssapForm()

    addressform = AddressForm()
  
    user = current_user

    if current_user.is_student:
        abort(403)



    if  request.method == 'POST' and studentform.validate() :

        if studentform.is_student.data == "Yes" :
            user.is_student = True

        elif studentform.is_student.data == "No" :
            user.is_student = False

        db.session.commit()



    if request.method == 'POST' and whatssapForm.validate() :
        user.whatssap_number = whatssapForm.phone.data
        db.session.commit()


    if request.method == 'POST' and addressform.validate() :
        user.address = addressform.address.data
        db.session.commit()



        flash('INFORMATION ADDED!', 'success')
        return redirect(url_for('buy.ads', page = 1, sort = 'normal'))


            
    return render_template('buy/buy-user-details.html', whatssapForm = whatssapForm,  addressform = addressform, studentform = studentform, page_title = "please help us with the following info ", val = 'Proceed')






#main page with all the buys

@buy_blueprint.route('/ads',methods=['GET'])
@login_required  
def ads():
    page = request.args.get('page', 1, type = int)
    sort = request.args.get('sort')
    filtering  =  request.args.get('filtering')
    # posts = Post.query.paginate(page = page, per_page = 10  )



    ads = E_commerce.query.join(User).order_by(User.paid.desc()).order_by(E_commerce.date_of_post.desc()).paginate(page = page, per_page = 10  )

    posts = ads    

    sort_value = 'normal'

    filt = filtering



    if sort == 'normal':
        sort_value = 'normal'
        posts = ads

    elif sort == 'phone':
        print('entered this ablock')
        phones = E_commerce.query.filter_by(ad_type = 'phone').join(User).order_by(User.paid.desc()).order_by(E_commerce.date_of_post.desc()).paginate(page = page, per_page = 10  )
        posts = phones
        sort_value = 'phone'

    elif sort == 'tablet':
            print('entered this bblock')
            sort_value = 'tablet'
            tablets = E_commerce.query.filter_by(ad_type = 'tablet').join(User).order_by(User.paid.desc()).order_by(E_commerce.date_of_post.desc()).paginate(page = page, per_page = 10  )
            posts = tablets

























    if filtering == 'cheapest':
        print('entered this vlock')
        val = str(sort)
        print(val)
        posts = E_commerce.query.filter_by(ad_type = val).join(User).order_by(User.paid.desc()).order_by(E_commerce.price.asc()).paginate(page = page, per_page = 10  )
        
        sort_value = val
        filt = 'cheapest'


    if filtering == 'most_expensive':
        print('entered this clock')
        val = str(sort)
        print(val)
        posts = E_commerce.query.filter_by(ad_type = val).join(User).order_by(User.paid.desc()).order_by(E_commerce.price.desc()).paginate(page = page, per_page = 10  )
        
        sort_value = val
        filt = 'most_expensive'

    


    return render_template("buy/ads.html", sort_value = sort_value, page = page, posts = posts, filt = filt )
 





# route to view each buy individually
@buy_blueprint.route('/ad-view-page/<int:ad_id>/<string:ad_type>', methods=['GET', 'POST'])
@login_required  
def ad_view_page(ad_id, ad_type):

    commentForm = CommentForm()

    ad = E_commerce.query.get_or_404(ad_id)

    similar_ads = E_commerce.query.filter_by(ad_type = ad_type).order_by(E_commerce.date_of_post.asc()).limit(11)

        # logic for CONTENT field only
        # if request.method == 'POST' and commentForm.validate() :

        #     comment_body = commentForm.comment.data
        #     ad_id = ad_id

            # comment = Comments(
            #             comment_body = comment_body,
            #             buy_id = buy_id,
            #             commentor = current_user
            #             )

            # db.session.add(comment)
            # db.session.commit()
            # flash('COMMENT ADDED', 'success')
            # return redirect(request.url)


        # comments = Comments.query.filter_by(buy_id = buy_id).order_by(Comments.date_of_comment.desc()) 
        



    return render_template("buy/ad-view-page.html", ad = ad , similar_ads = similar_ads )








#the page that simulates online payment that gives you the ability to buy
@buy_blueprint.route('/buy-sturf-payment-page', methods=['GET', 'POST'])
@login_required  
def buy_payment_page():
    return render_template("buy/buy_sturf_payment.html")










#this route asks what kinda buy you want to make so it knows what kinda form to give you
@buy_blueprint.route('/ad-type', methods=['GET', 'POST'])
@login_required  
def ad_type():
    return render_template("buy/ad-type.html")










#the route that simulates the proceessing of  an online payment that gives you the ability to buy

@buy_blueprint.route('/buy-sturf-payment/<email>', methods=['GET', 'POST'])
@login_required  
def buy_sturf_payment(email):
    user = User.query.filter_by(email = email).first_or_404()
    user.paid = True
    user.generic = False
    db.session.commit()
    flash (' YOU HAVE BEEN SUBSCRIBED TO VIP, ENJOY!', 'success')
    return redirect(url_for('buy.buy', buy_type = 'normal'))





#the route that simulates the proceessing of  a free user, also gives you the ability to buy

@buy_blueprint.route('/buy-sturf-generic/<email>', methods=['GET', 'POST'])
@login_required  
def buy_sturf_generic(email):
    user = User.query.filter_by(email = email).first_or_404()
    user.generic = True
    user.paid = False
    db.session.commit()
    flash (' YOU HAVE BEEN REGISTERED AS A FREE USER', 'success')
    return redirect(url_for('buy.buy'))













@buy_blueprint.route('/user-template/<email>', methods=['GET'])
@login_required  
def user_template(email):

    user = User.query.filter_by(email = email).first_or_404()

    buy = buy.query.filter_by(author = user).order_by(buy.date_buyed.desc())

    buy_count = buy.query.filter_by(author = user).all()


    p = user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))
    return render_template("buy/user-template.html", user = user, img = img, buy = buy,  buy_count= buy_count )






@buy_blueprint.route('/my-ads/<email>', methods=['GET'])
@login_required
def my_ads(email):

    user = User.query.filter_by(email = email).first_or_404()

    buy = buy.query.filter_by(author = user).order_by(buy.date_buyed.desc())

    buy_count = buy.query.filter_by(author = user).all()

    p = user.image_file
    img = url_for('static', filename = 'profile_pics/uploads/{}'.format(p))


    return render_template("buy/my-ads.html", user = user, img = img, buy = buy,  buy_count= buy_count )













# the route that renders the page to create phone ads
@buy_blueprint.route('/create-phone-ad/', methods=['GET', 'POST'])
@login_required
def create_phone_ad():
    #
    form = AdForm(CombinedMultiDict((request.files, request.form)))
    imagelist = []
    

    

    if  request.method == 'POST' and form.validate() :

        #the request.files object intance
        images = request.files.getlist('photo')

        for each in images:
            if not each:
                flash('NO  PHOTO CHOSEN', 'error')
                # print('block1 executed')
                return redirect(request.url)

            if each and allowed_file(each.filename) and each.filename != '':
                # print ('file---->',each.filename)

                split_file_name = os.path.splitext(each.filename)
                name_list = list(split_file_name)
                ex = str(file_ext(each.filename))
                secure = secure_filename(each.filename)

                #funtion to generate random name
                def random_name(filename):
                    random_hex = str(secrets.token_hex(8))
                #the return statement below returns a random name for each file with different parameters separated by underscores 
                    return   current_user.first_name + '_' + current_user.last_name + '_' + name_list[0] + '__' + random_hex + '__' + current_time() + '.' + ex


                #the name of the file gets assigned to the randomly generated file name 
                filename  = random_name(each.filename)
                # print(filename)

                uploads_path = os.path.join(current_app.root_path, 'static/buy_sturf', filename)

                #the next four lines just resizes the image to the given dimensions e.g 125 by 125
                output_size = (250,250)
                i = Image.open(each)
                i.thumbnail(output_size)
                i.save(uploads_path)


                # flash('{}'.format(filename), 'error')
                imagelist.append(filename)                                  

        # flash('{}'.format(imagelist), 'success')
        
        # print(' new image list', imagelist)



        title = form.title.data.upper()

        brand = form.brand.data.lower()

        condition = form.condition.data.lower()

        price = form.price.data

        ram = form.ram.data.upper()

        screen_size = form.screen_size.data.lower()

        colour = form.colour.data.lower()

        camera = form.camera.data.upper()

        description =  form.description.data.lower()

        


        phone_ad = E_commerce(
                image_files = eval(str(imagelist)),
                title = title, 
                brand = brand,
                condition = condition,
                price = price,
                ram = ram ,
                screen_size = screen_size,
                colour = colour,
                camera = camera,
                description = description,
                ad_type = 'phone',
                seller = current_user

                )   
                
        db.session.add(phone_ad)
        db.session.commit()  

        flash('YOUR AD HAS BEEN POSTED ', 'success')

        # flash('{}'.format(imagelist), 'info')
        return redirect(request.url)



    return render_template('buy/create-phone-ad.html',  form = form, page_title = "create Phone ad")






# the route that renders the page to create phone ads
@buy_blueprint.route('/create-tablet-ad/', methods=['GET', 'POST'])
@login_required
def create_tablet_ad():
    #
    form = TabletAdForm(CombinedMultiDict((request.files, request.form)))
    imagelist = []
  

    

    if  request.method == 'POST' and form.validate() :

        #the request.files object intance
        images = request.files.getlist('photo')

        for each in images:
            if not each:
                flash('NO  PHOTO CHOSEN', 'error')
                # print('block1 executed')
                return redirect(request.url)

            if each and allowed_file(each.filename) and each.filename != '':
                # print ('file---->',each.filename)

                split_file_name = os.path.splitext(each.filename)
                name_list = list(split_file_name)
                ex = str(file_ext(each.filename))
                secure = secure_filename(each.filename)

                #funtion to generate random name
                def random_name(filename):
                    random_hex = str(secrets.token_hex(8))
                #the return statement below returns a random name for each file with different parameters separated by underscores 
                    return   current_user.first_name + '_' + current_user.last_name + '_' + name_list[0] + '__' + random_hex + '__' + current_time() + '.' + ex


                #the name of the file gets assigned to the randomly generated file name 
                filename  = random_name(each.filename)
                # print(filename)

                uploads_path = os.path.join(current_app.root_path, 'static/buy_sturf', filename)

                #the next four lines just resizes the image to the given dimensions e.g 125 by 125
                output_size = (250,250)
                i = Image.open(each)
                i.thumbnail(output_size)
                i.save(uploads_path)


                # flash('{}'.format(filename), 'error')
                imagelist.append(filename)                                  

        # flash('{}'.format(imagelist), 'success')
        
        # print(' new image list', imagelist)



        title = form.title.data.upper()

        brand = form.brand.data.lower()

        condition = form.condition.data.lower()

        price = form.price.data

        ram = form.ram.data.upper()

        operating_system = form.operating_system.data.lower()

        storage_capacity = form.storage_capacity.data.upper()

        screen_size = form.screen_size.data.lower()

        colour = form.colour.data.lower()

        camera = form.camera.data.upper()

        description =  form.description.data.lower()



        tablet_ad = E_commerce(
                image_files = eval(str(imagelist)),
                title = title, 
                brand = brand,
                condition = condition,
                storage_capacity = storage_capacity,
                operating_system = operating_system,
                price = price,
                ram = ram ,
                screen_size = screen_size,
                colour = colour,
                camera = camera,
                description = description,
                ad_type= 'tablet',
                seller = current_user

                )   
                
        db.session.add(tablet_ad)
        db.session.commit()  

        flash('YOUR AD HAS BEEN POSTED ', 'success')

        # flash('{}'.format(imagelist), 'info')
        return redirect(request.url)



    return render_template('buy/create-tablet-ad.html',  form = form, page_title = "create Tablet ad")




















@buy_blueprint.route('/update_ad_image/<int:ad_id>',methods=['GET','POST'])
@login_required
def update_ad_image(ad_id):

    ad = E_commerce.query.get_or_404(ad_id)
    imgr = ad.image_files
    imagelist = []
    multiphotoform = MultiPhotoForm(CombinedMultiDict((request.files, request.form)))

    if ad.seller != current_user:
        abort(403)

 
    if  request.method == 'POST' and multiphotoform.validate() :
        #the request.files object intance
        images = request.files.getlist('photo')

        for item in images:

            if not item:
                flash('NO  PHOTO CHOSEN', 'error')
                # print('block1 executed')
                return redirect(request.url)

            if item and allowed_file(item.filename) and item.filename != '':
                # print('yay', item.filename)

                split_file_name = os.path.splitext(item.filename)
                name_list = list(split_file_name)
                ex = str(file_ext(item.filename))
                secure = secure_filename(item.filename)

                #funtion to generate random name
                def random_name(filename):
                    random_hex = str(secrets.token_hex(8))
                #the return statement below returns a random name for each file with different parameters separated by underscores 
                    return   current_user.first_name + '_' + current_user.last_name + '_' + name_list[0] + '__' + random_hex + '__' + current_time() + '.' + ex


                #the name of the file gets assigned to the randomly generated file name 
                filename  = random_name(item.filename)
                # print(filename)

                uploads_path = os.path.join(current_app.root_path, 'static/buy_sturf', filename)

                #the next four lines just resizes the image to the given dimensions e.g 125 by 125
                output_size = (250,250)
                i = Image.open(item)
                i.thumbnail(output_size)
                i.save(uploads_path)


                # flash('{}'.format(filename), 'error')
                imagelist.append(filename)
                print(imagelist)
        

    


 
        ad.image_files = eval(str(imagelist))
        db.session.commit()


        flash('AD IMAGES UPDATED', 'success')
        return redirect(request.url)



    

    
    return render_template("buy/update-ad-image.html",ad = ad,  photoForm = multiphotoform, imgr = imgr)
















# route to update each buy individually
@buy_blueprint.route('/ad-update/<int:ad_id>', methods=['GET', 'POST'])
@login_required  
def ad_update(ad_id):
    buy = buy.query.get_or_404(ad_id)
    if buy.author != current_user:
        abort(403)
    titleForm = TitleForm()
    contentForm = ContentForm()
    linkForm = LinkForm()

    
    # logic for CONTENT field only
    if request.method == 'POST' and contentForm.validate() :
        buy.content = contentForm.content.data.lower()
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR buy CONTENT', 'success')
        return redirect(request.url)


    # logic for TITLE field only
    elif request.method == 'POST' and titleForm.validate() :
        buy.title = titleForm.title.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR buy TITLE', 'success')
        return redirect(request.url)


    # logic for link field only
    elif request.method == 'POST' and linkForm.validate() :
        buy.link = linkForm.url.data
        db.session.commit()
        flash('SUCESSFULLY UPDATED  YOUR buy LINK', 'success')
        return redirect(request.url)






    

    elif request.method == 'GET':
        titleForm.title.data =   buy.title
        contentForm.content.data = buy.content
        linkForm.url.data = str(buy.link)
     


    return render_template("buy/buy-ad-update.html", buy = buy, page_title = "update your buy", titleForm = titleForm, contentForm = contentForm, linkForm = linkForm)















# route to delete a specific image from a list individually
@buy_blueprint.route('/delete-image/<int:ad_id>/<img>', methods=['GET','POST'])
@login_required  
def delete_image(ad_id,img):
    ad = E_commerce.query.get_or_404(ad_id)
    images = ad.image_files


    if ad.seller != current_user:
        abort(403)

    if img in images:
        print('found image {} in images'.format(img), images)
        print('\n','the list type is ', type(images))        
        images.remove(img)
        new_list = images
        # print('\n','new stored image variable', images)

        # i cant add an image to a list in a postgres database because it is immutable
         # so i have to flush the list and repopulate it again thats why i have 2 commits
        ad.image_files = None
        db.session.commit()

        ad.image_files  = eval(str(images))
        # print('\n','new image list after remove', images) 
        # ad.image_files = images
        db.session.commit()

    
    # print('\n', 'now this is what is left in the database after commit', images ,'\n')

 
    flash('DELETED!', 'success')
    return redirect(url_for('buy.update_ad_image', ad_id = ad_id ))






# route to delete each buy individually
@buy_blueprint.route('/delete-ad/<int:ad_id>',  methods=['GET','POST'])
@login_required  
def delete_ad(ad_id):
    ad = E_commerce.query.get_or_404(ad_id)
    
    if ad.seller != current_user:
        abort(403)

    db.session.delete(ad)
    db.session.commit()
    flash('YOUR AD HAS BEEN DELETED', 'success')
    return redirect(url_for('buy.ads', page = 1, sort = 'normal' ))





# route to delete a comment
@buy_blueprint.route('/buy-comment-delete/<int:id>/<int:buy_id>', methods=['GET','POST'])
@login_required  
def delete_comment(id,buy_id):
    comment = Comments.query.get_or_404(id)
    
    if comment.commentor != current_user:
        abort(403)

    db.session.delete(comment)
    db.session.commit()
    flash('COMMENT DELETED', 'success')
    return redirect(url_for('buy.buy_view_page', buy_id = buy_id))






# route to follow a user
@buy_blueprint.route('/follow-user/<email>/<int:buy_id>', methods=['GET','POST'])
@login_required  
def follow_user(email,buy_id):
    u1 = current_user
    u2 = User.query.filter_by(email = email).first()
    buy = buy.query.get_or_404(buy_id)

    # this is so that a user cannot follow themselves
    if buy.author == current_user:
        abort(403)


    u1.follow(u2)

    db.session.commit()
    return redirect(url_for('buy.buy_view_page', buy_id = buy_id))





# route to unfollow a user
@buy_blueprint.route('/unfollow-user/<email>/<int:buy_id>', methods=['GET','POST'])
@login_required  
def unfollow_user(email,buy_id):
    u1 = current_user
    u2 = User.query.filter_by(email = email).first()
    buy = buy.query.get_or_404(buy_id)

    # this is so that a user cannot follow themselves
    if buy.author == current_user:
        abort(403)


    u1.unfollow(u2)

   
    db.session.commit()
    return redirect(url_for('buy.buy_view_page', buy_id = buy_id))