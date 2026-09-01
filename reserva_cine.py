# Programa para reservar asientos en una sala de cine

# Crear una matriz de 3 filas por 4 columnas
# 0 significa asiento libre
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir al usuario la fila y columna del asiento
fila = int(input("Ingrese la fila del asiento (0 a 2): "))
columna = int(input("Ingrese la columna del asiento (0 a 3): "))

# Reservar el asiento
asientos[fila][columna] = 1

# Mostrar el estado de la sala
print("\nEstado de la sala:")

# Recorrer la matriz con bucles anidados
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
