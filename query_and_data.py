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

    school_dict = (school_df.to_dict('records'))
    school_data = []
    for dictionary in school_dict:
        l =[]
        for key in dictionary:
            if key == 'SchoolID':
                pass
            else:
                l.append(dictionary[key])
        school_data.append(tuple(l))
    mycursor.executemany(insert_school_query, school_data)
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

    class_dict = (class_df.to_dict('records'))
    class_data = []
    for dictionary in class_dict:
        class_data.append(tuple(dictionary.values()))
    
    mycursor.executemany(insert_class_query, class_data)
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

    student_dict = (student_df.to_dict('records'))
    student_data = []
    for dictionary in student_dict:
        student_data.append(tuple(dictionary.values()))
    
    mycursor.executemany(insert_student_query, student_data)
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

    test_dict = (test_df.to_dict('records'))
    test_data = []
    for dictionary in test_dict:
        test_data.append(tuple(dictionary.values()))

    mycursor.executemany(insert_test_query, test_data)
    db.commit()

#Drop a single tabel
def dropTable(table):
    mycursor.execute("DROP TABLE " + table)

def drop_all_tables():
    all_tables = get_tables()
    for x in all_tables:
        dropTable(x)

#Returns a list of all tables in the database
def get_tables():
    tables = list()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        tables.append(x[0])
    
    return (tables)

# closing database connection





    







