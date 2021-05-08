def addDeveloper(id, name, joiningDate):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db',
                                           detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_create_table_query = '''CREATE TABLE new_developers (
                                       id INTEGER PRIMARY KEY,
                                       name TEXT NOT NULL,
                                       joiningDate timestamp);'''

        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_create_table_query)

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'new_developers'
                          ('id', 'name', 'joiningDate') 
                          VALUES (?, ?, ?);"""

        data_tuple = (id, name, joiningDate)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Developer added successfully \n")

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
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

addDeveloper(1, 'Mark', datetime.datetime.now())