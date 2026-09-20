matriz = []

# Ingresar los 25 valores
for i in range(5):
    fila = []
    for j in range(5):
        numero = int(input(f"Ingrese el valor [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz ingresada:")

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()