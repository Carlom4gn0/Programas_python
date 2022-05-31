#def conversacion(mensaje):
#    print("Hola")
#    print("hello")
#    print("bye")
#    print(mensaje)

#conversacion("se terminaron los saludos")

a = int(input("ingrese el numero a "))
b = int(input("ingrese el numero b "))


def suma(a,b):
    print("se suman estos numeros",a,"",b)
    resultado = a + b
    return resultado

sumatoria = suma(a,b)
print("el valor dentro de sumatoria es : ",sumatoria)