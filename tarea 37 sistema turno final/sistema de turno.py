import random
import time
from time import sleep
from datetime import datetime
import os


lista_turnos = [1,2,3,4,5,6,7,8,9,10]

print("*********************************")
print("*         Trabajo Final         *")
print("*********************************")
print("*       Sistema de turnos       *")
print("*********************************")
print("*********************************")
print("*       Angel Steven #16        *")
print("*       Marinati       *")
print("*********************************")



def general():
    
    Ultimo_dato_de_lista =(lista_turnos[-1])
    primer_dato_de_lista =(lista_turnos[0])
    
    escoger_un_turno = int(input (f"escoge un turno del 1 al {Ultimo_dato_de_lista}: "))
    
    while escoger_un_turno > Ultimo_dato_de_lista or escoger_un_turno <primer_dato_de_lista :
        os.system("cls")
        print()
        print("Ha escogido un turno no perteneciente a la lista, sobrepasando los limites de turnos")
        print()
        print("nuevamente dentro de los limites")
        print()
        escoger_un_turno = int(input (f"escoge un turno del 1 al {Ultimo_dato_de_lista}: "))
        
    
    
    os.system("cls")
    print(f"A escogido el turno numero {escoger_un_turno} espere por favor...")
    print()
    print ("Gracias por preferirnos y lamentamos la espera")
    time.sleep(3.5)
    turno_consola = random.choice(lista_turnos)
    time.sleep(0.9)
    
    while (turno_consola != escoger_un_turno):
            
            turno_consola = random.choice(lista_turnos)
            print(f"El turno que acaba de salir es: {turno_consola}")
            time.sleep(1.0)
            print()
            print("Espere por favor")
            time.sleep(0.9)
    
    if escoger_un_turno == turno_consola:
        
        os.system("cls")
        print()
        print(f"A Salido su turno el # {escoger_un_turno}!")
        print()
        
        print("bienvenido y disculpe la espera por su turno")

        nombre = input("ingrese su nombre: ")
        apellido = input("ingrese su apellido: ")
        fecha_de_dia_de_renta = datetime.strptime(input("ingrese la fecha de la cita: "), "%d/%m/%Y")  
        
        os.system("cls")
        print("***********************************")
        print("*          Tipo de Cita           *")
        print("***********************************")
        print("*    1. Cita Especial  800$       *")
        print("*    2. Cita Normal    400$       *")
        print("***********************************")
        print()
        
        tipo_de_cita = input("seleccione una opcion de cita: ")
        
        precio = 0
        tipo_de_cita_selecionada = ""
        
        if tipo_de_cita =="1":
            precio = precio + 800
            tipo_de_cita_selecionada = "Especial Premium"
        elif tipo_de_cita =="2":
            tipo_de_cita_selecionada = "normal"
            precio = precio + 400
        
        os.system("cls")
        print("*******************************************")
        print("*           Tratado de la Cita            *")
        print("*******************************************")
        print("*    1. Negocios               700$       *")
        print("*    2. Atencion al cliente    250$       *")
        print("*******************************************")
        print()
        
        tratado_de_cita = ""
        accion_cita = input ("ingrese la opcion: ")
        
        
        if accion_cita =="1":
            precio = precio + 700
            tratado_de_cita = "Negocios"
        elif accion_cita =="2":
            tratado_de_cita = "Atencion al cliente"
            precio = precio + 250
        
         
        itebis = precio * 0.18
        Total_itebis = precio + itebis    
        print()
        
        print("*****************************************")
        print("     Recibo de Datos almacenandos      ")
        print("                                       ")
        print(f"    Nombre:  {nombre} {apellido}       ")
        print("                                       ")
        print(f"    tipo de cita: {tipo_de_cita_selecionada} ")
        print("                                       ")
        print(f"    trarado de la cita: {tratado_de_cita} ")
        print("                                       ")
        print(f"    fecha de la cita: {fecha_de_dia_de_renta.day}/{fecha_de_dia_de_renta.month}/{fecha_de_dia_de_renta.year} ")
        print("                                       ")
        print(f"    Total sin Itebis: {precio} ")
        print("                                       ")
        print(f"    Itebis: {itebis} ")
        print("                                       ")
        print(f"    Total con Itebis: {Total_itebis} ")
        print("                                      ")
        print("*******************************************")


general()    
    