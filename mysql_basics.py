import mysql.connector
from mysql.connector import errorcode
print("mysql")

# Connect to database
# try:
#     db = mysql.connector.connect(
#         host = "localhost", # Since mysql is running on same computer
#         user = "root",
#         passwd = "Gradebook",
#         database = "Gradebook"
#     )
#     mycursor = db.cursor()
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your username or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Databse does not exist")
#         # cursor object using above database
        
#         mycursor.execute("CREATE DATABASE Gradebook") 
#     else:
#         print(err)
# else:
#     db.close()


db = mysql.connector.connect(
        host = "localhost", # Since mysql is running on same computer
        user = "root",
        passwd = "Gradebook",
        database = "Gradebook"
    )
  

# cursor object using above database
mycursor = db.cursor()

# Create a database
#mycursor.execute("CREATE DATABASE Gradebook") 

# Create a classes table
#mycursor.execute("CREATE TABLE Classes (class_id int PRIMARY KEY AUTO_INCREMENT, class_name VARCHAR(50), Year int UNSIGNED)")

# Add rows to table
#mycursor.execute("INSERT INTO classes (class_name, Year) VALUES(%s,%s)", ("Class A", 2021))

# Print data from table
mycursor.execute("SELECT * FROM classes")

# To commit data to table
#db.commit()

# Describe a table
#mycursor.execute("DESCRIBE classes")

# prints information what mycursor got
for x in mycursor:
    print(x)
