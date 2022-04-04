import gradebook_sql
from gradebook_csv import Gradebook_csv
import query_and_data as qd

#Create a database connection object
c1 = gradebook_sql.gradebook_sql_connection()
g_csv = Gradebook_csv()

def main():
    print("""   ____     ____        _      ____  U _____ u   ____     U  ___ u   U  ___ u   _  __    
U /"___|uU |  _"\ u U  /"\  u |  _"\ \| ___"|/U | __")u    \/"_ \/    \/"_ \/  |"|/ /    
\| |  _ / \| |_) |/  \/ _ \/ /| | | | |  _|"   \|  _ \/    | | | |    | | | |  | ' /     
 | |_| |   |  _ <    / ___ \ U| |_| |\| |___    | |_) |.-,_| |_| |.-,_| |_| |U/| . \\u   
  \____|   |_| \_\  /_/   \_\ |____/ u|_____|   |____/  \_)-\___/  \_)-\___/   |_|\_\    
  _)(|_    //   \\_  \\    >>  |||_   <<   >>  _|| \\_       \\         \\   ,-,>> \\,-. 
 (__)__)  (__)  (__)(__)  (__)(__)_) (__) (__)(__) (__)     (__)       (__)   \.)   (_/ """)

    # Drop all tables
    qd.drop_all_tables()
    # Create all tables
    qd.create_school_table()
    qd.create_class_table()
    qd.create_student_table()
    qd.create_test_table()
    qd.create_enrollment_table()
    qd.get_data_from_table('student')
    qd.get_class('AI101')
   # qd.table_to_csv('student')


    #c1.createTable("NewClass")
    #c1.createTable("Classes")
    
    #c1.create_new_table(g_csv.get_school_table_query())
    #q,d = g_csv.insert_data_in_school_table()
    # print(c1.get_tables)
    # g_csv.create_tables(c1)
    # g_csv.insert_data_in_school_table(c1)
    # #print(q,d)
    # #c1.insert_all_data(q,d)
    # print(c1.get_tables())



if __name__ == "__main__":
    main()
    