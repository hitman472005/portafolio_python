import os 
import time


def general():
    
    os.system("cls")
    listaxd = ["1","2","3","4"]
    
    print("*************************************")
    print("*  Selecciona el tipo de operacion  *")
    print("*************************************")
    print("* 1. Sumar                          *")
    print("* 2. Restar                         *")
    print("* 3. Multiplicar                    *")
    print("* 4. Dividir                        *") 
    print("*************************************")
    
    opcion = input("Ingrese el numero de opcion: ")
 
    while (opcion not in listaxd):
        
        os.system("cls")

        print("Esa opcion no existe reintente de nuevo")
        print()
        print("*************************************")
        print("*  Selecciona el tipo de operacion  *")
        print("*************************************")
        print("* 1. Sumar                          *")
        print("* 2. Restar                         *")
        print("* 3. Multiplicar                    *")
        print("* 4. Dividir                        *") 
        print("*************************************")

        opcion = input("Ingrese el numero de opcion: ")
 
    os.system("cls")

    if (opcion == "1"):
        
        s1 = int(input("Introdusca el primer numero: "))
        s2 = int(input("Introdusca el segundo numero: "))

        resultado = s1 + s2

        os.system("cls")

        print(f"La suma es igual a: {resultado}")
        
        print()
        print("para volver a seleccionar opcion")
        os.system("pause")
        return general()
    
    elif (opcion == "2"):
        
        r1 = int(input("Introdusca el primer numero: "))
        r2 = int(input("Introdusca el segundo numero: "))

        os.system("cls")

        resultado = r1 - r2

        print(f"La resta es igual a: {resultado}")
        
        print()
        print("para volver a seleccionar opcion")
        os.system("pause")
        return general()
    
    elif (opcion == "3"):

        m1 = int(input("Introdusca el primer numero: "))
        m2 = int(input("Introdusca el segundo numero: "))

        os.system("cls")

        resultado = m1 * m2

        print(f"La multiplicacion es igual a: {resultado}")
        
        print()
        print("para volver a seleccionar opcion")
        os.system("pause")
        return general()

    elif (opcion == "4"):

        d1 = float(input("Introdusca el primer numero divisor: "))
        d2 = float(input("Introdusca el segundo numero que dividira: "))

        os.system("cls")


        resultado = d1 / d2

        print(f"La divicion es igual a: {resultado}")
        
        print()
        print("para volver a seleccionar opcion")
        os.system("pause")
        return general()

general()