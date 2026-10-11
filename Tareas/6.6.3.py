def ultimosN(lista,n):
    return lista[-n:]

print(f"Ultimos N: {ultimosN([1,2,3,4,5], 2)}")

def ordenarLista(lista):
    if (lista == []):
        return []
    pivot = lista[0]
    mayores = []
    menores = []
    for i in range(1, len(lista)):
        if (lista[i] < pivot):
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return ordenarLista(menores) + [pivot] + ordenarLista(mayores)

print(f"Lista Ordenada: {ordenarLista([4,9,2,5,1])}")

def verificarSub(lista):
    for i in lista:
        if (type(i) == type([])):
            return True
    return False

print(f"Verificiar Sublista: {verificarSub([1,2,3,4,5])}")

def encontrarSub(lista, i, j):
    sublista = []
    for i in range(i, j):
        sublista.append(lista[i])
    return sublista

print(f"Encontrar Sublista: {encontrarSub([1,2,3,4,5], 3, 5)}")

def multiplosLista(lista,k):
    cont = 0
    for i in lista:
        if (i % k == 0):
            cont += 1
    return cont
            
print(f"Multiplos de K: {multiplosLista([1,2,3,4,5,6], 2)}")

def primerosN(n):
    enteros = []
    for i in range(1, n + 1):
        enteros.append(i)
    return enteros

print(f"Primeros N enteros: {primerosN(5)}")

def criba(n):
    primos = [0]*2 + [1] * (n+1)
    p = 2
    while (p * p <= n):
        if (primos[p] == 1):
            for i in range(p * p, n+1, p):
                primos[i] = 0
        p += 1
    return primos

def primerosPrimos(n):
    tablero = criba(n)
    primos = []
    for i in range(1, n+1):
        if tablero[i] == 1:
            primos.append(i)
    return primos

print(f"Primeros Primos: {primerosPrimos(5)}")

def intercambiar(lista,i,j):
    lista[i] ^= lista[j]
    lista[j] ^= lista[i]
    lista[i] ^= lista[j]
    return lista

print(f"Intercambiar: {intercambiar([1,2,3,4,5], 1,4)}")

def remplazar(lista,a,b):
    for i in range(len(lista)):
        if lista[i] == a:
            lista[i] = b
    return lista

print(f"Remplazar: {remplazar([1,2,3,1,1], 1,4)}")

def multi(lista):
    result = 1
    for i in lista:
        result *= i
    return result

print(f"Multiplicación Lista: {multi([1,2,3,4,5])}")

def eliminarDupli(lista):
    listaNoDupli = []
    for elemento in lista:
        if elemento not in listaNoDupli:
            listaNoDupli.append(elemento)
    return listaNoDupli

print(f"Eliminar Duplicados: {eliminarDupli([7,8,7,3,2,3])}")

def invertir(lista):
    inv = []
    for i in lista:
        inv = [i] + inv
    return inv

print(f"Invertir: {invertir([1,2,3,4,5])}")

def remvEspacios(string):
    newString = ""
    for i in string.split():
        newString += i
    return newString

def palindromo(string):
    string = remvEspacios(string)
    if string == string[::-1]:
        return True
    else:
        return False
    
print(f"Palíndromo: {palindromo("oso")}")

def combinacion(lista, n):
    if len(lista) == n:
        return [lista]
    if n == 0:
        return [[]]
    
    result = []
    primerEle = lista[0]
    for C in combinacion(lista[1:], n-1):
        result.append([primerEle] + C)
    result += combinacion(lista[1:], n)
    return result

print(f"Combinaciones: {combinacion([6, 7, 8], 2)}")

def permutaciones(lista):
    res = [[]]
    for e in lista:
        listaPermuta = []
        for p in res:
            for i in range(len(p) + 1):
                newPermuta = p[:i] + [e] + p[i:]
                listaPermuta.append(newPermuta)
        res = listaPermuta
    return res

print(f"Permutaciones: {permutaciones(["A","B","C"])}")

def expoConjuntos(lista, n):
    if n == 0:
        return [[]]
    conjExpo = expoConjuntos(lista, n // 2)
    r = []
    for i in conjExpo:
        for j in conjExpo:
            r.append(i + j)

    if n % 2:
        resultado = []
        for i in lista:
            for t in r:
                resultado.append([i] + t)
        return resultado
    return r

print(f"Exponenciación Conjuntos: {expoConjuntos([0,1], 3)}")




