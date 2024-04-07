#---- SERIE 1 ----- 
#Utilizando Pila
def serie1P(n):
    if(n == 1):
        return 1
    return 1 + serie1P(n-1)

print(f"Serie 1 Pila: {serie1P(5)}")

#Utilizando Cola
def serie1C(n,a=0):
    if(n < 1):
        return a
    return serie1C(n-1, a + 1)

print(f"Serie 1 Cola: {serie1C(5)}")



#---- SERIE 2 ----- 
#Utilizando Pila
def serie2P(n):
    if n <= 3:
        return 1
    return serie2P(n-1) + serie2P(n-2) + serie2P(n-3)

print(f"Serie 2 Pila: {serie2P(8)}")

#Utilizando Cola
def serie2C(n,a1=1,a2=1,a3=1):
    if n <= 3:
        return a3
    else:
        return serie2C(n-1, a2, a3, a1+a2+a3)

print(f"Serie 2 Cola: {serie2C(8)}")



#---- SERIE 3 ----- 
#Utilizando Pila
def serie3P(n):
    if (n == 1):
        return 3
    return 2 * serie3P(n-1)

print(f"Serie 3 Pila: {serie3P(4)}")

#Utilizando Cola    
def serie3C(n,a=3):
    if (n == 1):
        return a
    return serie3C(n-1, a * 2)

print(f"Serie 3 Cola: {serie3C(4)}")



#---- SERIE 4 ----- 
#Utilizando Pila
def serie4P(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 3
    return 2 * serie4P(n-1) + serie4P(n-2)

print(f"Serie 4 Pila: {serie4P(3)}")

#Utilizando Cola    
def serie4C(n,a1=1,a2=3):
    if (n == 1):
        return a1
    if (n == 2):
        return a2
    return serie4C(n-1, a2, 2 * a2 + a1)

print(f"Serie 4 Cola: {serie4C(3)}")



#---- SERIE 5 ----- 
#Utilizando Pila
def serie5P(n):
    if (n == 1):
        return 2
    if (n == 2):
        return 3
    if (n == 3):
        return 4
    return serie5P(n-1) + serie5P(n-2) + serie5P(n-3)*2

print(f"Serie 5 Pila: {serie5P(5)}")

#Utilizando Cola
def serie5C(n,a1=2,a2=3,a3=4):
    if (n == 1):
        return a1
    if (n == 2):
        return a2
    if (n == 3):
        return a3
    return serie5C(n-1, a2, a3, (a1*2)+a2+a3)

print(f"Serie 5 Cola: {serie5C(5)}")



#---- SERIE 6 ----- 
#Utilizando Pila
def serie6P(n):
    if (n == 1):
        return 1024
    return serie6P(n-1)//2

print(f"Serie 6 Pila: {serie6P(2)}")

#Utilizando Cola
def serie6C(n, a=1024):
    if (n == 1):
        return a
    return serie6C(n-1, a//2)

print(f"Serie 6 Cola: {serie6C(2)}")



#---- SERIE 7 ----- 
#Utilizando Pila
def serie7P(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 5
    return 3 * serie7P(n-2)

print(f"Serie 7 Pila: {serie7P(7)}")

#Utilizando Cola
def serie7C(n, a1=1, a2=5):
    if (n == 1):
        return a1
    if (n == 2):
        return a2
    return serie7C(n-2, a1 * 3, a2 * 3)

print(f"Serie 7 Cola: {serie7C(7)}")