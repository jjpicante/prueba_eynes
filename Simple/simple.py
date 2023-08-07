import random


def generar_lista_diccionarios():
    lista = []
    while len(lista) < 10:
        id_persona = len(lista) + 1
        edad = random.randint(1, 100)
        lista.append({'id': id_persona, 'edad': edad})
    return lista


def ordenar_lista(elem):
    elem.sort(key=lambda e: e['edad'], reverse=True)
    print(
        f"La persona más joven es la número {elem[-1]['id']} y tiene {elem[-1]['edad']} años.")
    print(
        f"La persona con más edad es la número {elem[0]['id']} y tiene {elem[0]['edad']} años.")
    return elem


print(ordenar_lista(generar_lista_diccionarios()))
