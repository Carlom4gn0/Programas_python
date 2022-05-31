## Numeros Primos (Primalidad)
## Funcion para saber si un numero es primo
def primo(numero):
    from math import sqrt #uso de biblioteca math
    es_primo = True #Se da por acentado que el numero es primo, si llega a ser dividido este cambia su valor a falso
    divisor = 2 

## El metodo que utilize fue el de que el numero solo sea dividido
## solo por los numeros menores a su raiz cuadrada, de ese modo el 
## ciclo while no se repetiria tantas veces y lo hace mas eficiente

    while divisor <= sqrt(numero) and es_primo:
        resto = numero % divisor #Si el resto es 0 el numero no es primo
        if  resto == 0:
            es_primo = False
        else:
            divisor += 1     
    return(es_primo) #devolvera TRUE o FALSE


## Función principal
## Recibe un numero por teclado, este sirve de parametro para la funcion primo
## y asi devolviendome si es o no un numero primo 
def run():
    numero = int(input("Ingrese un numero: "))
    es_primo = primo(numero)
    if es_primo:
        print("Si es primo")
    else:
        print("No es primo")    


if __name__ == "__main__":
    run()