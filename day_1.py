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
        
        
