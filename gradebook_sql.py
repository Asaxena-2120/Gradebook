import mysql.connector
from mysql.connector import errorcode

class gradebook_sql_connection:

    #Initalize and connect to an existing database
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Gradebook",
        database = "Gradebook"
        )

        self.mycursor = self.db.cursor()

    #Drop a single tabel
    def dropTable(self, table):
        self.mycursor.execute("DROP TABLE " + table)

    #TODO This does not work
    def dropAllTables(self):
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            drop_statement = "DROP TABLE " + x[0]
            print(drop_statement)
            self.mycursor.execute(drop_statement)

        print("Drop all tables finished")


    #Create Tables (this is probably not useful for real table creation)
    def createTable(self, class_name):
        table = "CREATE TABLE " + class_name + " (class_id int PRIMARY KEY AUTO_INCREMENT, class_name VARCHAR(50), Year int UNSIGNED)"
        #self.mycursor.execute("CREATE TABLE Classes (class_id int PRIMARY KEY AUTO_INCREMENT, class_name VARCHAR(50), Year int UNSIGNED)")
        self.mycursor.execute(table)

    #Prints a lsit of all tables in the database
    def show_tables(self):
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            print(x)

    #Returns a list of all tables in the database
    def get_tables(self):
        tables = list()
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            tables.append(x[0])
        return tables
    
    def execute(self, query):
        self.mycursor.execute(query)

    # Insert all the data in one go
    def insert_all_data(self, query, values):
        self.mycursor.executemany(query,values)
    
    # create new table with a query
    def create_new_table(self,query):
        self.mycursor.execute(query)


