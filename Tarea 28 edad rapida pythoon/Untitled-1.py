import os

def main():
    print("Elija una opcion mi bro")
    print("1. si quiere saber tiempo en que nacio")
    print("2. quiere saber edad")
    
    opcion = input("Escriba una opcion: ")
    if opcion == "1":
        Edad = int(input("diga su edad: "))
        tiempo_total = 2022
        print(f"Usted nacio en {tiempo_total - Edad}")

        print()
        print()
        Salir = input("Confirmar Salida S/N ")
            
        if(Salir == "N") or (Salir == "n"):
            os.system("cls")
            return main()


    elif opcion == "2":
        Edad = int(input("diga su Fecha de nacimiento: "))
        tiempo_total = 2022
        print(f"su edad es {tiempo_total - Edad}")
        
        print()
        print()

        Salir = input("Confirmar Salida S/N ")
            
        if(Salir == "N") or (Salir == "n"):
            os.system("cls")
            return main()
        
main()
