n=int(input())

for i in range(n):
    entrada=input()
    numero=""
    for i in entrada:
        if i=="A" or i=="B" or i=="C":
            numero+="2"
        if i=="D" or i=="E" or i=="F":
            numero+="3"
        if i=="G" or i=="H" or i=="I":
            numero+="4"
        if i=="J" or i=="K" or i=="L":
            numero+="5"
        if i=="M" or i=="N" or i=="O":
            numero+="6"
        if i=="P" or i=="Q" or i=="R" or i=="S":
            numero+="7"
        if i=="T" or i=="U" or i=="V":
            numero+="8"
        if i=="W" or i=="X" or i=="Y"  or i=="Z":
            numero+="9"
    print(numero)
        