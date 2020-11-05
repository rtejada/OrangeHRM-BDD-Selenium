import pymysql
from dotenv import load_dotenv
import os


class DataBase:

    def __init__(self):
        load_dotenv(os.getcwd() + "/.env.orangeHRM")

        host = os.getenv('HOST')
        user = os.getenv('USER_DB')
        password = os.getenv('PASSWORD')
        db = os.getenv('DB')

        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        self.cursor = self.connection.cursor()

    def get_employee_by_id(self, employee_id):

        try:
            sql = 'SELECT * FROM hs_hr_employee WHERE employee_id=%s'
            value = employee_id
            self.cursor.execute(sql, value)
            result = self.cursor.fetchone()

            return result

        except Exception as e:
            self.connection.rollback()
            print(f'Exception to get employee: {e}')

        finally:
            self.connection.close()

    def get_employee_number(self, employee_number):

        try:
            sql = 'SELECT * FROM hs_hr_employee WHERE emp_number=%s'
            value = employee_number
            self.cursor.execute(sql, value)
            result = self.cursor.fetchone()

            return result

        except Exception as e:
            self.connection.rollback()
            print(f'Exception to get employee: {e}')

        finally:
            self.connection.close()

    def get_salary_component(self, salary_component):

        try:
            sql = 'SELECT * FROM hs_hr_emp_basicsalary WHERE salary_component=%s'
            value = salary_component
            self.cursor.execute(sql, value)
            result = self.cursor.fetchone()

            return result

        except Exception as e:
            self.connection.rollback()
            print(f'Exception to get employee: {e}')

        finally:
            self.connection.close()

