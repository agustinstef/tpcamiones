import os
camiones = 0
contsoja = 0
contmaiz = 0
cont_tara_s = 0
cont_tara_m = 0
maximo_s = 0
menor_m = 1000000000000000000000
contcamiones = 0
camion_maximo_s = 0
camion_menor_m = 0
pesonetosoja = 0
pesonetomaiz = 0
promedionetosoja = 0
promedionetomaiz = 0

# os.system("CLS")
def menu_principal():
    opcion = "1"
    while opcion != "0": 
        print ("-" * 30)
        print ("Menu principal : ")
        print ("-" * 30)
        print("\n")
        print ("1- Administracion")
        print ("-" * 30)
        print ("2- Entrega de cupos")
        print ("-" * 30)
        print ("3- Recepcion")
        print ("-" * 30)
        print ("4- Registrar calidad")
        print ("-" * 30)
        print ("5- Registrar peso bruto")
        print ("-" * 30)
        print ("6- Registrar descarga")
        print ("-" * 30)
        print ("7- Registrar tara")
        print ("-" * 30)
        print ("8- Reporte")
        print ("-" * 30)
        print ("0- Fin del programa")
        print ("-" * 30)
        print ("-" * 30)
        
        opcion = input("selecciona una opcion del menu : ")
        while opcion !="1" and opcion!="2" and opcion!="3" and opcion!="4"  and opcion!="5"  and opcion!="6"  and opcion!="7"  and opcion!="8"  and opcion!="0":
             opcion = input("la opcion ingresada es invalida, por favor ingrese una opcion del menu : ")
             
        if opcion == "1":
            os.system("CLS")
            print("\n")
            menu_administracion()
            print("\n")

        elif opcion == "3":
            os.system("CLS")
            print("\n")
            menu_recepcion()
            print("\n")

        elif opcion == "0":
            print("\n")
            print ("Fin del programa")
            print("\n")

        elif opcion == "8":
            os.system("CLS")
            print ("\n")
            menu_reporte()
            print("\n")
     

        elif (opcion == "2") or (opcion == "4") or (opcion == "5") or (opcion == "6") or (opcion == "7"):
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

    
        else:
            0


def menu_administracion():
    # entra = True
    opcion_administracion = "1"
    while opcion_administracion != "v" or opcion_administracion != "V":
        print ("-" * 30)
        print ("Menu Administracion : ")
        print ("-" * 30)
        print("\n")
        print ("A. Titulares")
        print ("-" * 30)
        print ("B. Productos")
        print ("-" * 30)
        print ("C. Rubros")
        print ("-" * 30)
        print ("D. Rubros x producto")
        print ("-" * 30)
        print ("E. Silos")
        print ("-" * 30)
        print ("F. Sucursales")
        print ("-" * 30)
        print ("G. Producto por titular")
        print ("-" * 30)
        print ("V. Volver al menu principal")
        print ("-" * 30)


        opcion_administracion = input("Ingrese una opcion del menu : ")
        if opcion_administracion == "a" or opcion_administracion == "A":
            os.system("CLS")
            print("\n")
            menu_titulares()
            print("\n")

        elif opcion_administracion == "B" or opcion_administracion == "b" or opcion_administracion == "C" or opcion_administracion == "c" or opcion_administracion == "D" or opcion_administracion == "d" or opcion_administracion == "E" or opcion_administracion == "e" or opcion_administracion == "F" or opcion_administracion == "f" or opcion_administracion == "G" or opcion_administracion == "g":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")
            

        # elif opcion_administracion == "V" or opcion_administracion == "v":
        #     print("\n")
        #     print ("Volver al menu principal")
        #     print("\n")
        #     os.system("CLS")
            # entra = False
        else:
            # os.system("CLS")
            # print("\n")
            # print ("opcion no valida, por favor elja otra opcion")
            # print("\n")
            0
   

def menu_titulares():
    #  entra = True
    opcion_titulares = "1"
    while opcion_titulares != "v" or opcion_titulares != "V":
        print("\n")
        print ("-" * 30)
        print ("Menu Titulares : ")
        print ("-" * 30)
        print("\n")
        print ("A. Alta")
        print ("-" * 30)
        print ("B. Baja")
        print ("-" * 30)
        print ("C. Consulta")
        print ("-" * 30)
        print ("M. Modificacion")
        print ("-" * 30)
        print ("V. Volver al menu anterior")
        print ("-" * 30)

        opcion_titulares = input ("ingrese una opcion del menu : ")
        if opcion_titulares == "A" or opcion_titulares == "a":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "B" or opcion_titulares == "b" :
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "C" or opcion_titulares == "c":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "M" or opcion_titulares == "m":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        # elif opcion_titulares == "V" or opcion_titulares == "v":
        #     print("\n")
        #     print ("Volver al menu anterior")
        #     print("\n")
        #     os.system("CLS")
        #     entra = False

        else:
            # os.system("CLS")
            # print("\n")
            # print ("opcion no valida, por favor elija otra opcion")
            # print("\n")
            0


