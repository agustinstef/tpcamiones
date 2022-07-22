import os
# neto_productos: array [0..4] of int
# cont_cupos_camiones: array [0..1] of int
# cont_productos : array [0..4] of int
# maximo : array [0..4] of int
# menor : array [0..4] of int
# patente_max_min : array [0..4] [0..4] of string
# neto_max_min : array [0..4] [0..4] of int
# patente_estado : array [0..7] [0..7] [0..7] of string
# PesosPorPatente: array [0..7] [0..7] of int
# Netos: array [0..7] of int
# productos: array [0..2] of string

neto_productos = [0,0,0,0,0]
cont_cupos_camiones = [0,0]
cont_productos = [0,0,0,0,0]
maximo = [0,0,0,0,0]
menor = [45,45,45,45,45]
patente_max_min = [["","","","",""],["","","","",""]]
neto_max_min = [[0,0,0,0,0],[0,0,0,0,0]]
patente_estado = [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]
PesosPorPatente = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Netos = [0,0,0,0,0,0,0,0] 
productos = ["","",""]
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

        elif opcion == "2":
            os.system("CLS")
            print("\n")
            Entrega_cupo()
            print("\n")
        elif opcion == "3":
            os.system("CLS")
            print("\n")
            menu_recepcion()
            print("\n")

        elif opcion == "5":
            os.system("CLS")
            print("\n")
            RegistrarPesoBruto()
            print("\n")

        elif opcion == "7":
            os.system('CLS')
            print("\n")
            RegistrarPesoTara()
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
     

        elif (opcion == "2") or (opcion == "4") or (opcion == "6"):
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

    
        else:
            0

def menu_administracion():
    opcion_administracion ="1"
    while opcion_administracion != "v" and opcion_administracion != "V":
        os.system('CLS')
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

        elif opcion_administracion == "B" or opcion_administracion == "b":
            os.system("CLS")
            Productos()

        elif opcion_administracion == "C" or opcion_administracion == "c" or opcion_administracion == "D" or opcion_administracion == "d" or opcion_administracion == "E" or opcion_administracion == "e" or opcion_administracion == "F" or opcion_administracion == "f" or opcion_administracion == "G" or opcion_administracion == "g":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")
            
        else:
            os.system("CLS")
            print("\n")
            print ("opcion no valida, por favor elja otra opcion")
            print("\n")

    print("\n")
    print ("Volver al menu principal")
    print("\n")
    os.system("CLS")

def menu_titulares():
     opcion_titulares = "1"
     while opcion_titulares != "v" and opcion_titulares != "V":
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

        else:
            os.system("CLS")

