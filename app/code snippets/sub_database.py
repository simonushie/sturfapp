#############################################################################################################################################################################
############################################################################# BUY STURF MODELS ##############################################################################
#############################################################################################################################################################################






#####################################
######### PHONES CATEGORY ###########
#####################################




class Phones(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    title =  db.Column(db.String(1500), nullable = False)
    image_files = db.Column(db.ARRAY(db.String(1500)))
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)

    # optional fields
    ram =  db.Column(db.String(1500), nullable = True)
    screen_size =  db.Column(db.String(1500), nullable = True)
    colour =  db.Column(db.String(1500), nullable = True)
    camera =  db.Column(db.String(1500), nullable = True)
    description = db.Column(db.Text)    
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Phone_ad  ('{self.id}', {self.price},'{self.title}', {self.description}', '{self.condition}', '{self.camera}',  '{self.screen_size}') > \n\n"




class Tablets(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    title =  db.Column(db.String(1500), nullable = False)
    image_files = db.Column(db.ARRAY(db.String(1500)))
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)
    storage_capacity =  db.Column(db.String(1500), nullable = False)
    operating_system =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)

    # optional fields
    ram =  db.Column(db.String(1500), nullable = True)
    screen_size =  db.Column(db.String(1500), nullable = True)
    colour =  db.Column(db.String(1500), nullable = True)
    camera =  db.Column(db.String(1500), nullable = True)
    description = db.Column(db.Text)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" <Tablet_ad  ('{self.id}', {self.price},'{self.title}', {self.description}', '{self.condition}', '{self.camera}',  '{self.screen_size}') > \n\n"



class Mobile_Accessories(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)    
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < MObile_accessories ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"











##########################################
######### ELECTRONICS CATEGORY ###########
##########################################



class Laptops(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    title =  db.Column(db.String(1500), nullable = False)
    image_files = db.Column(db.ARRAY(db.String(1500)))
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)
    storage_capacity =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    ram =  db.Column(db.String(1500), nullable = True)
    description = db.Column(db.Text)

    # optional fields
    subtype =  db.Column(db.String(1500), nullable = True)
    processor =  db.Column(db.String(1500), nullable = True)
    number_of_cores =  db.Column(db.String(1500), nullable = True)
    graphics_card =  db.Column(db.String(1500), nullable = True)
    graphics_card_memory =  db.Column(db.String(1500), nullable = True)
    storage_type =  db.Column(db.String(1500), nullable = True)
    operating_system =  db.Column(db.String(1500), nullable = True)
    screen_size =  db.Column(db.String(1500), nullable = True)
    camera =  db.Column(db.String(1500), nullable = True)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" <Laptops_ad  ('{self.id}', {self.price},'{self.title}', {self.description}', '{self.condition}', '{self.camera}',  '{self.screen_size}') > \n\n"




