from operator import itemgetter
import json
import numpy as np
import base64

archivo = open('C:\\Users\\kchavesb\\PycharmProjects\\TallerPy\\data.json', "r")
print(archivo)
json_strings = json.load(archivo)
print(json_strings)

i = 0
y = ''
total = 0
print('**********************************************')

print('**********************************************')
nprimaria = 0
totalavgPrimaria = 0
avgprimaria = 0

for salon in json_strings['primaria'][0]['curso']:
    nsalon = 0
    TotalAvgSalon = 0
    avgcurso = 0
    numero_notas = 0
    suma_notas = 0
    avg_scoreXsalon = 0
    count = 0
    total_result = 0

    print('**********************************************')
    print('Grado: ' + str(salon['grado']) + salon['curso'])
    for alumno in salon['estudiante']:
        i = alumno['nota']
        y = alumno['nombre']
        numero_notas = numero_notas + 1
        suma_notas = suma_notas + i
        print(y + ' ' + str(i))
    avg_scoreXsalon = suma_notas / numero_notas

    result = [avg_scoreXsalon]
    for k in result:
        count = count + 1
        total_result = total_result + i
    avg_score_2 = total_result / count
    print(avg_score_2)

print(result)
# print(avg_scoreXsalon)
# TotalAvgSalon = TotalAvgSalon +avg_scoreXsalon
#Nsalon = Nsalon + 1
#AvgCurso = TotalAvgSalon / Nsalon
# print(AvgCurso)


