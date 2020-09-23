import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='roxana',
            db='orangehrm_mysql'
        )

        self.cursor = self.connection.cursor()
        print('conexion extablecida')

    def select_user(self):
        sql = 'SELECT * FROM hs_hr_employee'
        self.cursor.execute(sql)
        registers = self.cursor.fetchall()
        print(registers)

database = DataBase()
database.select_user()
