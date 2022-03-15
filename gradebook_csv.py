import pandas as pd


class Gradebook_csv:

    def __init__(self):

        #read the csv
        self.school_df = pd.read_csv("C:/Users/Gradebook/Desktop/Project/Gradebook/Resources/School.csv")
        self.test_df = pd.read_csv("C:/Users/Gradebook/Desktop/Project/Gradebook/Resources/Test.csv")
        self.student_df = pd.read_csv("C:/Users/Gradebook/Desktop/Project/Gradebook/Resources/Student.csv")
        self.class_df = pd.read_csv("C:/Users/Gradebook/Desktop/Project/Gradebook/Resources/Class.csv")
        #self.insert_data_in_school_table()

    def get_school_table_query(self):
        columns = self.school_df.columns.values.tolist()
        #print((columns))
        #Q1 = f"CREATE TABLE School ({columns[0]} int PRIMARY KEY AUTO_INCREMENT, school_name VARCHAR(100), school_address VARCHAR(100))"
        Q1 = f"CREATE TABLE School (school_id int PRIMARY KEY, school_name VARCHAR(100), school_address VARCHAR(100))"
        return Q1
        
    def insert_data_in_school_table(self):
        num_rows = self.school_df.shape[0]
        print(f"num rows: {num_rows}")
        
        data = []
       
        for row in range(num_rows):
            
            school = self.school_df.iloc[row]
            #print(school)
            data.append((school["SchoolID"], school["SchoolName"], school["Address"]))
            Q2 = "INSERT INTO classes (school_id, school_name, school_address) VALUES(%s,%s,%s)"
            print()

        print(f"data: {data}")
        ## cursor.executemany(Q2,data)
        return Q2, data