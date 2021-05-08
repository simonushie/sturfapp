from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, url
from wtforms import Form, BooleanField, StringField, IntegerField, PasswordField, validators, TextAreaField, DateField, SelectField, SubmitField, RadioField
from wtforms.fields.html5 import URLField
from wtforms.fields import  MultipleFileField
from flask_security import current_user
from flask_security.forms import LoginForm, RegisterForm, StringField, Required, BooleanField,Length
from flask import session



#####################################
######### USER FORMS ################
#####################################




# my custom login form that sets session to x amount of minutes
class CustomLoginForm(LoginForm):
    def validate(self): 
        response = super(CustomLoginForm, self).validate()
        session.permanent = True
        return response

# adding other form fields to the sign up form e.g first name and last name
class ExtendedRegisterForm(RegisterForm):
    choices = [('Above 18', 'Above 18'),
               ('Below 18', 'Below 18')]
    first_name = StringField('First Name', [Required()])
    last_name = StringField('Last Name', [Required()])
    # phone = StringField('Phone', [Required()])
    age = SelectField('Age', choices=choices)
    






#####################################
######### COMMENT FORM #########
#####################################

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment ', [validators.Length(min=3, max=160)])





#####################################
######### MESSAGE FORM #########
#####################################

class MessageForm(FlaskForm):
    message = TextAreaField((''), validators=[DataRequired(), Length(min=0, max=140000)])


#####################################
######### EDIT PROFILE FORMS #########
#####################################

class CaptionForm(FlaskForm):
    caption = TextAreaField('you are a.....?( finish the sentence ) ', [validators.Length(min=3, max=160)])


class MoreAboutForm(FlaskForm):
    more_about = TextAreaField('Write More About Yourself', [validators.Length(min=3, max=300)])
    
   
class BirthDayForm(FlaskForm):
    birth_day = StringField('Birth Day(you can add just the month and day)', [validators.Length(min=5, max=20)])


class LikesForm(FlaskForm):
    likes = StringField('Likes', [validators.Length(min=3, max=150)])


class DislikesForm(FlaskForm):
    dislikes = StringField('Dislikes', [validators.Length(min=3, max=150)])


class PhoneForm(FlaskForm):
    phone = StringField('Phone Number', [validators.Length(min=11, max=11)])


class WhatssapForm(FlaskForm):
    phone = StringField('Whatssap Number', [validators.Length(min=11, max=11)])


class AddressForm(FlaskForm):
    address = StringField('Address', [validators.Length(min=3, max=150)])


class BirthDayForm(FlaskForm):
    
    a = [


(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20),
(21),
(22),
(23),
(24),
(25),
(26),
(27),
(28),
(29),
(30),
(31)

    ]      



    b = [('January', 'January'),
                ('February', 'February'),
                ('March', 'March'),
                ('April', 'April'),
               ('May', 'May'),
               ('June', 'June'),
                ('July', 'July'),
                ('August', 'August'),
               ('September', 'September'),
               ('October', 'October'),
                ('November', 'November'),
                ('December', 'December')
        
               ]



    c = [

(1980),
(1981),
(1982),
(1983),
(1984),
(1985),
(1986),
(1987),
(1988),
(1989),
(1990),
(1991),
(1992),
(1993),
(1994),
(1995),
(1996),
(1997),
(1998),
(1999),
(2000),
(2001),
(2002),
(2003),
(2004),
(2005),
(2006),
(2007),
(2008),
(2009),
(2010),
(2011),
(2012),
(2013),
(2014),
(2015),
(2016),
(2017),
(2018),
(2019),
(2020)

    ]
               

    day = SelectField('Day', [Required()] ,  choices = a)
    month = SelectField('month',  [Required()] , choices = b)
    year = SelectField('year', [Required()] ,  choices = c)

# END OF EDIT PROFILE FORM
















#####################################
########## POST STURF FORMS #########
#####################################

# POST ANNOUNCEMENT FORM
class PostForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=3, max=100)])
    content = TextAreaField('Content', [validators.Length(min=3, max=30000)])
    photo = FileField('')




