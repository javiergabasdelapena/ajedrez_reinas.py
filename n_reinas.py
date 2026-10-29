def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if x == 1 else "." for x in fila))
    print("\n")


def es_seguro(tablero, fila, col, n):
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = fila, col
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def resolver_n_reinas(tablero, fila, n, soluciones):
    if fila == n:
        soluciones.append([f[:] for f in tablero])
        return

    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1
            resolver_n_reinas(tablero, fila + 1, n, soluciones)
            tablero[fila][col] = 0


def n_reinas(n):
    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    resolver_n_reinas(tablero, 0, n, soluciones)
    return soluciones


n = 4
soluciones = n_reinas(n)
print("Se encontraron", len(soluciones), "soluciones.")
for idx, solucion in enumerate(soluciones, start=1):
    print("Solución", idx, ":")
    imprimir_tablero(solucion)