def menu_recepcion():
    global cont_productos
    global cont_cupos_camiones
    entrada = 1
    while entrada != 0:
        p = 0
        comprobar_p = 0
        patente = input("Ingrese la patente de su camion : ")
        print("\n")
        while len(patente) < 6 or len(patente) > 7:
            print ("Error, cantidad de caracteres invalida.")
            print("\n")
            patente = input("Vuelva a ingresar por favor : ")
        while patente_estado[0][p] != patente and p <7:
            p = p + 1
        if patente_estado[0][p] == patente:
            if patente_estado[1][p] == "p":
                print("El estado de su camion se ha modificado y ahora esta en proceso.")
                patente_estado[1][p] = "e"
                print ("-" * 90)
                print("Nuestra empresa solamente trabaja con TRIGO(t), SOJA(s), MAIZ(m), GIRASOL(g) y/o CEBADA(c): ")
                print ("-" * 90)
                print("\n")
                producto = input("Ingrese el producto que transporta su camion : ").upper()
                while producto != "T" and producto != "M" and producto != "S" and producto != "G" and producto != "C":
                    os.system("CLS")
                    print ("La opcion ingresada no es valida")
                    print("\n")
                    print ("-" * 90)
                    print("Nuestra empresa solamente trabaja con TRIGO(t), SOJA(s), MAIZ(m), GIRASOL(g) y/o CEBADA(c): ")
                    print ("-" * 90)
                    print("\n")
                    producto = input("Elija una opcion valida : ").upper()
                while productos[comprobar_p] != producto and comprobar_p < 2:
                    comprobar_p = comprobar_p + 1
                if productos[comprobar_p] == producto:
                    if producto == "S":
                        cont_productos[0] = cont_productos[0] + 1
                        patente_estado[2][p] = "S"

                    elif producto == "M":
                        cont_productos[1] = cont_productos[1] + 1
                        patente_estado[2][p] = "M"

                    elif producto == "G":
                        cont_productos[2] = cont_productos[2] + 1    
                        patente_estado[2][p] = "G"  

                    elif producto == "C":
                        cont_productos[3] = cont_productos[3] + 1
                        patente_estado[2][p] = "C"

                    elif producto == "T":
                        cont_productos[4] = cont_productos[4] + 1
                        patente_estado[2][p] = "T"
                    cont_cupos_camiones[1] = cont_cupos_camiones[1] + 1
                else: 
                    os.system('CLS')
                    print("Hoy no trabajamos con este producto")
                    patente_estado[1][p] = "p"
                opcion = input("Desea ingresar otro camion ? Si (s) No (n)")
                entrada = validar_entrada(opcion)
            else:
                patente_estado[1][p] == "c" or patente_estado[1][p] == "e"
                print("Su camion ya esta en proceso o se ha cumplido su carga, por lo tanto no puede volver a ingresarse.")
                print("\n")
                opcion = input("Desea ingresar otro camion ? Si (s) No (n)")
                entrada = validar_entrada(opcion)
        else:
            print("Su camion no tiene cupo o no esta registrado.")
            print("\n")
            opcion = input("Desea ingresar otro camion ? Si (s) No (n)")
            entrada = validar_entrada(opcion)
        
def Productos ():
    opcion_productos = "1"
    while opcion_productos != "v" and opcion_productos != "V":
        print("\n")
        print ("-" * 30)
        print ("Menu Productos : ")
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

        opcion_productos = input("Elija una opcion : ")
        if opcion_productos == "A" or opcion_productos == "a":
            os.system("CLS")
            Alta()
        elif opcion_productos == "B" or opcion_productos == "b":
            os.system("CLS")
            Baja()
        elif opcion_productos == "c" or opcion_productos == "C":
            Consulta()
        elif opcion_productos == "M" or opcion_productos == "m":
            Modificacion()
        else:
            os.system("CLS")
            print("Error, elija una opcion valida.")

def Alta():
    global productos
    print ("-" * 90)
    print("Nuestra empresa solamente trabaja con TRIGO(t), SOJA(s), MAIZ(m), GIRASOL(g) y/o CEBADA(c): ")
    print ("-" * 90)
    print("\n")
    nom_producto = input("Ingrese su producto : ").upper()
    while nom_producto != "T" and nom_producto != "M" and nom_producto != "S" and nom_producto != "G" and nom_producto != "C":
        os.system("CLS")
        print ("La opcion ingresada no es valida")
        print("\n")
        print ("-" * 90)
        print("Nuestra empresa solamente trabaja con TRIGO(t), SOJA(s), MAIZ(m), GIRASOL(g) y/o CEBADA(c): ")
        print ("-" * 90)
        print("\n")
        nom_producto = input("Elija una opcion valida : ").upper()
        os.system("CLS")
    if nom_producto == "T" or nom_producto == "M" or nom_producto == "S" or nom_producto == "G" or nom_producto == "C":
        p = 0
        i = 0
        while productos[p] != "" and p < 2:
            p = p + 1
        if productos[p] == "":
            while productos[i] != nom_producto and i < 2:
                i = i + 1
            if productos [i] != nom_producto:
                productos[p] = nom_producto
                print ("CARGA EXITOSA!")
            else:
                print("El producto ya se encuentra cargado.")
        else:
            print("Ya se cumplio la cantidad maxima de producto. Si quiere modificar alguno vaya a la seccion modificacion.")           

