# ------------------
# 1. Gauss-Jordan
# ------------------
def cambiarFila(iFila, matriz):
    if matriz[iFila][iFila] != 1:
        pivote = matriz[iFila][iFila]
        for j in range(len(matriz[0])):
            matriz[iFila][j] = matriz[iFila][j] / pivote

def hacerCeros(filaAct, colAct, matriz):
    if matriz[filaAct][colAct] != 0:
        elemPivote = matriz[filaAct][colAct]
        for j in range(len(matriz[0])):
            matriz[filaAct][j] = matriz[filaAct][j] - (elemPivote * matriz[colAct][j])

def gaussJordan(matriz):
    for i in range(len(matriz)):
        cambiarFila(i, matriz)
        for j in range(len(matriz)):
            if i != j:
                hacerCeros(j, i, matriz)
    return matriz

def printMatriz(matriz):
    for fila in matriz:
        print(fila)

res = gaussJordan([[2, 1, -1, 8],[-3, -1, 2, -11],[-2, 1, 2, -3]])
print("Gauss-Jordan:")
printMatriz(res)

# --------------------------------  
# 2.  Exponenciación de matrices
# --------------------------------
def filaNula(largo):
    return [0] * largo

def matrizNula(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(filaNula(columnas))
    return matriz

def identidad(n):
    matrizIden = matrizNula(n,n)
    for i in range(n):
        matrizIden[i][i] = 1
    return matrizIden

def multiMatriz(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    columnas2 = len(matriz2[0])
    result = matrizNula(filas1, columnas2)
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                result[i][j] += matriz1[i][k] * matriz2[k][j] 
    return result

def expoLogMatri(matriz, n):
    if n == 0:
        return identidad(len(matriz))
    matExpo = expoLogMatri(matriz, n // 2)
    res = multiMatriz(matExpo, matExpo)
    if n % 2 == 1:
        return multiMatriz(res, matriz)
    return res

def tribonacci(n):
    matriz = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        ]
    casos = [[0],[1],[1]]
    matrizExpo = expoLogMatri(matriz, n)
    res = multiMatriz(matrizExpo, casos)
    return res[0][0]

print(f"Tribonacci: {tribonacci(6)}")