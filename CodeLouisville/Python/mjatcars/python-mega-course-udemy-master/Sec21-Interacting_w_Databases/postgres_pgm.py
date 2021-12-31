import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgrespw' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(i,q,p):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgrespw' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (i,q,p) )
    conn.commit()
    conn.close()
def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgrespw' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(i):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgrespw' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s",(i,)) #Stupid syntax requires comma or item must be passed as a list ([])
    conn.commit()
    conn.close()


def update(q,p,i):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgrespw' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(q,p,i,)) #Stupid syntax requires comma or item must be passed as a list ([])
    conn.commit()
    conn.close()
#create_table()
#insert("Orange",10,1.5)
#print(view())
#delete('Apple')
update(10000,1,'Orange')
#print(view())






