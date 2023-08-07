import os
from re import S
import string

print ("****************************\n")
print ("*   Angel Steven #16       *\n")
print ("****************************\n")

print()

print("*   Bienvenido a su banco popuxd  *\n")

print()

print("               ****************************\n")
print("               *  popuxd banco company xd *\n")
print("               ****************************\n")



sueldo_general = 100000

def hola(sueldo_general):


    clave_determinada = "2005"

    Clave =  input("Ingrese Clave: ")

    if Clave != clave_determinada:
        
        os.system("cls")
        print("*  Reintente de nuevo *\n")
        return hola(sueldo_general)
    else:
        os.system("cls")
    
    print("****************************\n")
    print("*   Opciones de tu cajero  *\n")
    print("*                          *\n")
    print("*  1) introducir dinero    *\n")
    print("*                          *\n")
    print("*  2) Retirar dinero       *\n")
    print("*                          *\n")
    print("*  3) ver Saldo            *\n")
    print("*                          *\n")
    print("*  4) Salir                *\n")
    print("****************************\n")

    opciones = input("ingrese la opcion que desea hacer: ")

    if opciones == "1":

        ingresar = float(input("indique cantidad a ingresar: "))

        sueldo_general = sueldo_general + ingresar
        
        os.system("cls")

        print(f"Cantidad actual en tu cuenta bancaria: {sueldo_general} $ \n")
        print()
        print("Gracias por utilizar su cajero automático")

        print()

        Salir = input("Confirmar Salida S/N ")
        
        print()

        if(Salir == "N") or (Salir == "n"):
            os.system("cls")
            return hola(sueldo_general)


    elif opciones == "2":

        os.system("cls")
        Retirar = float(input("indique cantidad a Retirar: "))

        while Retirar > sueldo_general:
            os.system("cls")
            print("no tiene la cantidad")
            print()
            Retirar = float(input("indique cantidad a Retirar: "))




        sueldo_general = sueldo_general - Retirar

        print(f"Cantidad actual en tu cuenta bancaria: {sueldo_general} $")

        print("Gracias por utilizar su cajero automático")

        print()

        Salir = input("Confirmar Salida S/N ")
        
        print()

        if(Salir == "N") or (Salir == "n"):
            os.system("cls")
            return hola(sueldo_general)

    elif opciones == "3":
        
        os.system("cls")

        print(f"Cantidad actual en tu cuenta bancaria: {sueldo_general} $")
        print()
        print("Gracias por utilizar su cajero automático")

        print()

        Salir = input("Confirmar Salida S/N ")
        
        print()

        if(Salir == "N") or (Salir == "n"):
            
            os.system("cls")
            return hola(sueldo_general)

    elif opciones == "4":

        print("Gracias por utilizar su cajero automático")
        Salir = input("Confirmar Salida S/N ")
            
        if(Salir == "N") or (Salir == "n"):
            os.system("cls")
            return hola(sueldo_general)
                
    else:
        os.system("cls"),
        print("Error, esa opcion no exite, ingrese de nuevo para confirmacion")   
        
        return hola(sueldo_general)



hola(sueldo_general)

    