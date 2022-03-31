# Import libraries
import pandas as pd
import mysql.connector
from mysql.connector import connect, Error

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Gradebook",
        database = "Gradebook"
        )

mycursor = db.cursor()


#read the csvs
school_df = pd.read_csv('./Resources/School.csv')
test_df = pd.read_csv("./Resources/Test.csv")
student_df = pd.read_csv("./Resources/Student.csv")
class_df = pd.read_csv("./Resources/Class.csv")

# Create Schema queries for each table and insert data in each table

# SCHOOL
def create_school_table():
    create_school_table_query = """
    CREATE TABLE school (
        schoolId INT  PRIMARY KEY AUTO_INCREMENT,
        schoolName VARCHAR(100),
        schoolAddress VARCHAR(100)
        )
    """

    mycursor.execute(create_school_table_query)

    insert_school_query = """
    INSERT INTO school
    (schoolName, schoolAddress)
    VALUES (%s, %s)
    """
    
    # Converting dataframe into list of dictionaries, 
    # where each row is a dictionary with column names as the keys
    school_dict = school_df.to_dict('records')

    # school_data is a list of tuples, 
    # where each tuple contains data values corresponding to single row from csv
    school_data = []
    for dictionary in school_dict:
        l =[]
        for key in dictionary:
            # As school_id is auto incremented, so skipping SchoolID column
            if key == 'SchoolID':
                pass
            else:
                l.append(dictionary[key])
        school_data.append(tuple(l))
    
    # Inserting all the rows from csv into table
    mycursor.executemany(insert_school_query, school_data)

    # Commiting inserted data to the database
    db.commit()


# CLASS
def create_class_table():
    create_class_table_query = """
    CREATE TABLE class (
        classId VARCHAR(100)  PRIMARY KEY,
        className VARCHAR(100),
        semester VARCHAR(100)
        )
    """

    mycursor.execute(create_class_table_query)

    insert_class_query = """
    INSERT INTO class
    (classId, className, semester)
    VALUES (%s, %s, %s)
    """
    
    # Converting dataframe into list of dictionaries, 
    # where each row is a dictionary with column names as the keys
    class_dict = (class_df.to_dict('records'))

    # class_data is a list of tuples, 
    # where each tuple contains data values corresponding to single row from csv
    class_data = []
    for dictionary in class_dict:
        class_data.append(tuple(dictionary.values()))
    
    # Inserting all the rows from csv into table
    mycursor.executemany(insert_class_query, class_data)

    # Commiting inserted data to the database
    db.commit()

# STUDENT
def create_student_table():
    create_student_table_query = """
    CREATE TABLE student (
        studentId INT PRIMARY KEY,
        studentName VARCHAR(100),
        email VARCHAR(100)
        )
    """

    mycursor.execute(create_student_table_query)

    insert_student_query = """
    INSERT INTO student
    (studentId, studentName, email)
    VALUES (%s, %s, %s)
    """
    
    # Converting dataframe into list of dictionaries, 
    # where each row is a dictionary with column names as the keys
    student_dict = (student_df.to_dict('records'))

    # student_data is a list of tuples, 
    # where each tuple contains data values corresponding to single row from csv
    student_data = []
    for dictionary in student_dict:
        student_data.append(tuple(dictionary.values()))
    
    # Inserting all the rows from csv into table
    mycursor.executemany(insert_student_query, student_data)

    # Commiting inserted data to the database
    db.commit()

# TEST
def create_test_table():
    create_test_table_query = """
    CREATE TABLE test (
        testId VARCHAR(100)  PRIMARY KEY,
        testName VARCHAR(100),
        studentId INT,
        classId VARCHAR(100),
        score FLOAT,
        FOREIGN KEY(studentId) REFERENCES student(studentId),
        FOREIGN KEY(classId) REFERENCES class(classId)
        )
    """

    mycursor.execute(create_test_table_query)

    insert_test_query = """
    INSERT INTO test
    (testId, testName, studentId, classId, score)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Converting dataframe into list of dictionaries, 
    # where each row is a dictionary with column names as the keys
    test_dict = (test_df.to_dict('records'))

    # test_data is a list of tuples, 
    # where each tuple contains data values corresponding to single row from csv
    test_data = []
    for dictionary in test_dict:
        test_data.append(tuple(dictionary.values()))
    
    # Inserting all the rows from csv into table
    mycursor.executemany(insert_test_query, test_data)

    # Commiting inserted data to the database
    db.commit()

#Drop a single tabel
def dropTable(table):
    mycursor.execute("DROP TABLE " + table)

def drop_all_tables():
    # all_tables = get_tables()
    # for x in all_tables:
    #     dropTable(x)
    dropTable("test")
    dropTable("class")
    dropTable("student")
    dropTable("school")

#Returns a list of all tables in the database
def get_tables():
    tables = list()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        tables.append(x[0])
    
    return (tables)

# Get data from given table
def get_data_from_table(table_name):
    select_query = f"SELECT * FROM {table_name}"
    # mycursor.execute(select_query)
    # for row in mycursor.fetchall():
    #     print(type(row))
    #     print(row)
    result = pd.read_sql(select_query, db)
    print(type(result))
    print(result)
    # SQL_Query = pd.read_sql_query(f"SELECT * FROM {table_name}", db)

    # df = pd.DataFrame(SQL_Query, columns=['studentID', 'student name', 'email'])
    # print(df)
    # print(type(df))

# Get data from given table
def table_to_csv(table_name):
    select_query_csv = f"""SELECT * FROM {table_name}
    INTO OUTFILE './Resources/{table_name}_from_table.csv'
    FIELDS ENCLOSED BY '"' TERMINATED BY ';' ESCAPED BY '"'
    LINES TERMINATED BY '\r\n';
    """
    mycursor.execute(select_query_csv)
   



    







