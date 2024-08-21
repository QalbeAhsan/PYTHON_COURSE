import sqlite3

# Connect to an SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the 'students' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
''')

# Insert some records into the 'students' table
cursor.execute( '''INSERT INTO students (name, age, grade) VALUES ('John Doe', 20, 'A')''')
cursor.execute(''' INSERT INTO students (name, age, grade) VALUES ('Jane Smith', 22, 'B')''')
cursor.execute(''' INSERT INTO students (name, age, grade) VALUES ('Emily Davis', 21, 'A')''')

# Commit the transaction
conn.commit()

# Retrieve all data from the 'students' table
cursor.execute('''SELECT * FROM students''')
rows = cursor.fetchall()

# Print the retrieved data
print("All Students:")
for row in rows:
    print(row)

# Retrieve data with a condition (students with grade 'A')
cursor.execute('''SELECT * FROM students WHERE grade = ('A',)''')
rows = cursor.fetchall()

# Print the retrieved data
print("\nStudents with Grade A:")
for row in rows:
    print(row)

# Update a student's grade
cursor.execute('''UPDATE students SET grade = ? WHERE name = ?''', ('A+', 'Jane Smith'))

# Commit the transaction
conn.commit()

# Retrieve data again to see the updated record
cursor.execute('''SELECT * FROM students''')
rows = cursor.fetchall()

# Print the updated data
print("\nUpdated Students List:")
for row in rows:
    print(row)

# Delete a student record
cursor.execute('''DELETE FROM students WHERE name = ('John Doe',)''')

# Commit the transaction
conn.commit()

# Retrieve data again to see the final records
cursor.execute('''SELECT * FROM students''')
rows = cursor.fetchall()

# Print the final data
print("\nFinal Students List After Deletion:")
for row in rows:
    print(row)

# Close the connection
conn.close()
