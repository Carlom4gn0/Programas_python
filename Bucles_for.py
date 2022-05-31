
    

def es_primo():
    seguir = True 
    while seguir == True:
        print("Menu :")
        print("1 - Si desea saber si un numero es primo")
        print("2 - Si quiere saber cuantos primos hay en un rango")
        print("3 - Salir")
        opcion = int(input("opcion:"))
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            seguir = False
        else:
            print("Vuelva a ingresar un dato valido...")


def run():
        es_primo()


if __name__ == "__main__":
    run()