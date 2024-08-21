import sqlite3

# Connect to the database
conn = sqlite3.connect("employes.db")
c = conn.cursor()



c.execute("DELETE FROM employes WHERE id=11")
print("DELETE COMMAND EXECUTED SUCCESSFULLY")

conn.commit()
conn.close()