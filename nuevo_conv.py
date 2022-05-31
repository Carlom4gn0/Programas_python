''' Nuevo programa de convercion de monedas
    utilizando condicionales y ciclos repetitivos ... '''
import os #libreria para poder utilizar os.system
import time #libreria para pausar luego de que me convierta el resultado antes de volver al menu

continuar = True #variable que me permite realizar el ciclo del programa
while (continuar == True):
    print("Bienvenido al conversor de monedas:")
    print("Menu")
    print("1 - Convertir pesos ARG a dolares")
    print("2 - Convertir pesos MEX a dolares")
    print("3 - convertir pesos COL a dolares")
    print("4 - SALIR")
    opcion = int(input("opcion: "))
    if opcion == 1: #pesos ARGENTINOS
        pesos_arg = int(input("ingrese cuantos pesos ARG tiene: "))
        cambio = pesos_arg/70.59
        cambio = round(cambio, 2)
        print("El cambio de pesos ARG a Dolares es $",cambio)
        time.sleep(5) #volvera al menu principal luego de 5 seg
    elif opcion == 2: #pesos MEXICANOS
        pesos_mex = int(input("ingrese cuantos pesos MEX tiene: "))
        cambio = pesos_mex/22.46
        cambio = round(cambio, 2)
        print("El cambio de pesos MEX a Dolares es $",cambio)
        time.sleep(5) #volvera al menu principal luego de 5 seg
    elif opcion == 3: #pesos COLOMBIANOS 
        pesos_col = int(input("ingrese cuantos pesos COL tiene: "))
        cambio = pesos_arg/3645.99
        cambio = round(cambio, 2)
        print("El cambio de pesos COL a Dolares es $",cambio)
        time.sleep(5) #volvera al menu principal luego de 5 seg
    elif opcion == 4:
        print("Fin del programa...")
        time.sleep(5) #volvera al menu principal luego de 5 seg
        continuar = False #finaliza el ciclo 
    os.system("cls") #limpiar pantalla para volver al menu sin codigo arriba               