# POST EVENT FORM
class EventForm(FlaskForm):

    a = [



(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20),
(21),
(22),
(23),
(24),
(25),
(26),
(27),
(28),
(29),
(30),
(31)

    ]      



    b = [('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
       ('May', 'May'),
       ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
       ('September', 'September'),
       ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')

       ]



    c = [

(2021),
(2022),
(2023),
(2024),
(2025),
(2026),
(2027),
(2028),
(2029),
(2030),
(2031)

    ]


    day = SelectField('Day', [Required()] ,  choices = a)
    month = SelectField('month',  [Required()] , choices = b)
    year = SelectField('year', [Required()] ,  choices = c)

    title = StringField('Title', [validators.Length(min=3, max=100)])
    venue = StringField('Venue', [validators.Length(min=3, max=100)])
    content = TextAreaField('Content', [validators.Length(min=3, max=30000)])
    photo = FileField('')





# INDIVIDUAL POST EVENT FORM
class TitleForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=3, max=30)])

class ContentForm(FlaskForm):
    content = TextAreaField('Content', [validators.Length(min=3, max=300)])
   
class PhotoForm(Form):
    photo = FileField('')


class MultiPhotoForm(Form):
    photo =  MultipleFileField('', [Required()])

class VenueForm(FlaskForm):
    venue = StringField('Venue', [validators.Length(min=1, max=100)])


class LinkForm(FlaskForm):
    url = URLField('Add/Update link (must contain "http://") ', validators = [url()])

    # def validate(self):
    #     if not (str(self.url.data).startswith("http://") or str(self.url.data).startswith("https://")):
    #         self.url.data = "http://" + self.url.data

 





# POST EVENT FORM
class LostForm(FlaskForm):


    x = [('id card', 'id card'),
             ('phone', 'phone'),
             ('key', 'key'),
             ('laptop', 'laptop'),
             ('tablet', 'tablet'),
             ('charger', 'charger'),
             ('document or file', 'document or file'),
             ('clothing', 'clothing'),
             ('fashion accessory', 'fashion accessory'),
             ('mobile phone accessory', 'mobile phone accessory'),
             ('wallet', 'wallet'),
             ('electronic device', 'electronic device'),
             ('atm card', 'atm card')
             ]
    z = [('Found Items', 'Found Items'),
             ('Lost Items', 'Lost Items'),
             ('Events', 'Events'),
             ('Regular Posts', 'Regular Posts'),
             ('Donation Campaigns', 'Donation Campaigns'),
             ('All', 'All')
             ]



    stud = [('Yes', 'Yes'),
            ('No', 'No')
           ]

    item_name = StringField('Name of item?', [validators.Length(min=3, max=100)])

    item_location = StringField('Location item was found?', [validators.Length(min=3, max=100)])

    description = TextAreaField('Description of Item', [validators.Length(min=3, max=30000)])

    photo = FileField('')


    possession = RadioField('Are you currently in possession of this item?', [Required()] ,   choices = stud, default = 'Yes' )


    item_category = SelectField('Item category', [Required()] ,  choices = x)



# for each in LostForm.x :
#   print(str(each[0]))


class SearchingForm(FlaskForm):

    x = [('id card', 'id card'),
             ('phone', 'phone'),
             ('key', 'key'),
             ('laptop', 'laptop'),
             ('tablet', 'tablet'),
             ('charger', 'charger'),
             ('document or file', 'document or file'),
             ('clothing', 'clothing'),
             ('fashion accessory', 'fashion accessory'),
             ('mobile phone accessory', 'mobile phone accessory'),
             ('wallet', 'wallet'),
             ('electronic device', 'electronic device'),
             ('atm card', 'atm card')
             ]

    a = [

(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20),
(21),
(22),
(23),
(24),
(25),
(26),
(27),
(28),
(29),
(30),
(31)

    ]      



    b = [('January', 'January'),
                ('February', 'February'),
                ('March', 'March'),
                ('April', 'April'),
               ('May', 'May'),
               ('June', 'June'),
                ('July', 'July'),
                ('August', 'August'),
               ('September', 'September'),
               ('October', 'October'),
                ('November', 'November'),
                ('December', 'December')
        
               ]



    c = [


(2000),
(2001),
(2002),
(2003),
(2004),
(2005),
(2006),
(2007),
(2008),
(2009),
(2010),
(2011),
(2012),
(2013),
(2014),
(2015),
(2016),
(2017),
(2018),
(2019),
(2020),
(2021)

    ]
               



    item_name = StringField('Name of Item?', [validators.Length(min=3, max=100)])

    item_location = StringField('Location Item Was Lost?', [validators.Length(min=3, max=100)])

    description = TextAreaField('Description ', [validators.Length(min=3, max=30000)])


    item_category = SelectField('Item category', [Required()] ,  choices = x)


    day = SelectField('Day',  choices = a)
    month = SelectField('month',   choices = b)
    year = SelectField('year',   choices = c)















