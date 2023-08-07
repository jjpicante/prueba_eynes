import random


def generar_lista_diccionarios():
    """
    Genera una lista de diccionarios con 10 personas y sus edades aleatorias.

    Returns:
        list: Lista de diccionarios con las personas y sus edades.

    Ejemplo:
        >>> lista = generar_lista_diccionarios()
        >>> len(lista)
        10
        >>> all(isinstance(persona, dict) and 'id' in persona and 'edad' in persona for persona in lista)
        True
    """
    lista = []
    while len(lista) < 10:
        id_persona = len(lista) + 1
        edad = random.randint(1, 100)
        lista.append({'id': id_persona, 'edad': edad})
    return lista


def ordenar_lista(elem):
    """
    Ordena una lista de diccionarios de personas por edad, de mayor a menor.

    Args:
        elem (list): Lista de diccionarios de personas.

    Returns:
        list: Lista de diccionarios ordenada por edad.

    Ejemplo:
        >>> lista = [{'id': 1, 'edad': 25}, {'id': 2, 'edad': 42}, {'id': 3, 'edad': 18}]
        >>> ordenar_lista(lista) == [{'id': 2, 'edad': 42}, {'id': 1, 'edad': 25}, {'id': 3, 'edad': 18}]
        True
    """
    elem.sort(key=lambda e: e['edad'], reverse=True)
    print(
        f"La persona más joven es la número {elem[-1]['id']} y tiene {elem[-1]['edad']} años.")
    print(
        f"La persona con más edad es la número {elem[0]['id']} y tiene {elem[0]['edad']} años.")
    return elem


if __name__ == "__main__":
    import doctest
    doctest.testmod()
