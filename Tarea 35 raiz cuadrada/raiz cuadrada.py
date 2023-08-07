import math
import os

print("*************************")
print("* XD Angel Steven #16 XD*")
print("*************************")

def main(numero):

    while (numero < 0 or numero == 0):

        print ("reintente de nuevo")
        numero = float(input("ingrese el numero al que le sacara la raiz: "))


    print(f'la raiz cuadrada de {numero} es igual a {math.sqrt(numero)}')

    print()    

    opcion = input("desea reintentar: (S o N) ")
    

    if (opcion == "S" ) or (opcion == "s"):
        os.system("cls")
        return main(numero)
    elif (opcion == "N" ) or (opcion == "n"):
        os.system("pause")
numero = float(input("ingrese el numero al que le sacara la raiz: "))
main(numero)