class Computer_Accessories(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields  
    brand =  db.Column(db.String(1500), nullable = False)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Computer_accessories ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Cameras(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields  
    make =  db.Column(db.String(1500), nullable = False)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Cameras ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"






class Music_Equipment(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)

    # optional fields  
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Music_Equipment ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Video_Games(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    platform =  db.Column(db.String(1500), nullable = False)


    # optional fields  
    brand =  db.Column(db.String(1500), nullable = True)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Video_Games ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Computer_Software(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)
    

    # optional fields  
    brand =  db.Column(db.String(1500), nullable = True)
    format =  db.Column(db.String(1500), nullable = True)
    platform =  db.Column(db.String(1500), nullable = True)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Computer_Software ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




##########################################
############# FASHION CATEGORY ###########
##########################################



class Shoes(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)
    size =  db.Column(db.String(1500), nullable = True)
    style =  db.Column(db.String(1500), nullable = True)
    upper_material =  db.Column(db.String(1500), nullable = True)
    outsole_material =  db.Column(db.String(1500), nullable = True)   
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Shoes ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




class Clothing(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)
    size =  db.Column(db.String(1500), nullable = True)
    style =  db.Column(db.String(1500), nullable = True)  
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Clothing ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Bags(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)
    material =  db.Column(db.String(1500), nullable = True)
    closure =  db.Column(db.String(1500), nullable = True)  
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Bags ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Jewelries(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)
    main_material =  db.Column(db.String(1500), nullable = True)
    main_stone =  db.Column(db.String(1500), nullable = True)  
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Jewelries ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




class Bath_and_body(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
 

    # optional fields  
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Bath_and_body ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Fragrance(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)
    formulation =  db.Column(db.String(1500), nullable = False)
 

    # optional fields  
    scent =  db.Column(db.String(1500), nullable = False)
    volume =  db.Column(db.String(1500), nullable = False)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Fragrance ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




class Hair_Weaves(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    

    # optional fields  
    type =  db.Column(db.String(1500), nullable = False)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Hair_Weaves ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"





class Makeup(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    type = db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)
    brand =  db.Column(db.String(1500), nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)
    tone =  db.Column(db.String(1500), nullable = True)  
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Makeup ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




class Skin_Care(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    gender =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields
    colour =  db.Column(db.String(1500), nullable = True)
    type =  db.Column(db.String(1500), nullable = True)
    target_area =  db.Column(db.String(1500), nullable = True) 
    skin_type = db.Column(db.String(1500), nullable = True)
    benefits = db.Column(db.String(1500), nullable = True) 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Skin_Care ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"








##########################################
############ SERVICES CATEGORY ###########
##########################################




############ automotive ###########


class Repairs_and_installation(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Repairs_and_installation ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




############ construction ###########


class Plumbing(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Plumbing ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Labour(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Labour ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"


class Electrical_works(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Electrical_works ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Printing(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Printing ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




############ personal ###########


class Classes_and_courses(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    subtype =  db.Column(db.String(1500), nullable = True)
    type =  db.Column(db.String(1500), nullable = True)
    level =  db.Column(db.String(1500), nullable = True)
    duration =  db.Column(db.String(1500), nullable = True)
    service_features =  db.Column(db.String(1500), nullable = True)
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Classes_and_courses ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Cleaning(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    round_the_clock_service = db.Column(db.Boolean())
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Cleaning ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"


class Repairs(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    round_the_clock_service = db.Column(db.Boolean())
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Repairs ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




############ business ###########



class Computer_and_IT(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Computer_and_IT ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Gfx_design(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Gfx_design ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




############ leisure ###########


class Party_and_catering_event(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    round_the_clock_service = db.Column(db.Boolean())
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Party_and_catering_event ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Dj_and_entertainmment(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    round_the_clock_service = db.Column(db.Boolean())
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Dj_and_entertainmment ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




class Health_and_beauty(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Health_and_beauty ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Photography(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    type_of_service =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields
    service_include =  db.Column(db.String(1500), nullable = False) 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Photography ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"







###############################################
############# AUTOMOBILE CATEGORY #############
###############################################


class Motorcycle_and_scooters(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    make =  db.Column(db.String(1500), nullable = False)
    year_of_manufacture =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields
    transmission =  db.Column(db.String(1500), nullable = False)
    mileage =  db.Column(db.String(1500), nullable = False) 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Motorcycle_and_scooters ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"




class Bicycles(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    make =  db.Column(db.String(1500), nullable = False)
    year_of_manufacture =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Bicycles ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"



class Vehicle_parts(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    make =  db.Column(db.String(1500), nullable = False)
    type =  db.Column(db.String(1500), nullable = False)
    condition =  db.Column(db.String(1500), nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Vehicle_parts ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"






###############################################
############### FOOD CATEGORY #################
###############################################


class Meals_and_drink(db.Model):
    id = db.Column(db.Integer,primary_key = True) 

    # mandatory fields
    image_files = db.Column(db.ARRAY(db.String(1500)))
    title =  db.Column(db.String(1500), nullable = False)
    date_of_post = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow())
    price =  db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.Text, nullable = False)

    # optional fields 
    ad_type = db.Column(db.String(1500), nullable = True)
    
    #RELATIONSHIP
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

  
    def __repr__(self):
        return f" < Meals_and_drink ({self.id}, {self.price},{self.title}, {self.description}, {self.condition}) > \n\n"
