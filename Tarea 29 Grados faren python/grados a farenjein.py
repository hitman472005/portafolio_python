import os

def fahrenheit_a_celsius(f):
    return (5/9) * (f - 32) 



# Modo de uso


print("***********************************")
print("* Angel Steven Gonzalez Fernandez *")
print("*                                 *")
print("  Programa de Fahrenjeit a celsio *")
print("***********************************")

def main():

    f = float(input("Ingresa los grados Fahrenheit: "))
    c = fahrenheit_a_celsius(f)
    print(f"Los {f} grados Fahrenheit son {c} grados celsius")

    print()
    print()
    print()

    Salir = input("Confirmar Salida S/N ")
                
    if(Salir == "N") or (Salir == "n"):
        os.system("cls")
        return main()

main()
