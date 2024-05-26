n=int(input())
superior=0
esquerda=0
centro=0
direita=0
inferior=0
for i in range(n):
    matriz=[]
    
    for i in range(6):
        linha=list(map(int,input().split()))
        matriz.append(linha)
    superior+=sum(matriz[0])
    esquerda+=matriz[1][0]+matriz[2][0]+matriz[3][0]+matriz[4][0]
    centro+=matriz[1][1]+matriz[2][1]+matriz[3][1]+matriz[4][1]
    direita+=matriz[1][2]+matriz[2][2]+matriz[3][2]+matriz[4][2]
    inferior+=sum(matriz[5])
    
    lista=[superior,esquerda,centro,direita,inferior]
    
maior = max(lista)
if maior==superior:
    print("superior")
elif maior==esquerda:
    print("esquerda")
elif maior==centro:
    print("centro")
elif maior==direita:
    print("direita")
elif maior==inferior:
    print("inferior")