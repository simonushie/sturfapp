from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def show_query(title, qry):
    print('%s' % (title))
    cur.execute(qry)
    for row in cur.fetchall():
        print(row)
    print('')

dbname = 'sturf_database'
print('connecting to default database ...')
con = connect(user ='postgres', host = 'localhost', password = 'linkinparker99', port=5432)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
show_query('current database', 'SELECT current_database()')
# cur.execute('CREATE DATABASE ' + dbname)
show_query('available databases', 'SELECT * FROM pg_database')
cur.close()
con.close()

print('connecting to %s ...' % (dbname))
con = connect(user ='postgres', database=dbname, host = 'localhost', password = 'linkinparker99', port=5432)
cur = con.cursor()
show_query('current database', 'SELECT current_database()')
cur.close()
con.close()
