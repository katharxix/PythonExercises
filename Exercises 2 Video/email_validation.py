#email= False
contadorArroba = 0
contadorPunto = 0

email= input("ingrese la direccion de correo: ")

for i in range (len(email)):

        if email[i]=="@":
            contadorArroba= 1

        if email[i]==".":
            contadorPunto= 1

if (contadorArroba!=0) and (contadorPunto!=0):

    print("email es correcto")

else:

    print("email es incorrecto")