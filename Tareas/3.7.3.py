def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base

    media_potencia = potencia(base, exponente // 2)
    resultado = media_potencia * media_potencia
    if exponente % 2 == 1:
        resultado *= base
    return resultado

def mcd(num1, num2):
    if (num1 == num2):
        return num1
    elif (num1 > num2):
        return mcd(num1 - num2, num2)
    elif (num1 < num2):
        return mcd(num1, num2 - num1)

print("MCD:", mcd(18, 24))


def mcdEucli(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return mcdEucli(num2, num1 % num2)

print("MCD EUCLI:", mcdEucli(18, 24))


def mcm(num1, num2):
    return (num1 * num2) // mcdEucli(num1, num2)

print("MCM:", mcm(18, 24))


def sumaCubos(num):
    if (num == 1):
        return num
    else:
        return (potencia(num, 3)) + sumaCubos(num - 1)

print("SUMA CUBOS:", sumaCubos(3))


def esPrimo(num, divisor=2):
    if (num < 2):
        return False
    elif (divisor * divisor > num):
        return True
    elif (num % divisor == 0):
        return False
    else:
        return esPrimo(num, divisor + 1)

print("ES PRIMO:", esPrimo(10))


def nsimoPrimo(num, numeroVerificar=2, contador=0):
    if (contador == num):
        return numeroVerificar - 1
    if (esPrimo(numeroVerificar)):
        return nsimoPrimo(num, numeroVerificar + 1, contador + 1)
    else:
        return nsimoPrimo(num, numeroVerificar + 1, contador)

print("N-SIMO PRIMO:", nsimoPrimo(6))


def cantDigitos(num):
    if (num == 0):
        return num
    else:
        return cantDigitos(num // 10) + 1

print("CANT DÍGITOS:", cantDigitos(500))


def invertNum(num, newNum=0):
    if (num == 0):
        return int(newNum)
    else:
        digito = num % 10
        newNum = str(newNum) + str(digito)
        return invertNum(num // 10, newNum)

print("INVERTIR NUM:", invertNum(1853))


def factorial(num, acum=1):
    if (num == 0):
        return acum
    else:
        return factorial(num - 1, acum * num)

print("FACTORIAL:", factorial(5))


def sumaFracciones(num):
    if (num == 0):
        return num
    else:
        return ((potencia(-1, num)) / num) + sumaFracciones(num - 1)

print("SUMA FRACC:", sumaFracciones(3))


def sumaDeSumaAdentro(i, j):
    if (j == i):
        return i * j
    else:
        return (i * j) + sumaDeSumaAdentro(i, j + 1)

def sumaDeSumaFuera(num, i=1):
    if (i == num):
        return sumaDeSumaAdentro(i, j=1)
    else:
        return sumaDeSumaAdentro(i, j=1) + sumaDeSumaFuera(num, i + 1)

print("SUMA DE SUMA:", sumaDeSumaFuera(3))


def producto(num, result=1):
    if (num == 0):
        return result
    else:
        result = result * 1 / potencia(2, num)
        return producto(num - 1, result)

print("PRODUCTO:", producto(3))


def productSumaDentro(i, j, resultado2=0):
    if (j > potencia(i,2)):
        return resultado2
    else:
        resultado2 += ((2 * i) / j)
        return productSumaDentro(i, j + 1, resultado2)

def productSumaFuera(num, i=2, resultado=1):
    if (i > num):
        return resultado
    else: 
        resultado *= productSumaDentro(i, j=1)
        return productSumaFuera(num, i + 1, resultado)
    
print("PROD SUMA:", productSumaFuera(3))


def tercerProducto(num, i, j, k, resultado3=1):
    if (k > num):
        return resultado3
    else:
        resultado3 *= ((2 * i) + (3 * j) + k)
        return tercerProducto(num, i, j, k+1, resultado3)

def segundaSuma(num, i, j, resultado2=0):
    if (j > num):
        return resultado2
    else:
        resultado2 += tercerProducto(potencia(num, 2), i, j, j)
        return segundaSuma(num, i, j + 1, resultado2)

def primerProducto(num, i=1, resultado=1):
    if (i > num):
        return resultado
    else:
        resultado *= segundaSuma(num, i, i)
        return primerProducto(num, i + 1, resultado)

print("MEZCLA GENE:", primerProducto(3))


def numsPitagoras(num, divisor=1, suma=0):
    if (divisor >= num):
        if (suma == num): 
            return 0
        elif (suma > num):
            return 1
        elif (suma < num):
            return -1
    else:
        if (num % divisor == 0):
            suma += divisor
        return numsPitagoras(num, divisor + 1, suma)

print("NUMS PITAGORAS:", numsPitagoras(28))


def sumaDeDivisores(num, divisor=1, suma=0):
    if (divisor >= num):
        return suma
    else:
        if (num % divisor == 0):
            suma += divisor
        return sumaDeDivisores(num, divisor + 1, suma)

def verifyAmigos(num1, num2):
    verifyNum1 = sumaDeDivisores(num1)
    verifyNum2 = sumaDeDivisores(num2)
    return verifyNum1 == num2 and verifyNum2 == num1

print("VERIFICACION AMIGO:", verifyAmigos(220, 284))

def devolverAmigo(num, guess=1, amigo=0):
    amigo = sumaDeDivisores(num, guess)
    if (verifyAmigos(num, amigo)):
        return amigo
    elif guess > num:
        return -1
    else:
        return devolverAmigo(num, guess + 1)

print("DEVOLVER AMIGO:", devolverAmigo(220))


def goldbach(num, primoUno=2):
    primoDos = num - primoUno
    if (esPrimo(primoDos) and esPrimo(primoUno)):
        numeros = primoUno, primoDos
        return numeros
    else:
        return goldbach(num, primoUno + 1)

print("GOLDBACH:", goldbach(8))


def cuatroCuadrados(n, a=0, b=0, c=0, d=0):
    if (n == 0):
        numsCuadrados = a, b, c, d
        return numsCuadrados
    elif ((b * b) > (n - (a * a))):
        return cuatroCuadrados(n, a + 1, 0, 0)
    elif ((c * c) > (n - (a * a) - (b * b))):
        return cuatroCuadrados(n, a, b + 1, 0)
    else:
        d = int((n - a * a - b * b - c * c) ** 0.5)
        if ((a * a) + (b * b) + (c * c) + (d * d) == n):
            numsCuadrados = a, b, c, d
            return numsCuadrados
        else:
            return cuatroCuadrados(n, a, b, c + 1)

print("NUMS CUADRADOS:", cuatroCuadrados(5))


def numTriangular(num):
    return num * (num + 1) // 2

def tresTriangulares(m, a=0, b=0, c=0):
    if (m == 0):
        numsTriangulares = a, b, c
        return numsTriangulares
    elif (numTriangular(b) > m - (numTriangular(a))):
        return tresTriangulares(m, a + 1, a + 1, 0)
    elif (numTriangular(c) > (m - (numTriangular(a)) - (numTriangular(b)))):
        return tresTriangulares(m, a, b + 1, 0)
    else:
        valorC = numTriangular(c)
        if (numTriangular(a) + numTriangular(b) + valorC == m):
            numsTriangulares = a, b, c
            return numsTriangulares
        else:
            return tresTriangulares(m, a, b, c + 1)

print("NUMS TRIANGULARES:", tresTriangulares(40))


def numCuadrado(num):
    return num * num

def minTriangulares(m, num=1):
    if (numTriangular(num) == m):
        return 1
    elif (numTriangular(num) > m):
        return -1
    else:
        conNum = minTriangulares(m - numTriangular(num), num + 1)
        sinNum = minTriangulares(m, num + 1)
        if ((conNum != -1) and (sinNum == -1 or conNum < sinNum)):
            return conNum + 1
        elif (sinNum != -1):
            return sinNum
        else:
            return -1

def minCuadrados(m, num=1):
    if (numCuadrado(num) == m):
        return 1
    elif (numCuadrado(num) > m):
        return -1
    else:
        conNum = minCuadrados(m - numCuadrado(num), num + 1)
        sinNum = minCuadrados(m, num + 1)
        if ((conNum != -1) and (sinNum == -1 or conNum < sinNum)):
            return conNum + 1
        elif (sinNum != -1):
            return sinNum
        else:
            return -1

print("MIN TRIANGUALRES:", minTriangulares(40))
print("MIN CUADRADOS:", minCuadrados(5))


def fibonacci(num, antes = 0, sig = 1):
    if (num == 0):
        return antes
    else:
        return fibonacci(num-1, sig, sig + antes)

def carmichael(num, inicio=2):
    fibonacciNum = fibonacci(num)
    if (num == 1 or num == 2 or num == 6 or num == 12):
        return -1
    elif inicio > num:
        return -1 
    elif (esPrimo(inicio) and (fibonacciNum % inicio == 0)):
        return inicio
    else:
        return carmichael(num, inicio + 1)

print("CARMICHAEL:", carmichael(14))
