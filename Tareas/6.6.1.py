def maximo(vector):
    valorMax = 0
    posiMax = 0
    for i in range(len(vector)):
        if (vector[i] > valorMax):
            valorMax = vector[i]
            posiMax = i
    return [valorMax, posiMax]

print(f"Máximo: {maximo([33,10,12])}")

def minimo(vector):
    valorMin = vector[0]
    posMin = 1
    for i in range(len(vector)):
        if (vector[i] < valorMin):
            valorMin = vector[i]
            posiMin = i
    return [valorMin, posiMin]
            
print(f"Mínimo: {minimo([33,10,12])}")

def escalarVector(vector, num):
    res = []
    for i in vector:
            res.append(i*num)
    return res

print(f"Escalar Vector: {escalarVector([34,132,44], 0.5)}")

def sumaVectores(vector1, vector2):
    newVector = [0]*len(vector1)
    for i in range(len(vector1)):
        newVector[i] = vector1[i] + vector2[i]
    return newVector

print(f"Suma Vectores: {sumaVectores([1,2,3], [4,-3,-10])}")

def productoPunto(vector1, vector2, result=0):
    if vector1 == []:
        return result 
    result += vector1[0] * vector2[0]
    return productoPunto(vector1[1:], vector2[1:], result)

print(f"Producto Punto: {productoPunto([2,4,8],[3,6,9])}")
    
def potencia(b, e):
    if not e:
        return 1
    r = potencia(b, e // 2)
    r *= r
    if e % 2:
        r *= b
    return r

def evaluarPoli(coeficientes, x):
    resultado = 0
    grado = len(coeficientes) - 1
    for i in range(grado + 1):
        resultado += coeficientes[i] * (potencia(x, grado - i))
    return resultado

def buscarRaiz(coeficientes, menor, mayor, epsilon=1e-10):
    if evaluarPoli(coeficientes, menor) * evaluarPoli(coeficientes, mayor) > 0:
        return None

    while mayor - menor >= epsilon:
        medio = (menor + mayor) / 2
        if evaluarPoli(coeficientes, medio) == 0:
            return medio
        elif evaluarPoli(coeficientes, menor) * evaluarPoli(coeficientes, medio) < 0:
            mayor = medio
        else:
            menor = medio

    return (menor + mayor) / 2

def solucionesPoli(coeficientes, epsilon=1e-10):
    raices = []
    menor = -1000
    mayor = 1000
    while True:
        raiz = buscarRaiz(coeficientes, menor, mayor, epsilon)
        if raiz is None:
            break
        raices.append(raiz)
        menor = raiz + epsilon
    return raices

print(f"Soluciones Polinomio: {solucionesPoli([3,2,6,2])}")

import math

def potencia(b, e):
    if not e:
        return 1
    r = potencia(b, e // 2)
    r *= r
    if e % 2:
        r *= b
    return r

def distanciaVec(v, w):
    suma = 0
    for i in range(len(v)):
        suma += (v[i] - w[i]) * (v[i] - w[i])
    
    distancia = math.sqrt(suma)
    return distancia

print(f"{distanciaVec([3,4],[5,8])}")

