import sqlite3
conn = sqlite3.connect("'INSTRUCTOR.db")

Cursor = conn.cursor()
Cursor.execute("DROP TABLE IF EXISTS INSTRUCTOR")

table = """CREATE TABLE INSTRUCTOR(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(50),
    city VARCHAR(50),
    field VARCHAR(50)
)"""

Cursor.execute(table)
print("Table created successfully\n")



insertQuery = """INSERT INTO INSTRUCTOR (name, city, field) VALUES
("John Doe", "New York", "Computer Science"),
("Jane Smith", "Los Angeles", "Mathematics"),
("Emily Davis", "Chicago", "Physics"),
("Michael Brown", "Houston", "Chemistry"),
("Sarah Wilson", "Phoenix", "Biology"),
("David Johnson", "Philadelphia", "History"),
("Laura Garcia", "San Antonio", "English"),
("James Martinez", "San Diego", "Art"),
("Linda Rodriguez", "Dallas", "Music"),
("Robert Lee", "San Jose", "Engineering");
"""
Cursor.execute(insertQuery)

Cursor.execute("SELECT * FROM INSTRUCTOR")
rows = Cursor.fetchall()

for row in rows:
    print(row)