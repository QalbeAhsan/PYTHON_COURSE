import sqlite3

# Connect to the database
conn = sqlite3.connect("employes.db")
c = conn.cursor()



# Insert records into the 'employes' table (Method 1)
c.execute('''INSERT INTO employes (name,status,pay) VALUES('ammar','principal',100)''')
c.execute('''INSERT INTO employes(name,status,pay) VALUES('hasham','middle student',550)''')
c.execute('''INSERT INTO employes(name,status,pay) VALUES('haseeb','businessman',700)''')
c.execute('''INSERT INTO employes(name,status,pay) VALUES('umer bhai','ceo',200)''')
c.execute('''INSERT INTO employes(name,status,pay) VALUES('ateeq','doctor',600)''')

print("Method 1 Command Executed Successfully:")




# Insert records into the 'employes' table (Method 2)
many_employes = [
    (6,"ahsan", "developer", 76),
    (7,"ahmad", "cs", 55),
    (8,"afnan", "hafiz", 70),
    (9,"hamzu bhai", "manager", 20),
    (10,"hanzala", "dealer", 80),
    (11,"amar", "student", 66),
]

c.executemany("INSERT INTO employes VALUES (?,?,?,?)",many_employes)
print("Method2 Command Executed Succesfully")

conn.commit()
c.close()
