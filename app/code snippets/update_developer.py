def UpdateDeveloper(name, joiningDate,id):
    msg = "msg"
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db',
                                           detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")


        
        sqlite_update = """UPDATE 'new_developers'
                          SET name = ?, joiningDate = ?
                          WHERE  id = ?"""

        data_tuple = (name, joiningDate, id)
        cursor.execute(sqlite_update, data_tuple)
        sqliteConnection.commit()
        print("Update added successfully \n")

        # get developer detail
        sqlite_select_query = """SELECT name, joiningDate from new_developers where id = ?"""
        cursor.execute(sqlite_select_query, (1,))
        records = cursor.fetchall()


        for row in records:
            developer= row[0]
            joining_Date = row[1]
            print(developer, " joined on", joiningDate)
            print("joining date type is", type(joining_Date))

        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
       
        return render_template("testing.html",msg = msg)
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

UpdateDeveloper(request.args.get('name'),datetime.datetime.now(),request.args.get('id'))
msg = "seems like all went well"