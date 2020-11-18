from datetime import datetime
from lib.pages.random_data import GeneratorRandomData
from random import randint


class GeneratorDataParameters(GeneratorRandomData):
    '''
    def __init__(self):

        print(os.getcwd())
        self.data_parameters = ''
        with open(os.getcwd() + "/BDD-TestApi/features/lib/data/key_params.json") as file:
            self.data_parameters = json.load(file)
    '''
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



