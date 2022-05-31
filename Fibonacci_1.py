## SUCECIÓN DE FIBONACCI : 0,1,1,2,3,5,8,13,21,34,55...
## Esta sucecion consiste en que cada termino es la suma de los dos anteriores
## comenzando con los terminos 0 y 1


def run():
    a = 0
    b = 0
    contador = 0
    num = int(input("Ingrese hasta que termino de fibonacci quiera ver: "))
    while True:
            c = a + b
            if c == 0:
                print("Termino",contador,":",c)
                contador += 1
                b = 1
                if contador == num:
                    break
            elif contador < 2:
                print("Termino",contador,":",c)
                contador += 1
                if contador == num:
                    break
            else:
                print("Termino",contador,":",c)
                a = b
                b = c
                contador +=1
                if contador == num:
                    break


if __name__ == "__main__":
    run()
