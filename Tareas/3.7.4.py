def converBases(num, base, baseToConvert):
    if (base < 2 or base > 10 or baseToConvert < 2 or baseToConvert > 10):
        return False

    def toBase10(numero, base, decimal=0, i=0):
        if (numero == 0):
            return decimal
        else:
            digito = numero % 10
            decimal += digito * (base ** i)
            numero = numero // 10
            return toBase10(numero, base, decimal, i + 1)

    def base10ToBase(num, base):
        if (num == 0):
            return 0
        else:
            return base10ToBase(num // base, base) * 10 + (num % base)

    numBase10 = toBase10(num, base)
    return base10ToBase(numBase10, baseToConvert)

print("CONVERSOR BASE:", converBases(27, 8, 10))


def convertir_base(num, base, baseToConvert):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def toBase10Letras(num, base):
        if (num == 0):
            return 0
        else:
            digito = int(num) % 10
            restNum = int(num) // 10
            return digito + base * toBase10Letras(restNum, base)

    def base10ToBase(num, base):
        if (num < base):
            if (num >= 10):
                return letras[num - 10]
            else:
                return str(num)
        else:
            if (num % base >= 10):
                return base10ToBase(num // base, base) + letras[num % base - 10]
            else:
                return base10ToBase(num // base, base) + str(num % base)

    numBase10 = toBase10Letras(str(num), base)
    resultado = base10ToBase(numBase10, baseToConvert)

    return resultado

print("CONVERSOR BASE LETRAS:", convertir_base(1010101, 2, 24))