def Baja():
    print("Los productos seleccionados son : ")
    for i in range (3):
        suma = i + 1
        print(productos[i],"--",suma)
        print("\n")
    print("¿Desea eliminar alguno de sus productos?")
    entrada = 1
    while entrada == 1:
        decision = input("Si su respuesta es SI presione S, si su respuesta es NO presione N: ")
        if decision =="s" or decision =="S":
            os.system("CLS")
            for i in range (3):
                suma = i + 1
                print(productos[i],"--",suma)
                print("\n")
            print("presione el numero que acompaña al producto que desea eliminar")
            print("\n")
            opcion_baja = input("Elija su opcion :")
            while opcion_baja != "1" and opcion_baja != "2" and opcion_baja != "3":
                opcion_baja = input ("Error, Vuelva a ingresar una opcion valida :")

            if opcion_baja == "1":
                     productos[0] = ""
            elif opcion_baja == "2":
                    productos[1] = ""
            elif opcion_baja == "3":
                     productos[2] = ""
            entrada = 0
        
        elif decision == "n" or decision == "N":
            entrada = 0

        else:
            os.system("CLS")
            print("error, vuelva a ingresar")
            print("\n")

def Consulta():
    os.system("CLS")
    for i in range (3):
        print ("-" * 15)
        print ("Producto", i + 1, "--", productos[i])
        print ("-" * 15)
        print("\n")

def Modificacion():
    os.system("CLS")
    for i in range (3):
        print ("-" * 15)
        print ("Producto", i + 1, "--", productos[i])
        print ("-" * 15)
        print("\n")
    cambio = input("¿Quiere realizar algun cambio? Ingrese una S si su respuesta es si o ingrese una N si su respuesta es no : ")
    while cambio != "s" and cambio !="S" and cambio != "N" and cambio != "n":
        cambio = input("Su respuesta no es valida, vuelva a ingresar S o N : ")
    if cambio == "S" or cambio == "s":
        os.system("CLS")
        for i in range (3):
            suma = i + 1
            print(productos[i],"--",suma)
            print("\n")
        print("presione el numero que acompaña al producto que desea modificar")
        print("\n")
        opcion_mod = input("Elija su opcion :")
        while opcion_mod != "1" and opcion_mod != "2" and opcion_mod != "3":
            opcion_mod = input ("Error, Vuelva a ingresar una opcion valida :")
        if opcion_mod == "1":
            verdadero = 0
        elif opcion_mod == "2":
            verdadero = 1
        elif opcion_mod == "3":
            verdadero = 2

        if productos[verdadero] != "":
            if opcion_mod == "1":
                print ("-" * 90)
                print("Nuestra empresa solamente trabaja con TRIGO(t), SOJA(s), MAIZ(m), GIRASOL(g) y/o CEBADA(c): ")
                print ("-" * 90)
                print("\n")
                aux = productos[0]
                productos[0] = input("ingrese el nuevo producto : ").upper()
                if productos [0] == productos [1] or productos[0] == productos[2]:
                    print("El producto a ingresar se encuentra ya cargado. Por tanto no puede ingresar otra vez el mismo.")
                    productos[0] = aux
            elif opcion_mod == "2":
                aux = productos[1]
                productos[1] = input("ingrese el nuevo producto : ").upper()
                if productos [1] == productos [0] or productos[1] == productos[2]:
                    print("El producto a ingresar se encuentra ya cargado. Por tanto no puede ingresar otra vez el mismo.")
                    productos[1] = aux
            elif opcion_mod == "3":
                aux = productos[2]
                productos[2] = input("ingrese el nuevo producto : ").upper()
                if productos [2] == productos [0] or productos[2] == productos[1]:
                    print("El producto a ingresar se encuentra ya cargado. Por tanto no puede ingresar otra vez el mismo.")
                    productos[2] = aux
        else:
            os.system('CLS')
            print("Esta opcion se encuentra vacia, por lo tanto no puede modificarse.")
    
