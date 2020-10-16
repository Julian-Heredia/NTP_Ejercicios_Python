from datetime import date

from datetime import datetime

Fecha_Nacimiento = date(2000, 8, 18)

fecha_actual = date.today()

calculo_fecha = (fecha_actual.year-Fecha_Nacimiento.year) * 12 + fecha_actual.month - Fecha_Nacimiento.month

print("Han pasado " + str(calculo_fecha) + " meses desde tu nacimiento " + str(Fecha_Nacimiento) + " hasta ahora " + str(fecha_actual))

