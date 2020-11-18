from datetime import datetime
from datetime import timedelta

#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2000)
format1 = new_date.strftime('%Y-%m-%d')

print(format1)



now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')

format1 = now.strftime('%B %m-%d')
print(format1)


una_fecha = '20/04/2019'
fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
fecha_dt = fecha_dt.strftime('%B %Y')
print(fecha_dt)