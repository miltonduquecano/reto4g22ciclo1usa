fallas_totales=0
falla_detectada=0
indice=0
baldosas_unicas=[]
ultima_posicion_baldosas_unicas=[]
cadena=""
n, k = [int(x) for x in list(input().split(' '))]
baldosas = [int(x) for x in list(input().split(' '))]
baldosas_cadena=list(baldosas)
count=0
for value in baldosas:
    if value in baldosas_unicas:
        fallas_totales+=1
    if value in baldosas_unicas:
        index = baldosas_unicas.index(value)
        posicion = ultima_posicion_baldosas_unicas[index]
        if count - posicion <= k:
            falla_detectada+=1
    if value not in baldosas_unicas:
        baldosas_unicas.append(value)
        ultima_posicion_baldosas_unicas.append(count)
    else:
        posicion = baldosas_unicas.index(value)
        ultima_posicion_baldosas_unicas[posicion]=count
    count+=1
print(f"{fallas_totales} {falla_detectada} {len(baldosas)}")