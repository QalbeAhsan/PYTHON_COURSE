import sqlite3

# Connect to the database
conn = sqlite3.connect("employes.db")
c = conn.cursor()

# Create the 'employes' table if it doesn't exist
c.execute(
    """
    CREATE TABLE IF NOT EXISTS employes(
        id INTEGER PRIMARY KEY,
        name TEXT, 
        status TEXT,
        pay FLOAT
    )
    """
)
print("Your Command Executed Succesfully")


conn.commit()
c.close()
