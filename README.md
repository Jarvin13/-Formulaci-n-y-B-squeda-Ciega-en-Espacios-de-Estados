# Misioneros y Caníbales – BFS vs DFS

Tarea DG_S4: formulación del problema de los misioneros y caníbales como espacio de estados y resolución con búsqueda no informada (BFS y DFS).

## Representación
Estado `(m, c, b)`: misioneros y caníbales en la orilla izquierda, y `b = 1` si el bote está a la izquierda.

- Estado inicial: `(3, 3, 1)`
- Estado objetivo: `(0, 0, 0)`
- Acciones: `(1,0) (2,0) (0,1) (0,2) (1,1)`

## Ejecución
```bash
python misioneros.py
```

## Métricas que imprime
- Nodos expandidos
- Tiempo promedio de ejecución (1000 repeticiones)
- Longitud del camino
- Tamaño máximo de la frontera (memoria)
- Factor de ramificación efectivo b*
