import sqlite3
import datetime
import time





####################
##Lightstatus Tab##
####################




#database creation of lightstatus table for the endpoint

# def create_table():

#     conn = sqlite3.connect('data/lightStatus.db', detect_types=sqlite3.PARSE_DECLTYPES |
#                                            sqlite3.PARSE_COLNAMES)
#     print("database file has been created")
#     # cur = conn.cursor()
#     # cur.execute()

#     conn.execute('DROP TABLE IF EXISTS lightStatus')
#     print('droping any existing tables')

#     conn.execute('''CREATE TABLE lightStatus(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         location TEXT NOT NULL,
#         period REAL,
#         state TEXT NOT NULL
# );''')
#     print ('table created sucessfully ')


#     unix = int(time.time())
    





#     conn.execute("INSERT INTO lightStatus (id,location,state,period) VALUES (?,?,?,?)",(1, 'campus', 'on', unix))
#     conn.execute("INSERT INTO lightStatus (id,location,state,period) VALUES  (?,?,?,?)", (2, 'offcampus', 'on', unix))
#     print('insert operation successful')

#     conn.commit()
#     print('database fully commited')

#     cur = conn.cursor()
#     # cur.execute("SELECT * FROM lightStatus")

#     era = cur.execute('SELECT period FROM lightStatus WHERE id = 1')

#     new  = int(cur.fetchone()[0])
    
#     print(type(new))


#     conn.close()
#     print('connection has been closed')



   
# create_table()
















####################
### Records Table ###
####################




## this is code to create the records table


def create_records():
    conn = sqlite3.connect('blueprints/history/records.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
    print("connected to new RECORDS database")
    # cur = conn.cursor()
    # cur.execute()

    conn.execute('DROP TABLE IF EXISTS records')

    conn.execute('''CREATE TABLE records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT NOT NULL,
        state TEXT NOT NULL,
        period TEXT NOT NULL
);''')
    print ('table created sucessfully ')


    stamp = int(time.time())
    date = datetime.datetime.fromtimestamp(stamp)
    date_string = date.strftime("%A") + " " + date.strftime("%I") + ":" + date.strftime("%M")  + date.strftime("%p")
    





    conn.execute("INSERT INTO records (id,location,state,period) VALUES (?,?,?,?)",(1, 'campus', 'on', date_string))
    # conn.execute("INSERT INTO lightStatus (id,location,state,period) VALUES  (?,?,?,?)", (2, 'offcampus', 'on', unix))
    print('insert operation successful')

    conn.commit()
    print('database fully commited')

    cur = conn.cursor()
    # cur.execute("SELECT * FROM lightStatus")

    era = cur.execute('SELECT period FROM records WHERE id = 1')

    new  = str(cur.fetchone()[0])

    print(new)
    
    print(type(new))


    conn.close()
    print('connection to records database has been closed')


create_records()








