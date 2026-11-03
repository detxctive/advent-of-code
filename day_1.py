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
        
        
