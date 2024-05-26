
n=int(input())

algoritmos=[]
boasp=[]
desempenho=[]
fluxo=[]
inter=[]
sintaxe=[]
fica=[]

hifen=("-")*30

while(True):
	try:
		entrada=input()
		nome=""
		materias=""
		for i in entrada:
			if i.isalpha():
				nome+=i
			else:
				materias+=i
		listmaterias=materias.split()

		for i in listmaterias:
			if i=="1":
				if len(algoritmos)<n:
					algoritmos.append(nome)
				else:
					fica.append(nome)
			if i=="2":
				if len(boasp)<n:
					boasp.append(nome)
				else:
					fica.append(nome)
			if i=="3":
				if len(desempenho)<n:
					desempenho.append(nome)
				else:
					fica.append(nome)
			if i=="4":
			
				if len(fluxo)<n:
					fluxo.append(nome)
				else:
					fica.append(nome)
			if i=="5":
				if len(inter)<n:
					inter.append(nome)
				else:
					fica.append(nome)
			if i=="6":
				if len(sintaxe)<n:
					sintaxe.append(nome)
				else:
					fica.append(nome)
	except EOFError:
        	break
algoritmos.sort()
boasp.sort()
desempenho.sort()
fluxo.sort()
inter.sort()
sintaxe.sort()
fica.sort()

print(hifen)
print("ALGORITMOS")
print(hifen)

for i in algoritmos:
	print(i)
print("\n")

print(hifen)
print("BOAS PRATICAS")
print(hifen)

for i in boasp:
	print(i)
print("\n")

print(hifen)
print("DESEMPENHO")
print(hifen)

for i in desempenho:
	print(i)
print("\n")

print(hifen)
print("FLUXOGRAMAS")
print(hifen)

for i in fluxo:
	print(i)
print("\n")

print(hifen)
print("INTERPRETACAO DE ENUNCIADOS")
print(hifen)

for i in inter:
	print(i)
print("\n")

print(hifen)
print("SINTAXE DA LINGUAGEM")
print(hifen)

for i in sintaxe:
	print(i)
print("\n")

t=len(fica)
if t>0:
	print(hifen)
	print("FICA PARA A PROXIMA!")
	print(hifen)
	for i in fica:
		print(i)
	print("\n")