def Entrega_cupo():
    global patente_estado
    global cont_cupos_camiones
    p = 0
    c = 0
    entrada = 1
    while entrada != 0:
        while patente_estado[0][p] != "" and p <7:
            p = p + 1
        if patente_estado[0][p] == "":
                aux = input("ingrese una nueva patente: ")
                caracteres = len(aux)
                while caracteres<6 or caracteres>7:
                    os.system("CLS")
                    aux = input("la cantidad de caracteres de la patente son invalidos, por favor vuelva a ingresar : ")
                    caracteres = len(aux)
                os.system("CLS")
                while patente_estado[0][c] != aux and c < 7:
                    c = c + 1
                if patente_estado[0][c] == aux:
                    print("Su patente ya tiene cupo. No se puede tener mas de un cupo por patente.")
                    entrada = 0
                else:
                    patente_estado[1][p] = "p"
                    patente_estado[0][p] = aux
                    cont_cupos_camiones[0] = cont_cupos_camiones[0] + 1
                    entrada = 0
                    print("CARGA EXITOSA!")
        else: 
            print("Se excedio la capacidad maxima de cupos, vuelva a intentarlo mas tarde")
            entrada = 0

def RegistrarPesoBruto():
    global PesosPorPatente
    entrada = 1
    p = 0
    while entrada != 0:
        patente = input("Ingrese la patente de su camion : ")
        print("\n")
        while len(patente) < 6 or len(patente) > 7:
            print ("Error, cantidad de caracteres invalida.")
            print("\n")
            patente = input("Vuelva a ingresar por favor : ")
        while patente_estado[0][p] != patente and p <7:
            p = p + 1
        if patente_estado[0][p] == patente:
            if PesosPorPatente[0][p] == 0:
                if patente_estado[1][p] == "e":
                    print("El estado de su camion es correcto.")
                    print("\n")
                    try:
                        PesosPorPatente[0][p] = int(input("Ingrese el peso bruto de su camion en toneladas : "))
                    except:
                        print("Caracter ingresado invalido, por favor cargue los datos correctamente.")
                        print("\n")
                        RegistrarPesoBruto()
                    while PesosPorPatente[0][p] > 45 or PesosPorPatente[0][p] < 9:
                        print("Su peso esta fuera del rango permitido o se ingreso un caracter invalido.")
                        print("\n")
                        try: 
                            PesosPorPatente[0][p] = int(input ("Ingrese el peso bruto de su camion en toneladas : "))
                        except:
                                print("Caracter ingresado invalido, por favor cargue los datos correctamente.")
                                print("\n")
                                RegistrarPesoBruto()
                    entrada = 0
                    os.system('CLS')
                    print("CARGA EXITOSA!")
                else:
                    print("Su patente no esta en proceso.")
                    entrada = 0
            else:
                os.system('CLS')
                print("Su patente ya tiene un peso bruto registrado.")
                entrada = 0
        else:
            print("Su patente no tiene cupo.")
            entrada = 0
    
