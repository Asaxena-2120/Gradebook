import gradebook_sql
from gradebook_csv import Gradebook_csv

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

    all_tables = c1.get_tables()
    for x in all_tables:
            print(x)
            c1.dropTable(x)
    #c1.createTable("NewClass")
    #c1.createTable("Classes")
    c1.create_new_table(g_csv.get_school_table_query())
    q,d = g_csv.insert_data_in_school_table()
    #print(q,d)
    #c1.insert_all_data(q,d)
    print(c1.get_tables())


if __name__ == "__main__":
    main()