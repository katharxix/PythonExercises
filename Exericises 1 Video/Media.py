print("Media")

num1= input("ingrese el número 1: ")
num2= input("ingrese el numero 2: ")
num3= input("ingrese el numero 3: ")

def calcular_media (*numeros):
    suma = 0
    for numero in numeros:
        suma += int(numero)
    divisor=len(numeros)
    return suma/divisor

print(calcular_media(num1, num2, num3, 4, 5, 6, 7, 8, 9, 10)) #invoke function