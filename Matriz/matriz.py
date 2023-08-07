import numpy as np


def crear_matriz():
    """
    Esta función crea una matriz aleatoria de tamaño 5x5.

    Returns:
        numpy.ndarray: Matriz aleatoria 5x5.
    """
    return np.random.randint(0, 5, size=(5, 5))


def buscar_secuencia(matriz):
    """
    Esta función busca secuencias de números idénticos en filas y columnas de una matriz.

    Args:
        matriz (numpy.ndarray): Matriz en la que se buscarán las secuencias.

    Returns:
        tuple or str: Si se encuentran secuencias, devuelve una tupla con la información de las secuencias
                      y la matriz original. Si no se encuentran secuencias, devuelve un mensaje indicando
                      que no se encontró ninguna coincidencia.
    """
    respuesta = []

    # Bucle que busca en las filas:
    for i in range(5):
        for j in range(2):
            if matriz[i][j] == matriz[i][j + 1] == matriz[i][j + 2] == matriz[i][j + 3]:
                respuesta.append(
                    f"fila número {i}, se repite el {matriz[i][j]} desde posición {j} hasta {j + 3}")

    # Bucle que busca en las columnas:
    for j in range(2):
        for i in range(5):
            if matriz[j][i] == matriz[j + 1][i] == matriz[j + 2][i] == matriz[j + 3][i]:
                respuesta.append(
                    f"columna número {i}, se repite el {matriz[j][i]} desde posición {j} hasta {j + 3}")

    if respuesta:
        return respuesta, matriz
    else:
        return "no se encontró ninguna coincidencia", matriz


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Ejemplo de uso con una matriz específica
print(buscar_secuencia(np.array([[1, 2, 3, 4, 3],
                                 [2, 2, 2, 2, 3],
                                 [3, 4, 5, 5, 3],
                                 [0, 1, 2, 3, 3],
                                 [5, 4, 3, 2, 1]])))
