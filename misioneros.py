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
