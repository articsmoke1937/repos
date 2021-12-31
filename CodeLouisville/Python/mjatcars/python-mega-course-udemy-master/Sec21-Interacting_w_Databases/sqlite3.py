import sqlite3

def create_table():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
 
def insert(i,q,p):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(i,q,p))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(i):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?",(i,)) #Stupid syntax requires comma or item must be passed as a list ([])
    conn.commit()
    conn.close()


def update(q,p,i):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(q,p,i,)) #Stupid syntax requires comma or item must be passed as a list ([])
    conn.commit()
    conn.close()

update(10000,1,'Water Glass')
#delete('Wine Glass')
print(view())









