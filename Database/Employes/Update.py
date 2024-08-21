import sqlite3

# Connect to the database
conn = sqlite3.connect("employes.db")
c = conn.cursor()


#Before we update the data
c.execute('''SELECT * FROM employes WHERE name='ahmad' ''')
details=c.fetchall()
print(details)


#HERE WE UPDATE THE DATA 
c.execute("UPDATE employes SET status='graphic designer' WHERE name='ahmad' ")
print("Your Command For Update Executed Succesfully")


#we have to commit 
conn.commit()

#After we update our data 
c.execute('''SELECT * FROM employes WHERE name='ahmad' ''')
details=c.fetchall()
print(details)

#close it 
conn.close()