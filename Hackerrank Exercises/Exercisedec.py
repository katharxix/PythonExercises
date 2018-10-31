print ("String Formating *Hackerrank*")
entero = int(input("ingrese el numero: "))

def convertobin(entero):
    binario = ''
    while entero // 2 != 0:
        binario = str(entero % 2) + binario
        entero = entero // 2
    return str(entero) + binario

def convert_oct(entero):
    octal = ''
    while entero // 8 !=0:
        octal = str (entero % 8) + octal
        entero = entero // 8
    return str (entero) + octal

def convert_hex (entero):
    hexa= hex(entero)
    hexa = hexa[2:]
    return (hexa)
i=1
while i<=entero:
    print(str(i) + " " + str(convert_oct(i)) + " " + str(convert_hex(i)).upper() + " " + str(convertobin(i)))
    i=i+1