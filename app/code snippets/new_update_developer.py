@app.route('/api-save',methods=['GET','POST'])
def save_post_data():
    def UpdateStatus(status,timestamp,location):
        msg="msg"
        
        try:
            sqliteConnection = sqlite3.connect('data/lightStatus.db',
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


            # get developer detail
            sqlite_select_query = """SELECT state, period from lightStatus where location = (?,?)"""
            cursor.execute(sqlite_select_query, ('campus','offcampus'))
            records = cursor.fetchall()


            for row in records:
                1st_row= row[0]
                2nd_row = row[1]
                print(1st_row, " was saved on", timestamp)
                print("timestamp type is", type(timestamp))
                

            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")

    UpdateStatus(request.args.get('status'),datetime.datetime.now(),request.args.get('location'))
    msg = "seems like all went well"
    return render_template("testing.html",msg = msg)
