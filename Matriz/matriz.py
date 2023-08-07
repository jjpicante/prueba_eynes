import numpy as np

# Funcion que crea matriz aleatoria 5x5


def crear_matriz():
    return np.random.randint(0, 5, size=(5, 5))

# Función que busca secuencia de números


def buscar_secuencia(matriz):
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


print(buscar_secuencia(crear_matriz()))
