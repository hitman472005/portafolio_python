from datetime import date
    
fecha_llegada = input("ingrese la fecha de llegadada: ")
fecha_salida = input("ingrese la fecha de Salida: ")
#****************************************************************************Fecha
slach_1 = fecha_llegada.split('/')

dia_e = int(slach_1[0])
mes_e = int(slach_1[1])
ano_e = int(slach_1[2])

P1_Fecha = date(ano_e , mes_e, dia_e)

slach_2 = fecha_salida.split('/')
dia_s = int(slach_2[0])
mes_s = int(slach_2[1])
ano_s = int(slach_2[2])

P2_Fecha = date(ano_s, mes_s, dia_s )

cantidad_dias_Duraras = abs(P1_Fecha - P2_Fecha).days