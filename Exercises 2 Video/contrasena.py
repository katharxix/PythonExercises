print ("Validacion contrasena")
con = False

contra = input ("introduzca la contrasena: ")
c= " "
print(len(contra))

if c in contra:
    print("Blank tolkens")

    print ("La contrasena que ha ingresado tiene espacios en blanco")
if len(contra)==8:
    print ("Contrasena OK")
else:
   print("su contrasena debe tener minimo 8 caracteres: ")




