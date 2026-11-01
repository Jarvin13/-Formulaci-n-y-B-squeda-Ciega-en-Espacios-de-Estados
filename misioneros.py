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
