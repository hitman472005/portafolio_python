from datetime import datetime
from operator import ge
import smtplib
import os




identificadores_de_ventas = []

def general():
    
    
    Almacenado_de_opciones = 0
    pelicula_escojida = ""
    categoria = ""

    print("**********************************")
    print("*Sistema de Alquiler de Peliculas*")
    print("**********************************")
    print("*        Angel STeven #16        *")
    print("**********************************")
    print()
    print("*************************************************")
    print("*              listado de Opciones              *")
    print("*************************************************")
    print("*    1. Alquilar Pelicula                       *")
    print("*    2. Ver listado de Ids de venta             *")
    print("*    3. Devolucion de pelicula                  *")
    print("*    4. salir del programa                      *")
    print("*************************************************")

    opcion_que_hacer = input("ingrese el numero de comando de lo que desea hacer: ")

    os.system("cls")

    def alquiler(Almacenado_de_opciones , pelicula_escojida, categoria):

        
        print("*********************************")
        print("*      Escoja la categoria      *")
        print("*      y Pelicula de Interes    *")
        print("*********************************")
        print("*     listado de categoria      *")
        print("*********************************")
        print("*  1. Terror..........400$      *")
        print("*  2. Accion..........250$      *")
        print("*  3. Infantil........100$      *")
        print("*********************************")

        print()

        Opcion_categotia = input("Ingrese el numero de la categoria a escojer: ")
        os.system("cls")
        print()

        if Opcion_categotia == "1":
            
            categoria = "Terror"
            
            Almacenado_de_opciones= Almacenado_de_opciones + 400
            
            print("*************************************")
            print("*   listado de peliculas de terror  *")
            print("*************************************")
            print("*           1. Scream               *")
            print("*           2. No respires          *")
            print("*           3. El conjuro           *")
            print("*************************************")
            
            print()
            
                
            pelicula_terror = input("Ingrese el numero de la pelicula a escojer: ")

            
            if pelicula_terror == "1":
                    
                pelicula_escojida = "Scream"
                
            elif pelicula_terror == "2":
                    
                pelicula_escojida = "No Respires"
                    
            elif pelicula_terror == "3":
                    
                pelicula_escojida = "El Conjuro"

        elif Opcion_categotia == "2":
            
            categoria = "Accion"
            
            Almacenado_de_opciones= Almacenado_de_opciones + 250
            
            print("*************************************")
            print("*   listado de peliculas de Accion  *")
            print("*************************************")
            print("*           1. Rambo                *")
            print("*           2. Alerta Roja          *")
            print("*           3. UNCHARTED            *")
            print("*************************************")
            
            print()
            
                
            pelicula_Accion = input("Ingrese el numero de la pelicula a escojer: ")

                
            if pelicula_Accion == "1":
                    
                pelicula_escojida = "Rambo"
                
            elif pelicula_Accion == "2":
                    
                pelicula_escojida = "Alerta roja"
                    
            elif pelicula_Accion == "3":
                    
                pelicula_escojida = "UNCHARTED"

        elif Opcion_categotia == "3":
            
            Almacenado_de_opciones= Almacenado_de_opciones + 100
            
            categoria = "Infantil"
            
            print("***************************************************")
            print("*       listado de peliculas de infantiles        *")
            print("***************************************************")
            print("*     1. Dora la Exploradora                      *")
            print("*     2. Diego GO a salvar                        *")
            print("*     3. Popeye el Marino LA PELICULA             *")
            print("***************************************************")
            
            print()
            
                
            pelicula_infantiles = input("Ingrese el numero de la pelicula a escojer: ")

                
            if pelicula_infantiles == "1":
                    
                pelicula_escojida = "Dora la Exploradora"
                
            elif pelicula_infantiles == "2":
                    
                pelicula_escojida = "Diego GO a salvar"
                    
            elif pelicula_infantiles == "3":
                    
                pelicula_escojida = "Popeye el Marino LA PELICULA "

        os.system("cls")  
        print()
        print()

        print("*****************************************************")
        print("*          Eleccion de Formato Pelicula             *")
        print("*                                                   *")
        print("*   1. Formato DVD...........................150$   *")
        print("*                                                   *")
        print("*   2. Formato Blueray (Ultra HD)............350$   *")
        print("*                                                   *")
        print("*****************************************************")

        print()
        print()

        formato_Pelis = input("Ingrese numero de comando de el formato que desea del disco: ")

        print()
        print()

        if formato_Pelis == "1":
            Almacenado_de_opciones = Almacenado_de_opciones + 150

            print("*buena eleccion*")

        elif formato_Pelis == "2":
            Almacenado_de_opciones = Almacenado_de_opciones + 350
            
            print("*Exelente eleccion*")

        print("***************************************************")
        print("*   Inicializacion de la generacion de factura    *")
        print("***************************************************")

        

        identificador_cliente = input ("ingrese ID del cliente: ")
        
        while (identificador_cliente in identificadores_de_ventas):
        
            os.system("cls")
            print ("ese ID ya existe, ingrese otro")
            print()
            identificador_cliente = input ("ingrese ID del cliente: ")
            print()
        
        lista_id_fecha = []
        lista_id_fecha.append(identificador_cliente)
        identificadores_de_ventas.append(identificador_cliente)                     
        Nombre_cliente = input("Ingrese el nombre del cliente: ")
        Apellido_cliente = input("ingrese el apellido del cliente: ")

        fecha_de_renta = datetime.strptime(input("ingrese la fecha de renta: "), "%d/%m/%Y")
        
        
        
        fechaxd = f"la fecha de renta es {fecha_de_renta.day}/{fecha_de_renta.month}/{fecha_de_renta.year}"
        lista_id_fecha.append(fechaxd)
        
        identificadores_de_ventas.append(lista_id_fecha) 

        itebis = Almacenado_de_opciones * 0.18
        
        total_itebis = Almacenado_de_opciones + itebis
        
        
        os.system("cls")
        print()
        print("***********************************************************************************")
        print("                    recibo del alquiler                      ")
        print("                                                             ")
        print(f"    Identificacion de venta: {identificador_cliente}        ")
        print("                                                             ")
        print(f"    Nombre del cliente: {Nombre_cliente} {Apellido_cliente} ")
        print("                                                             ")
        print(f"    PelicuLa Escojida: {pelicula_escojida}                  ")
        print("                                                             ")
        print(f"    Categoria de la pelicula: {categoria}                   ")
        print("                                                             ")
        print(f"    Fecha de Alquiler de la pelicula: {fecha_de_renta.day}/{fecha_de_renta.month}/{fecha_de_renta.year} ")
        print("                                                             ")
        print(f"    Total Sin ITEBIS: {Almacenado_de_opciones}              ")
        print("                                                             ")
        print(f"    Valor de ITEBIS: {itebis}                               ")
        print("                                                             ")
        print(f"    Total con ITEBIS: {total_itebis}                        ")
        print("                                                             ")
        print("**************************************************************************************")

        print()
        print()
        print()
        print("se a almacenado en la base de datos del block de notas DvD")
        
        block = open("dvd.txt","a")
        
        bl1 = ("***********************************************************************************")
        bl2 = (f"    Id recibo del alquiler # {identificador_cliente}        ")
        bl3 = ("                                                             ")
        bl4 = ("                                                             ")
        bl5 = (f"    Nombre del cliente: {Nombre_cliente} {Apellido_cliente} ")
        bl6 = ("                                                             ")
        bl7 = (f"    Pelicula Escojida: {pelicula_escojida}                  ")
        bl8 = ("                                                             ")
        bl9 =(f"    Categoria de la pelicula: {categoria}                   ")
        bl10 =("                                                             ")
        bl11 =(f"    Fecha de Alquiler de la pelicula: {fecha_de_renta.day}/{fecha_de_renta.month}/{fecha_de_renta.year} ")
        bl12 =("                                                             ")
        bl13 =(f"    Total Sin ITEBIS: {Almacenado_de_opciones}              ")
        bl14 =("                                                             ")
        bl15 =(f"    Valor de ITEBIS: {itebis}                               ")
        bl16 =("                                                             ")
        bl17 =(f"    Total con ITEBIS: {total_itebis}                        ")
        bl18 =("                                                             ")
        bl19 =("**************************************************************************************")
        
        nota_DVD = f"{bl1}\n{bl2}\n{bl3}\n{bl4}\n{bl5}\n{bl6}\n{bl7}\n{bl8}\n{bl9}\n{bl10}\n{bl11}\n{bl12}\n{bl13}\n{bl14}\n{bl15}\n{bl16}\n{bl17}\n{bl18}\n{bl19}\n\n\n\n"
        
        block.write(nota_DVD)
        
        block.close()

        desea_Correo = input("Desea que le llege el recibo al correo (S/N): ")

        print()
        print()

        if (desea_Correo == "s") or (desea_Correo == "S"):
            
            correo = input("ingrese su correo electronico: ")
            
            conexion = smtplib.SMTP('smtp.gmail.com', 587)
            conexion.ehlo()
            conexion.starttls()
            
            l1 = ("***********************************************************************************")
            l2 = ("                    recibo del alquiler                      ")
            l3 = ("                                                             ")
            l4 = (f"    Identificacion de venta: {identificador_cliente}        ")
            l5 = ("                                                             ")
            l6 = (f"    Nombre del cliente: {Nombre_cliente} {Apellido_cliente} ")
            l7 = ("                                                             ")
            l8 = (f"    Pelicula Escojida: {pelicula_escojida}                  ")
            l9 = ("                                                             ")
            l10 =(f"    Categoria de la pelicula: {categoria}                   ")
            l11 =("                                                             ")
            l12 =(f"    Fecha de Alquiler de la pelicula: {fecha_de_renta.day}/{fecha_de_renta.month}/{fecha_de_renta.year} ")
            l13 =("                                                             ")
            l14 =(f"    Total Sin ITEBIS: {Almacenado_de_opciones}              ")
            l15 =("                                                             ")
            l16 =(f"    Valor de ITEBIS: {itebis}                               ")
            l17 =("                                                             ")
            l18 =(f"    Total con ITEBIS: {total_itebis}                        ")
            l19 =("                                                             ")
            l20 =("**************************************************************************************")
            

            conexion.login('angelstevengonzalezf@gmail.com','tu contrasena')

            mensajexd = f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}\n{l8}\n{l9}\n{l10}\n{l11}\n{l12}\n{l13}\n{l14}\n{l15}\n{l16}\n{l17}\n{l18}\n{l19}\n{l20}\n"

            print ("Se esta a enviado mensaje de recibo al correo electronico")
            conexion.sendmail('angelstevengonzalezf@gmail.com', correo , msg = mensajexd )

            print()
            print("Se a enviado correctamente y gracias por preferirnos")
            print()

            conexion.quit()

            print("se ha terminado el proceso")
            print()
            
        elif  desea_Correo == (desea_Correo == "n") or (desea_Correo == "N"):
            
            print()
            print("se ha terminado el proceso")

        print("para volver a seleccionar las opciones")
        os.system("pause")
        os.system("cls")
        return general()
   
   
    
    
    def listado_id_ventas(identificadores_de_ventas):
        
        print("Aqui el listado de Ids de todas las ventas")
        print()
        print(identificadores_de_ventas)
        print()
        
        print("para volver a seleccionar las opciones")
        os.system("pause")
        os.system("cls")
        return general()
    
    def devolucion():
        
        verificador_de_lista = input("ingrese la id para verificar si es valido y si se realizo la compra: ")
        
        
         
        if(verificador_de_lista in identificadores_de_ventas):
            os.system("cls")
            print("ingrese la fecha que se guardo el id en la base de datos block de notas DVD")
        
            fecha_de_dia_de_renta = datetime.strptime(input("ingrese la fecha de renta: "), "%d/%m/%Y")
            fecha_de_dia_de_devuelta = datetime.strptime(input("ingrese la fecha de la devolucion: "), "%d/%m/%Y")
        
            dias = abs(fecha_de_dia_de_renta - fecha_de_dia_de_devuelta).days
        
            print("cantidad de dias de alquiler es de:" , (dias)) 
            
            if dias >= 15:
                dia_1 = 100
                
                retraso = dias -14
                
                resultado_devolucion = retraso * dia_1
                print()
                print (f"debe de pagar {resultado_devolucion} por retrazo")
                print()
                print("para volver a seleccionar las opciones")
                os.system("pause")
                os.system("cls")
                return general()
            else:
                print()
                print("gracias por preferirnos")
                print()
                print("para volver a seleccionar las opciones")
                os.system("pause")
                os.system("cls")
                return general()
        else:
            
            print("esa id no se encuentra")
            print()
            opcion_principal = input("desea volver a reintentar: S/N: ")
            
            if opcion_principal == "S" or opcion_principal == "s":
                os.system("cls")
                return devolucion()
            
            elif (opcion_principal == "n") or (opcion_principal == "N"):
            
                os.system("pause")
                os.system("cls")
                return general()
            
    
    if opcion_que_hacer == "1":
        
        alquiler(Almacenado_de_opciones ,pelicula_escojida, categoria )
        
    elif opcion_que_hacer == "2":
        listado_id_ventas(identificadores_de_ventas)
        
    elif opcion_que_hacer == "3":
        devolucion()
    
    elif opcion_que_hacer == "4":
        os.system("pause")

general()
