from datetime import datetime
from datetime import timedelta
from lib.pages.random_data import GeneratorRandomData
from lib.pages.query_employee import DataBase
from random import randint
import os
import json


class ContactDetails(GeneratorRandomData):

    def __init__(self):

        self.data_parameters = ''
        with open(os.getcwd() + "/BDD-TestApi/features/lib/data/data.json") as file:
            self.data_parameters = json.load(file)

    def address_street1(self):

        return self.random_name(8) + 'S/N'

    def address_street2(self):

        return self.random_name(8) + 'S/N'

    def city(self):

        return self.data_parameters["city"]

    def state(self):

        return self.data_parameters["state"]

    def zip(self):

        return str(randint(1, 9999999))

    def country(self):

        return self.data_parameters["country"]

    def home_telephone(self):

        return '9' + str(randint(1, 999999999))

    def work_telephone(self):

        return '9' + str(randint(1, 999999999))

    def mobile(self):

        return '6' + str(randint(1, 999999999))

    def work_email(self):

        return self.random_email(5)+'@'+self.random_email(5)+'.es'

    def other_email(self):
        return self.random_email(5) + '@' + self.random_email(5) + '.com'



