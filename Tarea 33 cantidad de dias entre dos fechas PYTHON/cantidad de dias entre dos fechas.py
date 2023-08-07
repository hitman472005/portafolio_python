
#Angel Steven

#importamos el tiempo de fecha
from datetime import date

fecha_llegada = input("ingrese la fecha de llegadada: ")

#Aqui indicamos que la variable "FECHA DE LLEGADA" se le dividira segun lo que pongamos en split en este caso "/" cuando lo escriban se dividiran en lista de contenedores

slach_1 = fecha_llegada.split('/')

#Segun los espacio que ocupe " 0 1 2" seran lo que ocupe dd/mm/yy

#****************************
#*         Ejemplo          *
#*                          *
#*         dd/mm/yy         *
#*         ↕  ↕   ↕         *
#*         0, 1,  2         *
#****************************

dia_e = int(slach_1[0])
mes_e = int(slach_1[1])
ano_e = int(slach_1[2])


#Nota: Siempre se debe de poner la variable primero
#o inversivo (osea de atras para lante) segun los espcios de los contenedores osea {2 ,1 ,0}
P1_Fecha = date(ano_e , mes_e, dia_e)

print(P1_Fecha)

fecha_salida = input("ingrese la fecha de Salida: ")

slach_2 = fecha_salida.split('/')
dia_s = int(slach_2[0])
mes_s = int(slach_2[1])
ano_s = int(slach_2[2])

P2_Fecha = date(ano_s, mes_s, dia_s )

print(P2_Fecha)

cantidad_dias = P1_Fecha - P2_Fecha

#se pone "ABS" para que salga los numeros en valor absoluto osea que no salgan negativos
print(abs(cantidad_dias.days))
