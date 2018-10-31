import json
import base64

archivo= open('C:\\Users\\kchavesb\\PycharmProjects\\TallerPy\\data.json', "r")
print(archivo)
json_strings=json.load(archivo)
print(json_strings)

for salon in json_strings['primaria'][0]['curso']:
    i=0
    y=''
    lista = []
    print('**********************************************')
    print('Grado: ' + str(salon['grado']) + salon['curso'])
    for alumno in salon['estudiante']:
        if alumno['nota'] > i:
            i = alumno['nota']
            y = alumno['nombre']

        if alumno == salon['estudiante'][-1]:
            print(y + ' '+str(i))


