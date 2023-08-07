from msvcrt import LK_LOCK


print("*************************")
print("*    Angel Steven #16   *")
print("*************************")

def main():
    suma = 0
    nnum = []
    monto = 1000
    for i  in range(0, monto):
        LL = int(input(f"Escriba el precio del articulo numero {i+1}: "))
        if LL > 0:
            
            nnum.append(LL)
        elif LL == 0:
            print("lo siento no se puede guardar\n")
            break
        else:
            print("cantidad no valida")
            continue
    for i in nnum:
        suma += i
        
    if suma > 1000:
        print("se le aplicara un descuento de 10%, gracias por preferirnos y gastar mas de 1000 pesos")
        r = suma * 0.10
        rr = suma -r
        print(f"sin descuento es:{suma}")
        print(f"con descuento es: {rr}")
    else:
        print(f"total es: {suma}")
main()

