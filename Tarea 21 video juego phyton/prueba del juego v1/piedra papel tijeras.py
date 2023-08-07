from os import sep
import random
import time


op = ["piedra", "papel", "tijeras"]
sep = "-" * 15

while True:
    user = input("Elije: piedra, papel o tijeras: ")

    if user not in op:
        print("\nMovimiento no valido")
        continue

    

    pc = random.choice(op)


    
    if user == pc:
        print(f"\nEmpate!, ambos eligieron {user}")

        print(f"\n")
        
    elif user == "piedra" and pc == "tijeras":
        print(f"Ganaste!, {user} ganas en contra de {pc}")
       
        print(f"\n")

        

        print(f"\n")

    elif user == "tijeras" and pc == "papel":
        print(f"Ganaste!, {user} ganas en contra de {pc}")
        
        print(f"\n")

        

        print(f"\n")

    elif user == "papel" and pc == "piedra":
        print(f"Ganaste!, {user} ganas en contra de {pc}")

        print(f"\n")

        print(f"\n")

    else:
     print(f"Perdiste, {user} pierde contra {pc}")

     print(f"\n")

     print(f"{sep} fin del juego xd  {sep}   \n")