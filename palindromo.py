def palindromo(palabra):
    palabra = palabra.replace(" ","") #borra los espacios vacios(los remplaza)
    palabra = palabra.lower() #pone toda la palabra en minuscula
    palabra_invertida = palabra[::-1]   #invierte la palabra o numero
    if palabra == palabra_invertida: 
        return True
    else:
        return False


def run():
    palabra = input("escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:   
        print("Es palindromo")
    else:
        print("no es palindromo...") 


if __name__ == '__main__':
    run()    


# pracrtica de buena programacion, dejar dos espacios entre funciones
# tener una funcion principal ejeplo main, run ...    