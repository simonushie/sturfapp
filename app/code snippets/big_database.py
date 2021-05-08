#############################################################################################################################################################################
############################################################################# BIG DATABSE MODEL ##############################################################################
#############################################################################################################################################################################



class E_commerce(db.Mode):
    id = db.Column(db.Integer,primary_key = True) 

    
    title =  db.Column(db.String(1500), nullable = True)

    image_file = db.Column(db.ARRAY(db.String(1500)))

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
