#previous sqlite code to update campus and offcampus routes from previous sqlite db
#and also to save from api route to various dbs





@app.route('/CtfT2GB2h9s4kP_cjZdqkSv5Bps/api-save',methods=['GET'])
def api_save():
    def lightStatus(status,timestamp,location):
        msg="msg"
        try:
            sqliteConnection = sqlite3.connect('app/data/lightStatus.db',
                                               detect_types=sqlite3.PARSE_DECLTYPES |
                                               sqlite3.PARSE_COLNAMES)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            # update developer detail
            sqlite_update = """UPDATE 'lightStatus'
                          SET state = ?, period = ?
                          WHERE  location = ?"""

            data_tuple = (status,timestamp,location)
            cursor.execute(sqlite_update, data_tuple)
            sqliteConnection.commit()
            print("Update added successfully \n")


            # get date from database
            sqlite_select_query = """SELECT period from lightStatus where location = ?"""
            cursor.execute(sqlite_select_query, (location,))
            records = cursor.fetchone()[0]

            stamp = int(records)

            date = datetime.fromtimestamp(stamp)

            date_string = date.strftime("%A") + " " + date.strftime("%I") + ":" + date.strftime("%M")  + date.strftime("%p") 

            # print (date_string)

            # print(type(records))

            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")



    # Second function that populates the records database
    def populateRecords(status,era,location):
        
        record_msg = "record msg"
        error = 'error'

        sqliteConnection = sqlite3.connect('app/blueprints/history/records.db',
                                               detect_types=sqlite3.PARSE_DECLTYPES |
                                               sqlite3.PARSE_COLNAMES)
        
        cursor = sqliteConnection.cursor()

        sqlite_add = """INSERT INTO records (state,period,location) VALUES (?,?,?)"""

        data_tuple = (status,era,location)
        cursor.execute(sqlite_add, data_tuple)
        sqliteConnection.commit()
        print("record added successfully \n \n \n ")
        sqliteConnection.close()
        print("connection to records db is closed \n \n ")


    lightStatus(request.args.get('status'),int(time.time()),request.args.get('location'))
    populateRecords(request.args.get('status'),datetime.now().strftime("%A " " %I:%M %p  %B " " %d "),request.args.get('location'))
    msg = "seems like all went well"
    record_msg = "seems like all went well recording those requests"
    


    return render_template("testing.html", record_msg = record_msg, msg = msg)









@electricity.route('/on-campus',methods=['GET'])
@login_required  
def campus():
    pic = 'static/lightbulb.gif'
    color = "#79ff4d"
    status = "status"
    era = "date"
    report = "report"
    t1 = "t1"
    t2 = "t2"
    title = "Campus"

    try:
    
        sqliteConnection = sqlite3.connect('app/data/lightStatus.db',
                                                   detect_types=sqlite3.PARSE_DECLTYPES |
                                                   sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")



        #check for datetime from database
        sqlite_datetime_query = """SELECT period from lightStatus where location = ?"""
        cursor.execute(sqlite_datetime_query, ('campus',))
        records = cursor.fetchone()[0]

        stamp = int(records)


        if stamp > 0: #checking for validity of timestamp

            date = datetime.fromtimestamp(stamp)

            date_string =  date.strftime("%I") + ":" + date.strftime("%M")  + date.strftime("%p") + " " + date.strftime("%A") + "," + date.strftime("%B") + " " +  date.strftime("%d")
           

            era = str(date_string)


        #checking for electricity status and update frontend appropriately
        sqlite_campus_query = """SELECT state from lightStatus WHERE location = 'campus' """
        cursor.execute(sqlite_campus_query)
        rec = cursor.fetchone()

        for row in rec: 
            com = str(row)
            print(com)
            
            if com == 'on':
                print ("yayyy!!!")
                status = "Hurray! there seems to be light on campus ☺"
                pic = 'static/lightbulb.gif'
                color = "#79ff4d"
                report = "The electricity was last restored around"
                t1 = ' #46BC28'
                t2 = '#79ff4d'

            else:
                print("nayyyy!")
                status = "No Power in school! ☹"
                pic = 'static/off.jpeg'
                color = "red"
                report = "The electricity was last interrupted at"
                t1 = 'red'
                t2 = 'red'


        

        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    sqliteConnection.close()


    return render_template("electricity/location.html",status = status, pic=pic,color=color,era = era,report = report,t1 = t1,t2 = t2, title = title)



@electricity.route('/off-campus',methods=['GET'])
@login_required  
def offcampus():
    pic = 'static/lightbulb.gif'
    color = "#79ff4d"
    status = "status"
    era = "date"
    report = "report"
    t1 = "t1"
    t2 = "t2"
    title = "Off Campus"
    try:
    
        sqliteConnection = sqlite3.connect('app/data/lightStatus.db',
                                                   detect_types=sqlite3.PARSE_DECLTYPES |
                                                   sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #check for datetime from database
        sqlite_datetime_query = """SELECT period from lightStatus where location = ?"""
        cursor.execute(sqlite_datetime_query, ('offcampus',))
        records = cursor.fetchone()[0]

        stamp = int(records)


        if stamp > 0: #checking for validity of timestamp

            date = datetime.fromtimestamp(stamp)

            date_string =   date.strftime("%I") + ":" + date.strftime("%M")  + date.strftime("%p") + " " + date.strftime("%A") + "," + date.strftime("%B") + " " +  date.strftime("%d")
           

            era = str(date_string)



        #check for electricity status and update frontend appropriately
        sqlite_offcampus_query = """SELECT state from lightStatus WHERE location = 'offcampus' """
        cursor.execute(sqlite_offcampus_query)
        rec1 = cursor.fetchone()
        success_report = ['Cheers! the power has been restored','Hurray! there is power off campus',
        'The power is back!',
        'The power supply has been restored','The electricity is back!','Homes off campus are shining bright! '
        ]

        failure_report = ['oops! no light off campus','Unfornately the streets off campus remain dark',
        'Sorry! but there is no electricity off-campus','The power hasn\'t still been restored, please check back shortly ',
         'electricity is non-existent at the moment', 'Nothing! yet, please try again shortly']

        for row in rec1: 
            com1 = str(row)
            if com1 == 'on':
                print ("yayyy!!!")
                status = random.choice(success_report)
                report = "The electricity was restored sometime around"
                pic = 'static/lightbulb.gif'
                color = "#79ff4d"
                t1 = ' #46BC28'
                t2 = '#79ff4d'

            else:
                print("nayyyy!")
                status = random.choice(failure_report)
                report = "The electricity was interrupted sometime around"
                pic = 'static/off.jpeg'
                color = "red"
                t1 = 'red'
                t2 = 'red'



        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    sqliteConnection.close()

    return render_template("electricity/location.html",status = status, pic=pic,color=color,era = era,report = report,t1 = t1,t2 = t2,title = title)




# the following code was extracted from the history 
#route which justs all the entries in the records database  

@history_blueprint.route('/',methods=['GET','POST'])
@login_required 
def history():
    con = sqlite3.connect("app/blueprints/history/records.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("select * from records order by period desc ") 
   
    rows = cur.fetchall();
    con.close()
    print ("old connection closed")
    return render_template("history/history.html", rows = rows)