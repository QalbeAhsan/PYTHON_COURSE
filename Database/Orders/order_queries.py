import sqlite3

#FUNCTION TO CREATE TABLE :
def create_table(name, price, address,receiver):
 conn = sqlite3.connect("orders.db")
 c = conn.cursor()
 c.execute(
        """
            CREATE TABLE IF NOT EXISTS orders(
            name TEXT,
            price FLOAT,
            address TEXT,
            reciever TEXT
              )
         """
    )
 

#FUNCTION TO INSERT RECORDS(Method 1):
def insert_one(name,price,address,reciever):
 conn = sqlite3.connect("orders.db")
 c = conn.cursor()
 c.execute("INSERT INTO orders VALUES (?,?,?,?)",(name,price,address,reciever))
 conn.commit()
 c.close()


#FUNCTION TO INSERT RECORDS (Method 2):
def insert_many(list):
 conn=sqlite3.connect("orders.db")
 c=conn.cursor()

 c.executemany("INSERT INTO orders VALUES(?,?,?,?)",(list))

 conn.commit()
 c.close()


#FUNCTION TO SHOW DETAILS:
def show_details():

 conn = sqlite3.connect("orders.db")
 c = conn.cursor()
 c.execute('''SELECT * FROM orders''')
 details=c.fetchall()
 for detail in details:
  print(detail)
 conn.close()
 



