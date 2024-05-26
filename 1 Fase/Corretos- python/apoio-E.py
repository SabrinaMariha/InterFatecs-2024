n = int(input())
grupos= list (map(int, input().split()))
regioes = int(input())

resultados= []

for i in range(regioes):
    linha = input().split()
    numeros = list(map(int, linha[1:]))
    
    resultado = []
    for i in range(len(numeros)):
        resultado.append(int(numeros[i]/grupos[i]))
    
    resultados.append({linha[0]: min(resultado)})
for d in resultados:
    for k in d:
        print(k, d[k])