def menu_recepcion():
    global contsoja
    global contmaiz
    global cont_tara_s
    global cont_tara_m 
    global maximo_s 
    global menor_m
    global camion_maximo_s
    global camion_menor_m
    global pesonetosoja
    global pesonetomaiz
    global promedionetosoja
    global promedionetomaiz
    global contcamiones

    camiones = int(input("ingrese cuantos camiones arribaran : "))
    print("\n")

    contcamiones = camiones
    for i in range (1,camiones + 1):

        print("\n")
        producto = input("ingrese que transporta su camion (s para soja/ m para maiz) : ")
        print("\n")

        if producto == "s" or producto == "S":

            contsoja = contsoja + 1
            print("\n")
            tara = int(input("ingrese su tara : "))
            print("\n")
            cont_tara_s= cont_tara_s + tara

            if tara>maximo_s:
                maximo_s=tara
                print("\n")
                patente = input("ingrese su patente : ")
                print("\n")
                camion_maximo_s= patente
                print("\n")
                peso_bruto = int(input("ingrese su peso bruto : "))
                print("\n")

                while peso_bruto <= tara:
                    print("\n")
                    print("el peso bruto debe ser mayor que la tara")
                    print("\n")
                    peso_bruto = int(input ("ingrese nuevamente el peso bruto : "))
                    print("\n")

                peso_neto = peso_bruto - tara
                pesonetosoja = pesonetosoja + peso_neto
                promedionetosoja = pesonetosoja / contsoja

                if peso_neto>0:
                    print("\n")
                    print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
                    print("\n")
            
            else:
                print("\n")
                patente = input("ingrese su patente : ")
                print("\n")
                camion_maximo_s = patente
                peso_bruto = int(input("ingrese su peso bruto : "))
                print("\n")

                while peso_bruto <= tara:
                    print("\n")
                    print("el peso bruto debe ser mayor que la tara")
                    print("\n")
                    peso_bruto = int(input ("ingrese nuevamente el peso bruto : "))
                    print("\n")

                peso_neto = peso_bruto - tara
                pesonetosoja = pesonetosoja + peso_neto
                promedionetosoja = pesonetosoja / contsoja
                print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
                print("\n")



        else:
            if producto == "m" or producto == "M":
                contmaiz = contmaiz + 1
                print("\n")
                tara = int(input("ingrese su tara : "))
                print("\n")
                cont_tara_m= cont_tara_m + tara
                if tara<menor_m:
                        menor_m=tara
                        print("\n")
                        patente = input("ingrese su patente : ")
                        print("\n")
                        camion_menor_m = patente
                        peso_bruto = int(input("ingrese su peso bruto : "))
                        print("\n")

                        while peso_bruto <= tara:
                            print("\n")
                            print("el peso bruto debe ser mayor que la tara")
                            print("\n")
                            peso_bruto = int(input ("ingrese nuevamente el peso bruto : "))
                            print("\n")

                        peso_neto= peso_bruto - tara
                        pesonetomaiz = pesonetomaiz + peso_neto
                        promedionetomaiz = pesonetomaiz / contmaiz

                        if peso_neto>0: 
                            print("\n")
                            print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
                            print("\n")
                else: 
                    print("\n")
                    patente = input("ingrese su patente : ")
                    print("\n")
                    camion_menor_m = patente
                    peso_bruto = int(input("ingrese su peso bruto : "))
                    print("\n")

                    while peso_bruto <= tara:
                            print("\n")
                            print("el peso bruto debe ser mayor que la tara")
                            print("\n")
                            peso_bruto = int(input ("ingrese nuevamente el peso bruto : "))
                            print("\n")

                    peso_neto = peso_bruto - tara
                    pesonetomaiz = pesonetomaiz + peso_neto
                    promedionetomaiz = pesonetomaiz / contmaiz
                    print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
        
        

def menu_reporte():
        print("\n")
        print ("-" * 30)
        print ("Reportes")
        print ("-" * 30)
        print("\n")
        print (f"- Cantidad total de camiones que llegaron: {contcamiones} ")
        print ("-" * 30)
        print (f"- Cantidad total de caminoes de soja: {contsoja} ")
        print ("-" * 30)
        print (f"- Cantidad total de camiones de maiz {contmaiz}")
        print ("-" * 30)
        print (f"- Peso neto total de soja: {pesonetosoja} ")
        print ("-" * 30)
        print (f"- Peso neto total de maiz: {pesonetomaiz} ")
        print ("-" * 30)
        print (f"- Promedio del peso neto de soja por camion: {promedionetosoja} ")
        print ("-" * 30)
        print (f"- Promedio del peso neto de maiz por camion: {promedionetomaiz} ")
        print ("-" * 30)
        print (f"- Patente del camion de soja que mayor cantidad de soja descargo: {camion_maximo_s}  ")
        print ("-" * 30)
        print (f"- Patente del camion de maiz que menor cantidad de maiz descargo: {camion_menor_m} ")
        print ("-" * 30)
        print("\n")
        print ("-" * 30)
        input("Presione Enter para volver al menu anterior : ")
        print ("-" * 30)
        os.system("CLS")
        # menu_principal()
    



menu_principal()