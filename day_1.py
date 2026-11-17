archivo = "input.txt"

posicio = 50

rotacions = 0

file = open(archivo)

for linea in file:
    #print("linea:",linea)
    #numero = int(linea[1:-1])
    #print("numero:", numero)
    if linea[0] == "L":

        numero = int(linea[1:-1])*-1
        #print("numero:", numero)
    else:
        numero = int(linea[1:-1])
        #print("numero:", numero)
    posicio = posicio + numero
    if posicio<0:
        while posicio < 0: 
            posicio = 100 + posicio 
    
    elif posicio>=100:
        posicio = posicio % 100
    #print(posicio)

    if posicio == 0:
        rotacions = rotacions + 1


print(rotacions)

#part 2:

archivo = "input.txt"

posicio =  50
posicio_anterior = posicio
rotacions = 0

file = open(archivo)
print("Poscio, rotacions, número, posicio_anterior")
for linea in file:
    
    #print("linea:",linea)
    #numero = int(linea[1:-1])
    #print("numero:", numero)
    if linea[0] == "L":
        numero = int(linea[1:-1])*-1
        #print("numero:", numero)
    else:
        numero = int(linea[1:-1])
        #print("numero:", numero)
    posicio = posicio + numero
    #if posicio<0:
    for paso in range(abs(numero)):
        if numero < 0:
            posicio-=1
        else:
            posicio+=1
        if posicio %100 == 0:
            rotacions+=1

    posicio_anterior = posicio
    print(posicio, rotacions, numero, posicio_anterior)        #posicio = 100 + posicio 

print(rotacions)

#day 1 2024

archivo = "input.txt"
file = open(archivo)
columnaA = list()
columnaB = list()
for linea in file:
    
    listaLinea = linea.strip().split("   ")
    columnaA.append(listaLinea[0])
    columnaB.append(listaLinea[1])
print(columnaA, columnaB) 

columnaA.sort()
columnaB.sort()

print(columnaA, columnaB) 
suma = 0
for index in range(len(columnaA)):
    Resta = abs(int(columnaA[index]) - int(columnaB[index]))
    print(Resta)
    suma = suma + Resta
    print(index, columnaA[index], columnaB[index])
print(suma)

#day 1 part 2

archivo = "input.txt"
file = open(archivo)
columnaA = list()
columnaB = list()
for linea in file:
    
    listaLinea = linea.strip().split("   ")
    columnaA.append(int(listaLinea[0]))
    columnaB.append(int(listaLinea[1]))
#print(columnaA, columnaB) 

columnaA.sort()
columnaB.sort()

print(columnaA, columnaB) 
suma = 0
for index in range(len(columnaA)):
    factor1 = columnaA[index]
    suma += factor1 * columnaB.count(factor1)
print(suma)