def RegistrarPesoTara():
    global PesosPorPatente
    global patente_max_min
    global neto_max_min
    global maximo
    global menor
    entrada = 1
    while entrada != 0:
        p = 0
        patente = input("Ingrese la patente de su camion : ")
        print("\n")
        while len(patente) < 6 or len(patente) > 7:
            print ("Error, cantidad de caracteres invalida.")
            print("\n")
            patente = input("Vuelva a ingresar por favor : ")
        while patente_estado[0][p] != patente and p <7:
            p = p + 1
        if patente_estado[0][p] == patente:
            if PesosPorPatente[0][p] != 0:
                if PesosPorPatente[1][p] == 0:
                    if patente_estado[1][p] == "e":
                        print("El estado de su camion es correcto.")
                        print("\n")
                        try:
                            PesosPorPatente[1][p] = int(input ("Ingrese el peso tara de su camion en toneladas : "))
                        except:
                            print("Caracter ingresado invalido, por favor cargue los datos correctamente.")
                            print("\n")
                            RegistrarPesoBruto()
                        while PesosPorPatente[1][p] > PesosPorPatente[0][p] or PesosPorPatente[1][p] < 0:
                            print("Error, su peso tara debe ser menor que su peso bruto y/o mayor a 0.")
                            print("\n")
                            try:
                                PesosPorPatente[1][p] = int(input("Ingrese el peso tara de su camion en toneladas : "))
                            except:
                                print("Caracter ingresado invalido, por favor cargue los datos correctamente.")
                                print("\n")
                                RegistrarPesoBruto()
                        while PesosPorPatente[1][p] > 16 or PesosPorPatente[1][p] < 0:
                            print("Su peso esta fuera del rango permitido (0 a 15).")
                            print("\n")
                            try:
                                PesosPorPatente[1][p] = int(input ("Ingrese el peso tara de su camion en toneladas : "))
                            except:
                                print("Caracter ingresado invalido, por favor cargue los datos correctamente.")
                                print("\n")
                                RegistrarPesoBruto()
                        Netos[p] = PesosPorPatente[0][p] - PesosPorPatente[1][p]
                        if patente_estado[2][p] == "S":
                            netosoja_m = PesosPorPatente[0][p] - PesosPorPatente[1][p]
                            neto_productos[0] = neto_productos[0] + netosoja_m
                            if netosoja_m > maximo[0]:
                                maximo[0] = netosoja_m
                                neto_max_min[0][1] = netosoja_m
                                patente_max_min[0][1] = patente_estado[0][p]

                            if netosoja_m < menor[0]:
                                menor[0] = netosoja_m
                                neto_max_min[1][1] = netosoja_m
                                patente_max_min[1][1] = patente_estado[0][p]

                        elif patente_estado[2][p] == "M":
                            netomaiz_m = PesosPorPatente[0][p] - PesosPorPatente[1][p]
                            neto_productos[1] = neto_productos[1] + netomaiz_m
                            if netomaiz_m > maximo[1]:
                                maximo[1] = netomaiz_m
                                neto_max_min[0][4] = netomaiz_m
                                patente_max_min[0][4] = patente_estado[0][p]

                            if netomaiz_m < menor[1]:
                                menor[1] = netomaiz_m
                                neto_max_min[1][4] = netomaiz_m
                                patente_max_min[1][4] = patente_estado[0][p]

                        elif patente_estado[2][p] == "G":
                            netogirasol_m = PesosPorPatente[0][p] - PesosPorPatente[1][p]
                            neto_productos[2] = neto_productos[2] + netogirasol_m
                            if netogirasol_m > maximo[2]:
                                maximo[2] = netogirasol_m
                                neto_max_min[0][3] = netogirasol_m
                                patente_max_min[0][3] = patente_estado[0][p]

                            if netogirasol_m < menor[2]:
                                menor[2] = netogirasol_m
                                neto_max_min[1][3] = netogirasol_m
                                patente_max_min[1][3] = patente_estado[0][p]
                                
                        elif patente_estado[2][p] == "C":
                            netocebada_m = PesosPorPatente[0][p] - PesosPorPatente[1][p]
                            neto_productos[3] = neto_productos[3] + netocebada_m
                            if netocebada_m > maximo[3]:
                                maximo[3] = netocebada_m
                                neto_max_min[0][2] = netocebada_m
                                patente_max_min[0][2] = patente_estado[0][p]

                            if netocebada_m < menor[3]:
                                menor[3] = netocebada_m
                                neto_max_min[1][2] = netocebada_m
                                patente_max_min[1][2] = patente_estado[0][p]

                        elif patente_estado[2][p] == "T":
                            netotrigo_m = PesosPorPatente[0][p] - PesosPorPatente[1][p]
                            neto_productos[4] = neto_productos[4] + netotrigo_m
                            if netotrigo_m > maximo[4]:
                                maximo[4] = netotrigo_m
                                neto_max_min[0][0] = netotrigo_m
                                patente_max_min[0][0] = patente_estado[0][p]

                            if netotrigo_m < menor[4]:
                                menor[4] = netotrigo_m
                                neto_max_min[1][0] = netotrigo_m
                                patente_max_min[1][0] = patente_estado[0][p]
                        entrada = 0
                        os.system('CLS')
                        print("CARGA EXITOSA!")
                        patente_estado[1][p] = "c"
                    else:
                        print("Su patente no esta en proceso.")
                        entrada = 0
                else:
                    os.system('CLS')
                    print("Su camion ya tiene registrado el peso tara.")
                    entrada = 0
            else:
                os.system('CLS')
                print("Su camion aun no ha registrado el peso bruto, por favor registre el peso bruto primero")
                entrada = 0
        else:
            print("Su patente no tiene cupo.")
            entrada = 0

