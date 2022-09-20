#testar a utilização de dicionario nessa questão
#1°passo:numero de planetas 
N = int(input())
#3°passo:identificação e grau de urgencia
lista = []
for i in range(N):
    ind,urg = input().split()
    lista.append({"ind":ind,
                  "urg":int(urg)})
#4°passo:ordenar pela maior até a menor urgência
n = N
for fim in range(n-1,0,-1):
    #determina o indice do maior elemento(imaior)
    imaior = 0
    for i in range(1,fim+1):
        if lista[i]["urg"] < lista[imaior]["urg"]:
            imaior = i
    #permuta o maior com o ultimo
    lista[imaior],lista[fim] = lista[fim],lista[imaior]

#5°passo:imprimir a saida
for i in lista:
    print(i["ind"],i["urg"])