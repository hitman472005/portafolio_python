from datetime import datetime

fecha1 = datetime.strptime(input("ingrese la primera fecha: "), "%d/%m/%Y")
fecha2 = datetime.strptime(input("ingrese la segunda fecha: "), "%d/%m/%Y")

dias = fecha1 - fecha2

print("cantidad de dias diferente son:" , abs(dias.days)) 