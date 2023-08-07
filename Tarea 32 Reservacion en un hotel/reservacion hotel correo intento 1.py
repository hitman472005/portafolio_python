from datetime import datetime
import smtplib
import os


  

def main():

    print()
    print()
    print()


    reservacion = 0
    personas_total = 0
    resultado_total = 0


    
    nombre = input("Ingrese su nombre: ")
    Apellido = input("Ingrese su Apellido: ")
    correo = input("Ingrese su correo electronico: ")
    
    print()
    print("La Duracion de noches vale 100")
    print()

   
#****************************************************************************   Fecha
    fecha_llegada = datetime.strptime(input("ingrese la fecha de llegadada: "), "%d/%m/%Y")
    fecha_salida = datetime.strptime(input("ingrese la fecha de Salida: "), "%d/%m/%Y")

    dias = fecha_llegada - fecha_salida

    cantidad_dias_Duraras = abs(fecha_llegada - fecha_salida).days

    print("cantidad de dias que se ospeda en el hotel son:" , abs(dias.days)) 

    print()
#****************************************************************************


    Cantidad_persona = int(input("Ingrese la cantidad de personas: "))
    
    cantidad_de_dias = cantidad_dias_Duraras * 100

    reservacion = reservacion + cantidad_de_dias
    
    

    hijos = input("Anda con niños (S o N) ")
    
    Cantidad_hijos = 0
    
    if (hijos == "S") or  (hijos == "s"):
        
        Cantidad_hijos = int(input("Ingrese la cantidad de niños: "))

        personas_total = Cantidad_persona + Cantidad_hijos

    elif (hijos == "N") or  (hijos == "n"):
        personas_total = personas_total + Cantidad_persona

    else:
      pass
        
    print()
    
    print()

    print ("*****************************")
    print (" 1. habitacion premium 300$ *")
    print (" 2. habitacion normal 200$  *")
    print ("*****************************")
    
    print()
 
    opcion = input("indica el tipo de habitacion: ")
    
    if opcion == "1":

        reservacion = reservacion + 300
        
        resultado_total = reservacion * personas_total

        tipo_habitacion = "Premium"

        resultado_total_ITBIS = resultado_total * 0.18

        itebis1 = (cantidad_dias_Duraras * 300 * personas_total) * 0.18 + resultado_total

        print()
        print("Exelente eleccion")
        print()
        print()
        print(" ************************************************************************************")
        print("                         Resultado de almacenado la recervacion                      ")
        print("                                                                                     ")
        print(f"  Nombre Completo V. : {nombre} {Apellido}                                          ")
        print("                                                                                     ")
        print(f"  Fecha de entrada :  {fecha_llegada.day}/{fecha_llegada.month}/{fecha_llegada.year}")
        print("                                                                                     ")
        print(f"  Fecha de salida :  {fecha_salida.day}/{fecha_salida.month}/{fecha_salida.year}    ")
        print("                                                                                     ")
        print(f"  tiempo que tardara en el hotel : {cantidad_dias_Duraras} dias                     ")
        print("                                                                                     ")
        print(f"  Tipo de Habitacion solicitada :  {tipo_habitacion}                                ")
        print("                                                                                     ")
        print(f"  Cantidad de personas (Adultas) : {Cantidad_persona}                               ")
        print("                                                                                     ")
        print(f"  Cantidad de niños : {Cantidad_hijos}                                              ")
        print("                                                                                     ")
        print(f"  Personas en total : {personas_total}                                              ")
        print("                                                                                     ")
        print(f"  Precio Total sin ITBIS : {resultado_total}                                        ")
        print("                                                                                     ")
        print(f"  ITEBIS:  {itebis1}                                                                ")
        print("                                                                                     ")
        print(f"  Precio Total con ITBIS : {resultado_total_ITBIS}                                  ")
        print("                                                                                     ")
        print("*************************************************************************************")
        print()
        print()
        print()

        conexion = smtplib.SMTP('smtp.gmail.com', 587)
        conexion.ehlo()
        conexion.starttls()


        l1=  "****************************************************************************************\n"
        l2=  "*                        Resultado de almacenado la recervacion                         \n"
        l3=  "*                                                                                       \n"
        l4=  f"*  Nombre Completo V. : {nombre} {Apellido}                                            \n"
        l5=  "*                                                                                       \n"
        l6=  f"*  Fecha de entrada :  {fecha_llegada.day}/{fecha_llegada.month}/{fecha_llegada.year}  \n"
        l7=  " *                                                                                      \n"
        l8=  f"*  Fecha de salida :  {fecha_salida.day}/{fecha_salida.month}/{fecha_salida.year}      \n"
        l9=   "*                                                                                      \n"
        l10= f"*  tiempo que tardara en el hotel : {cantidad_dias_Duraras} dias                       \n"
        l11= "*                                                                                       \n"
        l12= f"*  Tipo de Habitacion solicitada :  {tipo_habitacion}                                  \n"
        l13= "*                                                                                       \n"
        l14= f"*  Cantidad de personas (Adultas) : {Cantidad_persona}                                 \n"
        l15= "*                                                                                       \n"
        l16= f"*  Cantidad de infantes : {Cantidad_hijos}                                             \n"
        l17= "*                                                                                       \n"
        l18= f"*  Personas en total : {personas_total}                                                \n"
        l19= "*                                                                                       \n"
        l20= f"*  Precio Total sin ITBIS : {resultado_total}                                          \n"
        l21= "*                                                                                       \n"
        l22= f"*  ITEBIS:  {itebis1}                                                                  \n"
        l23= "*                                                                                       \n"
        l24= f"*  Precio Total con ITBIS : {resultado_total_ITBIS}                                    \n"
        l25 ="*                                                                                       \n"
        l26 ="****************************************************************************************"

        conexion.login('angelstevengonzalezf@gmail.com','angelsteven2806')

        mensajexd = f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}\n{l8}\n{l9}\n{l10}\n{l11}\n{l12}\n{l13}\n{l14}\n{l15}\n{l16}\n{l17}\n{l18}\n{l19}\n{l20}\n{l21}\n{l22}\n{l23}\n{l24}\n{l25}\n{l26}\n"

        print ("Se esta a enviado mensaje de recibo al correo electronico")
        conexion.sendmail('angelstevengonzalezf@gmail.com', correo , msg = mensajexd )

        print()
        print("Se a enviado correctamente y gracias por preferirnos")
        print()

        conexion.quit()
        print()
        print()
        print()
        Salir = input("Desea continuar con el siguiente visitante S/N  ")
            
        if(Salir == "S") or (Salir == "s"):
            os.system("cls")
            return main()

            
        elif(Salir == "N") or (Salir == "n"):
             os.system("pause")            
        else:
            print("esa opcion no exite")
            os.system("cls")
            return main()
       
            

    elif opcion == "2":
        
        reservacion = reservacion + 200

        resultado_total = reservacion * personas_total

        tipo_habitacion = "Normal"

        resultado_total_ITBIS = resultado_total * 0.18

        itebis2 = (cantidad_dias_Duraras * 200 * personas_total) * 0.18 + resultado_total

        print()
        print("Buena eleccion")
        print()
        print(" ************************************************************************************")
        print("                         Resultado de almacenado la recervacion                      ")
        print("                                                                                     ")
        print(f"  Nombre Completo V. : {nombre} {Apellido}                                          ")
        print("                                                                                     ")
        print(f"  Fecha de entrada :  {fecha_llegada.day}/{fecha_llegada.month}/{fecha_llegada.year}")
        print("                                                                                     ")
        print(f"  Fecha de salida :  {fecha_salida.day}/{fecha_salida.month}/{fecha_salida.year}    ")
        print("                                                                                     ")
        print(f"  tiempo que tardara en el hotel : {cantidad_dias_Duraras} dias                     ")
        print("                                                                                     ")
        print(f"  Tipo de Habitacion solicitada :  {tipo_habitacion}                                ")
        print("                                                                                     ")
        print(f"  Cantidad de personas (Adultas) : {Cantidad_persona}                               ")
        print("                                                                                     ")
        print(f"  Cantidad de niños : {Cantidad_hijos}                                              ")
        print("                                                                                     ")
        print(f"  Personas en total : {personas_total}                                              ")
        print("                                                                                     ")
        print(f"  Precio Total sin ITBIS : {resultado_total}                                        ")
        print("                                                                                     ")
        print(f"  ITEBIS:  {itebis2}                                                                 ")
        print("                                                                                     ")
        print(f"  Precio Total con ITBIS : {resultado_total_ITBIS}                                  ")
        print("                                                                                     ")
        print("*************************************************************************************")
        print()
        print()
        print()

        conexion = smtplib.SMTP('smtp.gmail.com', 587)
        conexion.ehlo()
        conexion.starttls()

        l1=  "**************************************************************************************\n"
        l2=  "*                        Resultado de almacenado la recervacion                      *\n"
        l3=  "*                                                                                    *\n"
        l4=  f"*  Nombre Completo V. : {nombre} {Apellido}                                          *\n"
        l5=  "*                                                                                    *\n"
        l6=  f"*  Fecha de entrada :  {fecha_llegada.day}/{fecha_llegada.month}/{fecha_llegada.year}*\n"
        l7=  " *                                                                                    *\n"
        l8=  f"*  Fecha de salida :  {fecha_salida.day}/{fecha_salida.month}/{fecha_salida.year}    *\n"
        l9=   "*                                                                                    *\n"
        l10= f"*  tiempo que tardara en el hotel : {cantidad_dias_Duraras} dias                     *\n"
        l11= "*                                                                                    *\n"
        l12= f"*  Tipo de Habitacion solicitada :  {tipo_habitacion}                                *\n" 
        l13= "*                                                                                    *\n"
        l14= f"*  Cantidad de personas (Adultas) : {Cantidad_persona}                               *\n"
        l15= "*                                                                                    *\n"
        l16= f"*  Cantidad de infantes : {Cantidad_hijos}                                           *\n"
        l17= "*                                                                                    *\n"
        l18= f"*  Personas en total : {personas_total}                                              *\n"
        l19= "*                                                                                    *\n"
        l20= f"*  Precio Total sin ITBIS : {resultado_total}                                        *\n"
        l21= "*                                                                                    *\n"
        l22= f"   ITEBIS:  {itebis2}                                                                 *\n"
        l23= "                                                                                      *\n"
        l24= f"*  Precio Total con ITBIS : {resultado_total_ITBIS}                                  *\n"
        l25 ="*                                                                                    *\n"
        l26 ="***************************************************************************************"

        conexion.login('angelstevengonzalezf@gmail.com','angelsteven2806')

        
        mensajexd = f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}\n{l8}\n{l9}\n{l10}\n{l11}\n{l12}\n{l13}\n{l14}\n{l15}\n{l16}\n{l17}\n{l18}\n{l19}\n\{l20}\n{l21}\n{l22}\n{l23}\n{l24}\n{l25}\n{l26}\n"

        print ("Se esta a enviado mensaje de recibo al correo electronico")
        conexion.sendmail('angelstevengonzalezf@gmail.com', correo , msg = mensajexd )

        print()
        print("Se a enviado correctamente y gracias por preferirnos")
        print()

        conexion.quit()


        print()
        print()
        print()
        Salir = input("Desea continuar con el siguiente visitante S/N  ")
            
        if(Salir == "S") or (Salir == "s"):
            
            os.system("cls")
            return main()
            
        elif(Salir == "N") or (Salir == "n"):
            os.system("pause")

        else:
            print("esa opcion no exite")
            os.system("cls")
            return main()
      
    else:

        print("Esa opcion no existe")
        
        print()
        
        Salir = input("Desea continuar con el siguiente visitante S/N ")
            
        if(Salir == "S") or (Salir == "s"):

            os.system("cls")
            return main()
            
        elif(Salir == "N") or (Salir == "n"):
             os.system("pause")
             
        else:
            print("esa opcion no exite")
            os.system("cls")
            return main()

main()  