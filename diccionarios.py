


def run():
    # mi_diccionario = {
    #     "llave1":1,
    #     "llave2":2,
    #     "llave3":3,
    # }
    # print(mi_diccionario)
    poblacion_paises = {
        "Argentina" : 44938712,
        "Brasil" : 210147125,
        "Colombia": 50372424,
    }
    #print(poblacion_paises["Argentina"])
    #keys devuelve impresas las llaves
    #values devuelve el contenido de las llaves

    #for pais in poblacion_paises.keys:
        #print(pais)

    # para imprimir todo en una oración
    for pais, poblacion in poblacion_paises.items():
        print(pais,"tiene",str(poblacion),"habitantes")

if __name__ == "__main__":
    run()
