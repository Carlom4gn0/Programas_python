print("bienvenido al programa de conversor de monedas")
pesos = input("Cuantos pesos Argentinos quieres convertir a Dolares? ")
pesos = float(pesos)
cambio = pesos /70.52
cambio = round(cambio, 2)
print("Tu tienes : $", cambio," dolares")
dolares = input("cuantos dolares quieres convertir a pesos Argentnos ?: ")
dolares = float(dolares)
cambio = dolares * 70.52
cambio = round(cambio, 2)
print("Tu tienes : $",cambio," Pesos ARG")