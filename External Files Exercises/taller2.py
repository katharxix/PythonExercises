import json
import base64

archivo = open('C:\\Users\\kchavesb\\PycharmProjects\\TallerPy\\data.json', "r")
print(archivo)
json_strings = json.load(archivo)
print(json_strings)

for salon in json_strings['primaria'][0]['curso']:
    i = 0
    y = ''
    print('**********************************************')
    print('Grado: ' + str(salon['grado']) + salon['curso'])

    print('*********************ALUMNOS DIEZ*************************')
    for alumno in salon['estudiante']:
        if alumno['nota'] > i:
            i = alumno['nota']
            y = alumno['nombre']


        if alumno == salon['estudiante'][-1]:
            print(y + ' ' + str(i))
            a = type(y)
            print(a)

    primero5 = 0
    print('*********************ALUMNOS CINCO PRIMARIA*************************')
    for alumno in salon['estudiante']:
        i = alumno['nota']
        y = alumno['nombre']
        if (i == 5) and (primero5 == 0):
            primero5 = 1
            print("Alumnos con nota 5: "+str(y) + ' ' + str(i))

print('**********************************************')
for salon in json_strings['bachillerato'][0]['curso']:
    x = 0
    z = ''
    lista1 = []
    print('Grado: ' + str(salon['grado']) + salon['curso'])

    print('*********************ALUMNOS DIEZ*************************')
    for alumno1 in salon['estudiante']:
        if alumno1['nota'] > x:
            x = alumno1['nota']
            z = alumno1['nombre']

        if alumno1 == salon['estudiante'][-1]:
            list_result = [z, str(x)]
            print(list_result)
            b = type(z)

    primero5 = 0
    print('*********************ALUMNOS CINCO BACHILLERATO*************************')
    for alumno in salon['estudiante']:
        i = alumno['nota']
        y = alumno['nombre']
        if (i == 5) and (primero5 == 0):
            primero5 = 1
            print("Alumnos con nota 5: "+str(y) + ' ' + str(i))

print('**********************************************')