# INDIVIDUAL POST EVENT FORM
class TitleForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=3, max=30)])

class ContentForm(FlaskForm):
    content = TextAreaField('Content', [validators.Length(min=3, max=300)])
   
class PhotoForm(Form):
    photo = FileField('')


class MultiPhotoForm(Form):
    photo =  MultipleFileField('', [Required()] )

class VenueForm(FlaskForm):
    venue = StringField('Venue', [validators.Length(min=1, max=100)])


class LinkForm(FlaskForm):
    url = URLField('Add/Update link (must contain "http://") ', validators = [url()])

    # def validate(self):
    #     if not (str(self.url.data).startswith("http://") or str(self.url.data).startswith("https://")):
    #         self.url.data = "http://" + self.url.data

 












#####################################
######## ROOMIE STURF FORMS #########
#####################################


class RoomieRegisterForm(FlaskForm):
    a = [('Christianity', 'Christianity'),
               ('Islam', 'Islam'),
               ('Other', 'Other')
               ]

    b = [('100L', '100L'),
                ('200L', '200L'),
                ('300L', '300L'),
                ('400L', '400L'),
               ('500L', '500L')]

    c = [('Gidan Kwano', 'Gidan Kwano'),
                ('Bosso', 'Bosso'),
                ('Other', 'Other')
               ]

    d = [('Greater than 10k', 'Greater than 10k'),
                ('Greater than 20k', 'Greater than 20k'),
                ('Greater than 30k', 'Greater than 30k'),
                ('Greater than 40k', 'Greater than 40k'),
                ('50k and above', '50k and above')
               ]

   


    religion = SelectField('Religion', [Required()] ,  choices = a)
    level = SelectField('Level',  [Required()] , choices = b)
    based_in = SelectField('Based currently in', [Required()] ,  choices = c)
    budget = SelectField('What\'s Your Budget?', [Required()] ,  choices = d)




#####################################
######## ROOMIE STURF FORMS #########
#####################################


class ClaimerForm(FlaskForm):



    photo = FileField('')

    content = TextAreaField('A brief description of this lost item', [validators.Length(min=3, max=30000)])
   
    








#####################################
######## ROOMIE INDEPENDENT  FORMS #########
#####################################


class ReligionForm(FlaskForm):
    a = [('Christianity', 'Christianity'),
               ('Islam', 'Islam'),
               ('Other', 'Other')
               ]



    religion = SelectField('Religion', [Required()] ,  choices = a)




class LevelForm(FlaskForm):
    b = [('100L', '100L'),
                ('200L', '200L'),
                ('300L', '300L'),
                ('400L', '400L'),
               ('500L', '500L')]

    level = SelectField('Level',  [Required()] , choices = b)


class BasedForm(FlaskForm):
    c = [('Gidan Kwano', 'Gidan Kwano'),
                ('Bosso', 'Bosso'),
                ('Other', 'Other')
               ]

    based_in = SelectField('Based currently in', [Required()] ,  choices = c)



class BudgetForm(FlaskForm):
    c = [('Greater than 10k', 'Greater than 10k'),
                ('Greater than 20k', 'Greater than 20k'),
                ('Greater than 30k', 'Greater than 30k'),
                ('Greater than 40k', 'Greater than 40k'),
                ('50k and above', '50k and above')
               ]

    budget = SelectField('Change Your Budget?', [Required()] ,  choices = c)








class StudentForm(FlaskForm):
    stud = [('Yes', 'Yes'),
            ('No', 'No')
           ]


    is_student = RadioField('Are you a student?', [Required()] ,  choices = stud)























#####################################
######## BUY STURF FORMS    #########
#####################################








    






