import sqlite3

# Connect to the database
conn = sqlite3.connect("employes.db")
c = conn.cursor()

# Retrieve all records from the 'employes' table
c.execute('''SELECT * FROM employes''')



#details = c.fetchone()
#details = c.fetchmany(2)
#details = c.fetchmany(3)
details=c.fetchall()


# Print each row
for detail in details:
    #print(detail[2])
    print(detail)


# CLOSE THE CONNECTION 
conn.close()