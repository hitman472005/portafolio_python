import os
def bucle():

    os.system("cls")

    print("\n************************************")
    print("\n******* Angel Steven G.F #16 *******")
    print("\n************************************")

    listaxd = []


    print("\n************************************")
    print("\n*******     Opciones         *******")
    print("\n************************************")
    print("\n*          1-  mayor que           *")
    print("\n*          2-  menor que           *")
    print("\n*          3-  maximo              *")
    print("\n*          4-  minimo              *")
    print("\n************************************")


    tipo_de_operacion = int (input("Elija el tipo de operacion a realizar operacion: "))
   
    if  tipo_de_operacion == 1:
        
        numero = int (input("ingrese el primer numero: "))
        numero2 = int (input("ingrese el segundo numero: "))

        if numero > numero2:
            print (f"el numero mayor es: {numero}")
        elif numero2 > numero:
            print (f"el numero mayor es: {numero2}")
        

    elif tipo_de_operacion == 2:
        numero = int (input("ingrese el primer numero: "))
        numero2 = int (input("ingrese el segundo numero: "))

        if numero < numero2:
            print (f"el numero menor es: {numero}")
        elif numero2 < numero:
            print (f"el numero menor es: {numero2}")

    elif tipo_de_operacion == 3:

        maximo = 0
        turno = 0
        os.system("cls")
        cantidad_de_numeros = int(input("ingrese la cantidad de numeros para la operacion: "))
        
        
        
        os.system("cls")
        
        for cantidad in range(cantidad_de_numeros):
            turno = turno + 1
            numero_ingrese = float(input("ingresa el " +str(turno) + ". numero: "))
            listaxd.append(numero_ingrese)
        
        for cantidad in range(1,5):
            maximo = max(listaxd)

        os.system("cls")

        print(f"El numero mayor es: {maximo}")
        print()

    elif tipo_de_operacion == 4:

        minimo = 0
        turno2 = 0
        os.system("cls")
        cantidad_de_numeros2 = int(input("ingrese la cantidad de numeros para la operacion: "))
        
        
        
        os.system("cls")
        
        for cantidad2 in range(cantidad_de_numeros2):
            turno2 = turno2 + 1
            numero_ingrese = float(input("ingresa el " +str(turno2) + ". numero: "))
            listaxd.append(numero_ingrese)
        
        for cantidad2 in range(1,5):
            minimo = max(listaxd)

        os.system("cls")

        print(f"El numero menor es: {minimo}")
        print()

    else:
        print("La opcion que eligio no existe")

    pc = input("quiere volver a hacer una operacion? (S o N): ")

    if(pc == "s") or (pc == "S"):
        return bucle()
    else:
        return

bucle()