# PHONE AD FORM
class AdForm(FlaskForm):


    r = [('3GB', '3GB'),
                ('3GB', '3GB'),
                ('3GB', '3GB')
               ]



    c = [('red', 'red'),
            ('blue', 'blue'),
            ('black', 'black')
           ]




    s = [('500 by 500', '500 by 500'),
            ('500 by 500', '500 by 500'),
            ('500 by 500', '500 by 500')
           ]

    cam = [('2MP', '2MP'),
            ('4MP', '4MP'),
            ('8MP', '8MP')
           ]

    cond = [('New', 'New'),
            ('Used', 'Used')
           ]

    br = [('Tecno', 'Tecno'),
            ('infinix', 'infinix'),
            ('Nexus', 'Nexus'),
            ('Apple', 'Apple')
           ]



    title = StringField('Title',  [validators.Length(min=3, max=50)])

    

    price = IntegerField('Price',  [Required()] )

    description = TextAreaField('Description')

    photo = MultipleFileField('', [Required()])



    brand = SelectField('Brand', [Required()] ,  choices = br)

    ram = SelectField('RAM',  choices = r)

    # operating_system = SelectField('Operating System',  choices = os)

    # storage_capacity = SelectField('Storage Capacity',  choices = storage)

    colour = SelectField('Colour',  choices = c)

    screen_size = SelectField('Screen size',  choices = s)

    camera = SelectField('Camera',  choices = cam)

    condition = RadioField('Condition', [Required()] ,  choices = cond)








class TabletAdForm(FlaskForm):

    r = [('3GB', '3GB'),
                ('3GB', '3GB'),
                ('3GB', '3GB')
               ]


    storage = [('3GB', '3GB'),
                ('6GB', '6GB'),
                ('112GB', '112GB')
               ]


    c = [('red', 'red'),
            ('blue', 'blue'),
            ('black', 'black')
           ]

    os = [('windows', 'windows'),
            ('linux', 'linux'),
            ('ios', 'ios'),
            ('android', 'android')
           ]



    s = [('500 by 500', '500 by 500'),
            ('500 by 500', '500 by 500'),
            ('500 by 500', '500 by 500')
           ]

    cam = [('2MP', '2MP'),
            ('4MP', '4MP'),
            ('8MP', '8MP')
           ]

    cond = [('New', 'New'),
            ('Used', 'Used')
           ]

    br = [('Tecno', 'Tecno'),
            ('infinix', 'infinix'),
            ('Samsung', 'Samsung'),
            ('Apple', 'Apple')
           ]



    title = StringField('Title',  [validators.Length(min=3, max=50)])

    

    price = IntegerField('Price',  [Required()] )

    description = TextAreaField('Description')

    photo = MultipleFileField('', [Required()])



    brand = SelectField('Brand', [Required()] ,  choices = br)

    ram = SelectField('RAM',  choices = r)

    operating_system = SelectField('Operating System',  choices = os)

    storage_capacity = SelectField('Storage Capacity',  choices = storage)

    colour = SelectField('Colour',  choices = c)

    screen_size = SelectField('Screen size',  choices = s)

    camera = SelectField('Camera',  choices = cam)

    condition = RadioField('Condition', [Required()] ,  choices = cond)


   
    
    
 





# PHONE AD FORM
class MobileAccessoriesForm(FlaskForm):

    c = [('red', 'red'),
            ('blue', 'blue'),
            ('black', 'black')
           ]

    cond = [('New', 'New'),
            ('Used', 'Used')
           ]

    br = [('Tecno', 'Tecno'),
            ('infinix', 'infinix'),
            ('Nexus', 'Nexus'),
            ('Apple', 'Apple')
           ]


    ty = [('type', 'type'),
            ('type', 'type'),
            ('type', 'type'),
            ('type', 'type')
           ]


    title = StringField('Title',  [validators.Length(min=3, max=50)])

    price = IntegerField('Price',  [Required()] )

    description = TextAreaField('Description' ,  [Required()])

    photo = MultipleFileField('', [Required()])

    brand = SelectField('Brand', [Required()] ,  choices = br)

    Type = SelectField('Type', [Required()] ,  choices = ty)

    colour = SelectField('Colour',  choices = c)

    condition = RadioField('Condition', [Required()] ,  choices = cond)