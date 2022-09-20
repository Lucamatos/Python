#1°passo:n° de selecionados e n° de candidatos
selecionados,candidatos = [int(x) for x in input().split()]

#2°passo:matriz de notas e id's de cada candidatos
lista = []
for l in range(candidatos):
    linha = [int(x) for x in input().split()]
    lista.append(linha)
#2.1:ordenar por maior nota(decrescente) e menor ID
n = candidatos
for fim in range(n-1,0,-1):
    #determina o indice do maior elemento(imaior)
    imaior = 0
    for i in range(1,fim+1):
        if (lista[i][0] < lista[imaior][0]) or (lista[i][0] == lista[imaior][0] and lista[i][1] > lista[imaior][1]):
            imaior = i
    #permuta o maior com o ultimo
    lista[imaior],lista[fim] = lista[fim],lista[imaior]

#3°passo:definindo candidatos selecionados
os_chosen = []
for i in range(selecionados):
    os_chosen.append(lista[i])

#4°passo:n° de candidatos para analise
lista2 = []
C_ana = int(input())
for i in range(C_ana):
    linha = [int(x) for x in input().split()]
    lista2.append(linha)

#5°passo:verificar se candidatos em analise foram selecionados
for i in range(C_ana):

    n = len(os_chosen)
    esq = 0
    dir = n - 1

    while esq <= dir:
        meio = (esq + dir) // 2
        if os_chosen[meio] == lista2[i]:
            break
        elif lista2[i] < os_chosen[meio]:
            dir = meio - 1
        else:
            esq = meio + 1

    if os_chosen[meio] == lista2[i]:
        print('Sim')
    else:
        print('Nao')