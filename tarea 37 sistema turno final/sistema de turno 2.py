import random
import time
from time import sleep
from datetime import datetime
import os


lista_turnos = [1,2,3,4,5,6,7,8,9,10]

print("\033[1;32m"+ "     *********************************" + "\033[0;m")
print("\033[1;32m"+ "     *         Trabajo Final         *" + "\033[0;m")
print("\033[1;32m"+ "     *********************************" + "\033[0;m")
print("\033[1;32m"+ "     *       Sistema de turnos       *" + "\033[0;m")
print("\033[1;32m"+ "     *********************************" + "\033[0;m")
print("\033[1;32m"+" *******************************************" + "\033[0;m")
print("\033[1;32m"+" *            Angel Steven #16             *" + "\033[0;m")
print("\033[1;32m"+" *       Marinati Hidalgo feliz #20        *" + "\033[0;m")
print("\033[1;32m"+" *******************************************" + "\033[0;m")
print()


def general():
    
    turno_voy = 0
    
    Ultimo_dato_de_lista =(lista_turnos[-1])
    primer_dato_de_lista =(lista_turnos[0])
    
    print("\033[1;34m"+"bienvenido/a al area de consulta de atencion al cliente" + "\033[0;m")
    print()
    
    escoger_un_turno = int(input ("\033[1;33m"+ f"escoge un turno del 1 al {Ultimo_dato_de_lista}: " + "\033[0;m"))
    
    while escoger_un_turno > Ultimo_dato_de_lista or escoger_un_turno <primer_dato_de_lista :
        os.system("cls")
        print()
        print("\033[1;31m"+"Ha escogido un turno no perteneciente a la lista, sobrepasando los limites de turnos" + "\033[0;m")
        print()
        print("\033[1;32m"+"nuevamente dentro de los limites"+ "\033[0;m")
        print()
        escoger_un_turno = int(input ("\033[1;33m"+ f"escoge un turno del 1 al {Ultimo_dato_de_lista}: "+ "\033[0;m"))
    
    os.system("cls")
    print("\033[1;34m"+ f"A escogido el turno numero {escoger_un_turno} espere por favor..."+ "\033[0;m")
    print()
    print ("\033[1;34m"+"Gracias por preferirnos y lamentamos la espera" + "\033[0;m")
    print()
    time.sleep(3.5)
    
    while turno_voy != escoger_un_turno :
        time.sleep(1.5)
        turno_voy = turno_voy + 1
        print("\033[1;32m"+ f"El turno que acaba de salir es: {turno_voy}"+ "\033[0;m")
        time.sleep(1.0)
        print()
        print("\033[1;35m"+"Espere por favor..."+ "\033[0;m")
        time.sleep(0.9)
    
    if escoger_un_turno == turno_voy:
        
        os.system("cls")
        print()
        print("\033[1;32m"+ f"A Salido su turno el # {escoger_un_turno}!" + "\033[0;m")
        print()
        
        print("\033[1;34m"+"bienvenido y disculpe la espera por su turno\n" + "\033[0;m")

        
        identidad = input("\033[1;33m"+ "ingrese una ID: " +"\033[0;m")
        nombre = input("\033[1;33m"+ "ingrese su nombre: " +"\033[0;m")
        apellido = input("\033[1;33m"+ "ingrese su apellido: "+"\033[0;m")
        fecha_de_dia_de_renta = datetime.strptime(input("\033[1;33m"+"ingrese la fecha de la cita: "+"\033[0;m"), "%d/%m/%Y")  
        
        os.system("cls")
        print("\033[1;32m"+ "***********************************" +"\033[0;m")
        print("\033[1;32m"+"*          Tipo de Cita           *"  +"\033[0;m")
        print("\033[1;32m"+"***********************************" +"\033[0;m")
        print("\033[1;32m"+"*    1. Cita Especial  800$       *" +"\033[0;m")
        print("\033[1;32m"+"*    2. Cita Normal    400$       *" +"\033[0;m")
        print("\033[1;32m"+"***********************************" +"\033[0;m")
        print()
        
        tipo_de_cita = input("\033[1;33m"+"seleccione una opcion de cita: "+"\033[0;m")
        
        precio = 0
        tipo_de_cita_selecionada = ""
        
        if tipo_de_cita =="1":
            precio = precio + 800
            tipo_de_cita_selecionada = "Especial Premium"
        elif tipo_de_cita =="2":
            tipo_de_cita_selecionada = "normal"
            precio = precio + 400
        
        os.system("cls")
        print("\033[1;32m"+"*******************************************"+"\033[0;m")
        print("\033[1;32m"+"*           Tratado de la Cita            *"+"\033[0;m")
        print("\033[1;32m"+"*******************************************"+"\033[0;m")
        print("\033[1;32m"+"*    1. Negocios               700$       *"+"\033[0;m")
        print("\033[1;32m"+"*    2. Atencion al cliente    250$       *"+"\033[0;m")
        print("\033[1;32m"+"*******************************************"+"\033[0;m")
        print()
        
        tratado_de_cita = ""
        accion_cita = input ("\033[1;33m"+"ingrese la opcion: "+"\033[0;m")
        
        
        if accion_cita =="1":
            precio = precio + 700
            tratado_de_cita = "Negocios"
        elif accion_cita =="2":
            tratado_de_cita = "Atencion al cliente"
            precio = precio + 250
        
         
        itebis = precio * 0.18
        Total_itebis = precio + itebis    
        print()
        
        print("\033[1;34m"+"*****************************************"+"\033[0;m")
        print("\033[1;34m"+"     Recibo de Datos almacenandos      "+"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    Identificador  {identidad}       "+"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    Nombre:  {nombre} {apellido}       "+"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    tipo de cita: {tipo_de_cita_selecionada} "+"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    trarado de la cita: {tratado_de_cita} "+"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    fecha de la cita: {fecha_de_dia_de_renta.day}/{fecha_de_dia_de_renta.month}/{fecha_de_dia_de_renta.year} ")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    Total sin Itebis: {precio} "       +"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    Itebis: {itebis} "                 +"\033[0;m")
        print("\033[1;34m"+"                                       "+"\033[0;m")
        print("\033[1;34m"+f"    Total con Itebis: {Total_itebis} "+"\033[0;m")
        print("\033[1;34m"+"                                      "+"\033[0;m")
        print("\033[1;34m"+"*******************************************"+"\033[0;m")
        
        print()
        print()
        
        bl1=("*****************************************")
        bl2=("     Recibo de Datos almacenandos      ")
        bl3=("                                       ")
        bl4=(f"    Identificador  {identidad}        ")
        bl5=("                                       ")
        bl6=(f"    Nombre:  {nombre} {apellido}       ")
        bl7=("                                       ")
        bl8=(f"    tipo de cita: {tipo_de_cita_selecionada} ")
        bl9=("                                       ")
        bl10=(f"    trarado de la cita: {tratado_de_cita} ")
        bl11=("                                       ")
        bl12=(f"    fecha de la cita: {fecha_de_dia_de_renta.day}/{fecha_de_dia_de_renta.month}/{fecha_de_dia_de_renta.year} ")
        bl13=("                                       ")
        bl14=(f"    Total sin Itebis: {precio} ")
        bl15=("                                       ")
        bl16=(f"    Itebis:      {itebis} ")
        bl17=("                                       ")
        bl18=(f"    Total con Itebis: {Total_itebis} ")
        bl19=("                                      ")
        bl20=("*******************************************")
        
        
        
        print("\033[1;32m"+"Se a guardado en el block de notas"+"\033[0;m")
        print()
        print("\033[1;32m"+"Se a guardado en el archivo sql para su futura ejecucion para confirmar guardar los datos"+"\033[0;m")
        
        bloc = open("citas agendadas.txt","a")
        guardado_agenda = f"{bl1}\n{bl2}\n{bl3}\n{bl4}\n{bl5}\n{bl6}\n{bl7}\n{bl8}\n{bl9}\n{bl10}\n{bl11}\n{bl12}\n{bl13}\n{bl14}\n{bl15}\n{bl16}\n{bl17}\n{bl18}\n{bl19}\n{bl20}\n\n\n\n\n"
        bloc.write(guardado_agenda)
        bloc.close()
       
        print()
        print()
        print()
        
        sqlxd = open("Datos de ejecucion almacenados para base de datos.sql","a")
        sqlxd.write("--Asegure el uso de la base de datos\n\n")
        sqlxd.write("use datos_sistema_turno\n\n")
        sqlxd.write("-- Ejecute lo siguiente para la confirmacion de almacenado en la base de datos\n\n")
        sqlxd.write("insert into formulario (id, Nombre, Apellido, tipo_cita, tratado_cita, fecha_cita , total_sin_itebis, Valor_itebis, total_con_itebis)\n")
        sqlxd.write(f"values('{identidad}','{nombre}','{apellido}','{tipo_de_cita}','{tratado_de_cita}','{fecha_de_dia_de_renta.day}/{fecha_de_dia_de_renta.month}/{fecha_de_dia_de_renta.year} ','{precio}','{itebis}','{Total_itebis}')\n")
        sqlxd.close()
        
        opcion_Salir = input("\033[1;33m"+"desea salir del programa S/N: "+"\033[0;m")
        
                
        
        if opcion_Salir == "s" or opcion_Salir == "S":
            os.system("cls")
            os._exit
        elif opcion_Salir == "n" or opcion_Salir == "N":
            os.system("cls")
            return general()
        
general()  
        