from datetime import datetime
from datetime import timedelta
from lib.pages.random_data import GeneratorRandomData
from lib.pages.query_employee import DataBase
from random import randint
import os
import json


class EmployeeData(GeneratorRandomData):

    def __init__(self):

        self.data_parameters = ''
        with open(os.getcwd() + "/BDD-TestApi/features/lib/data/data.json") as file:
            self.data_parameters = json.load(file)

    def first_name(self):

        return self.random_name(10)

    def middle_name(self):

        return self.random_name(10)

    def last_name(self):

        return self.random_name(15)

    def code(self):

        return 'ID'+str(randint(1, 50000))

    def dob(self):
        now = datetime.now()
        #format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
        return now.strftime('1980-%m-%d')

    def status(self):

        return self.data_parameters["status"]

    def drivers_license(self):

        return str(randint(10, 2000000000000))

    def license_expire(self):

        now = datetime.now()
        new_date = now + timedelta(days=2000)
        return new_date.strftime('%Y-%m-%d')

    def marital_status(self, m):

        return self.data_parameters["maritalStatus"][m]

    def gender(self, t):

        return self.data_parameters["gender"][t]

    def nationality(self):

        return self.data_parameters["nationality"]

    def job_title(self, i):

        return self.data_parameters["jobTitle"][i]

    def sin_number(self):

        return self.random_name(1).upper() + str(randint(1, 999999999))

    def supervisor(self, id_supervisor):

        query = DataBase()
        employe_info = query.get_employee_number(id_supervisor)
        name = employe_info['emp_firstname'] + ' ' + employe_info['emp_lastname']

        return name

