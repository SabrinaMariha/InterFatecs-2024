qtdNomes = int(input())
nomes =[]
resultados = []
dic={}
dicORd={}
for i in range(qtdNomes):
   nomes.append(input())
    
rodadas = int(input())

for i in range(rodadas):
    valores= list(map(int,input().split()))
    soma = sum(valores)
    chutes = list(map(int,input().split()))
    
    for  i in range(0,len(chutes)):
        if chutes[i] == soma:
            resultados.append(nomes[i])
        ganhou=resultados.count(nomes[i])
        dic[nomes[i]]=ganhou
valores=[]
nomes=[]
for i in sorted(dic,key=dic.get, reverse=True):
    valores.append(dic[i])
    nomes.append(i)
    

if valores[0]!=valores[1]:
    print(nomes[0],"GANHOU!")
else:
    print("EMPATE")
    