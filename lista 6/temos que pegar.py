#classificar os pomkemons por força ou nome, em ordem crescente ou descrescente
#1°passo:inserir qtd./poke.,classificação,ordem
N,C,O = input().split()
N = int(N)
#2°passo:inserir pokmemons e força
lista = []
for i in range(N):
    poke,força = input().split()
    lista.append({"poke":poke,"força":int(força)})

n = N
#3°passo: definir as ordenações
#ordenação por nome(usando selection sort)
if C == "N":
    #ordem da classificação
    if O=="C": #crescente
        for fim in range(n-1,0,-1):
            #determina o indice do maior elemento(imaior)
            imaior = 0
            for i in range(1,fim+1):
                if lista[i]["poke"] > lista[imaior]["poke"]:
                    imaior = i
            #permuta o menor com o ultimo
            lista[imaior],lista[fim] = lista[fim],lista[imaior]
    elif O=="D": #descrescente
        for fim in range(n-1,0,-1):
            #determina o indice do maior elemento(imaior)
            imaior = 0
            for i in range(1,fim+1):
                if lista[i]["poke"] < lista[imaior]["poke"]:
                    imaior = i
            #permuta o maior com o ultimo
            lista[imaior],lista[fim] = lista[fim],lista[imaior]
#ordenação por força
elif C=="L":
    #ordem da classificação
    if O=="C": #crescente
        for fim in range(n-1,0,-1):
            #determina o indice do maior elemento(imaior)
            imaior = 0
            for i in range(1,fim+1):
                if lista[i]["força"] > lista[imaior]["força"]:
                    imaior = i
            #permuta o maior com o ultimo
            lista[imaior],lista[fim] = lista[fim],lista[imaior]
    elif O=="D": #decrescente
        for fim in range(n-1,0,-1):
            #determina o indice do maior elemento(imaior)
            imaior = 0
            for i in range(1,fim+1):
                if lista[i]["força"] < lista[imaior]["força"]:
                    imaior = i
            #permuta o menor com o ultimo
            lista[imaior],lista[fim] = lista[fim],lista[imaior]
#4°passo:imprimir a saída
for i in lista:
    print(i["poke"],i["força"])