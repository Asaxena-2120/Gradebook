import pandas as pd
import gradebook_sql


class Gradebook_csv:

    def __init__(self):

        #read the csv
        self.school_df = pd.read_csv("./Resources/School.csv")
        self.test_df = pd.read_csv("./Resources/Test.csv")
        self.student_df = pd.read_csv("./Resources/Student.csv")
        self.class_df = pd.read_csv("./Resources/Class.csv")
        #self.insert_data_in_school_table()

    def get_school_table_query(self):
        columns = self.school_df.columns.values.tolist()
        #print((columns))
        #Q1 = f"CREATE TABLE School ({columns[0]} int PRIMARY KEY AUTO_INCREMENT, school_name VARCHAR(100), school_address VARCHAR(100))"
        Q1 = f"CREATE TABLE School (school_id int PRIMARY KEY, school_name VARCHAR(100), school_address VARCHAR(100))"
        return Q1

    def create_tables(self, c1):
        c1.execute("CREATE TABLE School (school_id int PRIMARY KEY, school_name VARCHAR(100), school_address VARCHAR(100))")
        
    def insert_data_in_school_table(self, c1):
        num_rows = self.school_df.shape[0]
        print(f"num rows: {num_rows}")
        
        data = []
       
        for row in range(num_rows):
            
            school = self.school_df.iloc[row]
            #print(school)
            data = ((school["SchoolID"], school["SchoolName"], school["Address"]))
            #Q2 = "INSERT INTO school (school_id, school_name, school_address) VALUES(%s,%s,%s)"
            Q2 = "INSERT INTO school VALUES(12, 'Hello', 'Somewhere')"
            c1.execute(Q2)
            print()

        print(f"data: {data}")
        ## cursor.executemany(Q2,data)
        return Q2, data