def menu_reporte():
    global cont_productos
    global Netos
    print("\n")
    print ("-" * 30)
    print ("Reportes")
    print ("-" * 30)
    print (f"- Cantidad de cupos otorgados : {cont_cupos_camiones[0]}")
    print (("-" * 30))
    print (f"- Cantidad total de camiones que llegaron: {cont_cupos_camiones[1]}")
    print ("-" * 30)
    print (f"- La cantidad de camiones es la siguiente : Soja: {cont_productos[0]}, Maiz: {cont_productos[1]}, Girasol: {cont_productos[2]}, Cebada: {cont_productos[3]}, Trigo: {cont_productos[4]}")
    print ("-" * 30)
    print (f"- El peso neto total de cada producto es el siguiente: Soja: {neto_productos[0]}, Maiz: {neto_productos[1]}, Girasol: {neto_productos[2]}, Cebada: {neto_productos[3]}, Trigo: {neto_productos[4]}")
    print ("-" * 30)
    print (f"- El peso neto promedio de cada producto es el siguiente :") 
    if cont_productos[0] == 0:
        print ("-" * 30)
        print(f"Soja: {cont_productos[0]}")
    else:
        print ("-" * 30)
        print(f"Soja: {int(neto_productos[0]/cont_productos[0])}")
    if cont_productos[1] == 0:
        print ("-" * 30)
        print(f"Maiz: {cont_productos[1]}")
    else:
        print ("-" * 30)
        print(f"Maiz: {int(neto_productos[1]/cont_productos[1])}")
    if cont_productos[2] == 0:
        print ("-" * 30)
        print(f"Girasol: {cont_productos[2]}")
    else:
        print ("-" * 30)
        print(f"Girasol: {int(neto_productos[2]/cont_productos[2])}")
    if cont_productos[3] == 0:
        print ("-" * 30)
        print(f"Cebada: {cont_productos[3]}")
    else:
        print ("-" * 30)
        print(f"Cebada: {int(neto_productos[3]/cont_productos[3])}")
    if cont_productos[4] == 0:
        print ("-" * 30)
        print(f"Trigo: {cont_productos[4]}")
    else:
        print ("-" * 30)
        print (f"Trigo: {int(neto_productos[4]/cont_productos[4])}")
    print ("-" * 30)
    print (f"- Patente del camion de cada producto que mayor cantidad de dicho producto descargo: Trigo: {patente_max_min[0][0]}, Soja: {patente_max_min[0][1]}, Cebada: {patente_max_min[0][2]}, Girasol: {patente_max_min[0][3]}, Maiz: {patente_max_min[0][4]}")
    print ("-" * 30)
    print (f"- Patente del camion de cada producto que menor cantidad de dicho producto descargo: Trigo: {patente_max_min[1][0]}, Soja: {patente_max_min[1][1]}, Cebada: {patente_max_min[1][2]}, Girasol: {patente_max_min[1][3]}, Maiz: {patente_max_min[1][4]}")
    print ("-" * 30)

    for i in range(7):
            for k in range(i+1, 8):
                if Netos[i] < Netos[k]:
                    aux = Netos[i]
                    Netos[i] = Netos[k]
                    Netos[k] = aux
                    for j in range(3):
                        aux = patente_estado[j][i]
                        patente_estado[j][i] = patente_estado[j][k]
                        patente_estado[j][k] = aux

    for i in range (8):
        print(patente_estado[0][i], "--", patente_estado[2][i], "--", Netos[i])
    
    print ("-" * 30)
    print("\n")
    print ("-" * 30)
    input("Presione Enter para volver al menu anterior : ")
    print ("-" * 30)
    os.system("CLS")

def validar_entrada(opcion):
    while opcion != "s" and opcion != "S" and opcion != "N" and opcion != "n":
        print ("Error, opcion invalida, ingrese S o N.")
        print("\n")
        opcion = input("Ingrese una opcion valida : ")
    if opcion == "n" or opcion == "N":
        return 0
    else:
        return 1 

menu_principal()

                