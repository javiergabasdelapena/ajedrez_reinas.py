import time
import matplotlib.pyplot as plt


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


def resolver_n_reinas(tablero, fila, n, soluciones, prohibidas):
    if fila == n:
        soluciones.append([f[:] for f in tablero])
        return

    for col in range(n):
        if (fila, col) in prohibidas:
            continue
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1
            resolver_n_reinas(tablero, fila + 1, n, soluciones, prohibidas)
            tablero[fila][col] = 0


def n_reinas(n, prohibidas=None):
    if prohibidas is None:
        prohibidas = set()
    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    resolver_n_reinas(tablero, 0, n, soluciones, prohibidas)
    return soluciones


def dibujar_tablero(ax, tablero, prohibidas, titulo):
    n = len(tablero)
    for i in range(n):
        for j in range(n):
            if (i, j) in prohibidas:
                color = "#777777"
            elif (i + j) % 2 == 0:
                color = "#f0d9b5"
            else:
                color = "#b58863"
            ax.add_patch(plt.Rectangle((j, n - 1 - i), 1, 1, color=color))
            if tablero[i][j] == 1:
                ax.text(j + 0.5, n - 1 - i + 0.5, "♛", ha="center", va="center", fontsize=24, color="black")
            elif (i, j) in prohibidas:
                ax.text(j + 0.5, n - 1 - i + 0.5, "X", ha="center", va="center", fontsize=16, color="white")
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(titulo)


def dibujar_soluciones(soluciones, prohibidas, titulo):
    total = len(soluciones)
    columnas = min(total, 4)
    filas = (total + columnas - 1) // columnas
    fig, ejes = plt.subplots(filas, columnas, figsize=(3.2 * columnas, 3.4 * filas), squeeze=False)
    for k in range(filas * columnas):
        ax = ejes[k // columnas][k % columnas]
        if k < total:
            dibujar_tablero(ax, soluciones[k], prohibidas, "Solución " + str(k + 1))
        else:
            ax.axis("off")
    fig.suptitle(titulo)
    plt.tight_layout()
    plt.show()


print("BONUS 1: N-Reinas con casillas prohibidas")
n = 6
prohibidas = {(0, 1), (2, 3), (4, 5)}
print("Casillas prohibidas (fila, columna):", sorted(prohibidas))
soluciones = n_reinas(n, prohibidas)
print("Se encontraron", len(soluciones), "soluciones.")
for idx, solucion in enumerate(soluciones, start=1):
    print("Solución", idx, ":")
    imprimir_tablero(solucion)

print("BONUS 2: Número de soluciones y tiempo de ejecución")
print("N", "Soluciones", "Tiempo (s)")
for n in [5, 6, 7, 8]:
    inicio = time.perf_counter()
    soluciones_n = n_reinas(n)
    fin = time.perf_counter()
    print(n, len(soluciones_n), round(fin - inicio, 5))

print("BONUS 3: Visualización gráfica")
n = 6
dibujar_soluciones(n_reinas(n, prohibidas), prohibidas, "N = 6 con casillas prohibidas (X)")
dibujar_soluciones(n_reinas(4), set(), "N = 4 sin casillas prohibidas")