def bucle():


    print("\n************************************")
    print("\n******* Angel Steven G.F #16 *******")
    print("\n************************************")



    print("\nbusqueda de mayor, menor, maximo y minimo")

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

        numero = int (input("ingrese el primer numero: "))
        numero2 = int (input("ingrese el segundo numero: "))
        numero3 = int (input("ingrese el tercer numero: "))
        if numero > numero2 and numero2 > numero3:
            print(f"el numero mayor es: {numero}")
        elif numero2 > numero and numero2 > numero3:
            print(f"el numero mayor es:  {numero2}")
        elif numero3 > numero2 and numero3 > numero2:
            print(f"el numero mayor es:  {numero3}")

    elif tipo_de_operacion == 4:

        numero = int (input("ingrese el primer numero: "))
        numero2 = int (input("ingrese el segundo numero: "))
        numero3 = int (input("ingrese el tercer numero: "))
        if numero < numero2 and numero2 < numero3:
            print(f"el numero menor es: {numero}")
        elif numero2 < numero and numero2 < numero3:
            print(f"el numero menor es:  {numero2}")
        elif numero3 < numero2 and numero3 < numero2:
            print(f"el numero menor es:  {numero3}")

    else:
        print("La opcion que eligio no existe")

    pc = input("quiere volver a hacer una operacion?: ")

    if(pc == "s") or (pc == "S"):
        return bucle()
    else:
        return

bucle()