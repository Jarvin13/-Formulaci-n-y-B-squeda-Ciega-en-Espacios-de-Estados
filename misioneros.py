"""
Misioneros y Canibales - Busqueda ciega (BFS y DFS)

Estado: (m, c, b)
  m = misioneros en la orilla izquierda
  c = canibales en la orilla izquierda
  b = 1 si el bote esta en la orilla izquierda, 0 si esta en la derecha
"""

import time
from collections import deque

ESTADO_INICIAL = (3, 3, 1)
ESTADO_OBJETIVO = (0, 0, 0)

# Acciones: (misioneros en el bote, canibales en el bote)
ACCIONES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def es_valido(estado):
    """Un estado es valido si ninguna orilla tiene mas canibales que misioneros
    (cuando en esa orilla hay al menos un misionero)."""
    m, c, b = estado
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    # Orilla izquierda
    if m > 0 and c > m:
        return False
    # Orilla derecha
    if (3 - m) > 0 and (3 - c) > (3 - m):
        return False
    return True


def resultado(estado, accion):
    """Modelo de transicion: aplica la accion y devuelve el nuevo estado."""
    m, c, b = estado
    dm, dc = accion
    if b == 1:  # el bote va de izquierda a derecha
        return (m - dm, c - dc, 0)
    else:       # el bote va de derecha a izquierda
        return (m + dm, c + dc, 1)


def sucesores(estado):
    """Devuelve la lista de (accion, nuevo_estado) validos."""
    lista = []
    for accion in ACCIONES:
        nuevo = resultado(estado, accion)
        if es_valido(nuevo):
            lista.append((accion, nuevo))
    return lista

def bfs():
    """Busqueda en anchura usando una cola (FIFO)."""
    frontera = deque([(ESTADO_INICIAL, [])])  # (estado, camino de acciones)
    visitados = set()
    expandidos = 0
    max_frontera = 1

    while frontera:
        estado, camino = frontera.popleft()
        if estado == ESTADO_OBJETIVO:
            return camino, expandidos, max_frontera
        if estado in visitados:
            continue
        visitados.add(estado)
        expandidos += 1
        for accion, nuevo in sucesores(estado):
            if nuevo not in visitados:
                frontera.append((nuevo, camino + [accion]))
        max_frontera = max(max_frontera, len(frontera))

    return None, expandidos, max_frontera


def dfs():
    """Busqueda en profundidad usando una pila (LIFO)."""
    frontera = [(ESTADO_INICIAL, [])]  # (estado, camino de acciones)
    visitados = set()
    expandidos = 0
    max_frontera = 1

    while frontera:
        estado, camino = frontera.pop()
        if estado == ESTADO_OBJETIVO:
            return camino, expandidos, max_frontera
        if estado in visitados:
            continue
        visitados.add(estado)
        expandidos += 1
        for accion, nuevo in sucesores(estado):
            if nuevo not in visitados:
                frontera.append((nuevo, camino + [accion]))
        max_frontera = max(max_frontera, len(frontera))

    return None, expandidos, max_frontera

def factor_ramificacion_efectivo(n, d):
    """Busca b* tal que n = b* + b*^2 + ... + b*^d (por tanteo, paso 0.0001)."""
    b = 1.0
    while sum(b ** i for i in range(1, d + 1)) < n:
        b += 0.0001
    return b


def analizar_espacio():
    """Cuenta los estados alcanzables y el factor de ramificacion promedio."""
    alcanzables = {ESTADO_INICIAL}
    cola = deque([ESTADO_INICIAL])
    while cola:
        estado = cola.popleft()
        for _, nuevo in sucesores(estado):
            if nuevo not in alcanzables:
                alcanzables.add(nuevo)
                cola.append(nuevo)
    total_sucesores = sum(len(sucesores(s)) for s in alcanzables)
    print("===== ESPACIO DE ESTADOS =====")
    print(f"Estados alcanzables    : {len(alcanzables)}")
    print(f"Ramificacion promedio  : {total_sucesores / len(alcanzables):.3f}")


def mostrar_camino(camino):
    estado = ESTADO_INICIAL
    print("   ", estado)
    for accion in camino:
        estado = resultado(estado, accion)
        lado = "->" if estado[2] == 0 else "<-"
        print(f"    {lado} lleva {accion[0]}M {accion[1]}C  =>  {estado}")


def medir(nombre, algoritmo, repeticiones=1000):
    # Se repite muchas veces porque una sola ejecucion tarda microsegundos
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        camino, expandidos, max_frontera = algoritmo()
    tiempo = (time.perf_counter() - inicio) / repeticiones

    b_ef = factor_ramificacion_efectivo(expandidos, len(camino))

    print(f"\n===== {nombre} =====")
    mostrar_camino(camino)
    print(f"Nodos expandidos       : {expandidos}")
    print(f"Tiempo promedio (s)    : {tiempo:.8f}")
    print(f"Longitud del camino    : {len(camino)}")
    print(f"Tamano max. frontera   : {max_frontera}")
    print(f"Factor ramif. efectivo : {b_ef:.4f}")
    return nombre, expandidos, tiempo, len(camino), max_frontera, b_ef


if __name__ == "__main__":
    analizar_espacio()
    filas = [medir("BFS", bfs), medir("DFS", dfs)]

    print("\n===== TABLA COMPARATIVA =====")
    print(f"{'Alg.':<5}{'Expandidos':>12}{'Tiempo (s)':>14}{'Camino':>8}{'Max front.':>12}{'b*':>8}")
    for n, e, t, l, f, b in filas:
        print(f"{n:<5}{e:>12}{t:>14.8f}{l:>8}{f:>12}{b:>8.4f}")



