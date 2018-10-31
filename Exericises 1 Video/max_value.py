print("Max Value")

num1 = input("ingrese el numero 1:")
num2 = input("ingrese el numero 2: ")


def DevuelveMax(num1, num2):
    respuesta= "no se"
    if num1 < num2:
        respuesta= 'el numero mayor es: ' + str(num2)
    else:
        respuesta= "el numero mayor es: " + str(num1)

    return respuesta


print(DevuelveMax(int(num1),int(num2)))
