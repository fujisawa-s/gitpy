
import mysql.connector 

class LoggingDT:
    def __init__(self, user, password, host, database):
        self.mysql_connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.mysql_connection.cursor()

    def insert_student(self, student_info):
        sql = "INSERT INTO Students (StudentID, Name, City) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, student_info)
    
    def show_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        values = self.cursor.fetchall()
        for student in values:
            print(student)

db_manager = DBManager('root', 'sylviaZXY_710412', 'localhost', 'multi_customer_locationDB')


#写入新信息
students = [
    (6, 'Frank', 'Beijing'),
    (7, 'Alice', 'Tokyo'),
]
for student in students:
    db_manager.insert_student(student)
# Check students
db_manager.show_data("Students")