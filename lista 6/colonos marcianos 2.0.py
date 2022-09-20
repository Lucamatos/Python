#dado o n° de selecionados e total de candidatos;inserir suas notas e id's;selecionar com preferencia de maior nota e menor idade;numero de canditos para analise;notas e id's dos candidatos;imprimir 'sim' para os selecionados e 'nao' caso contrario.

#1°passo:n° de selecionados e n° de candidatos
selecionados,candidatos = [int(x) for x in input().split()]

#2°passo:notas e id's de cada candidatos
lista = []
for i in range(candidatos):
    nota,ids = input().split()
    lista.append({'nota':int(nota),'ids':int(ids)})

#2.1°passo:ordenar por maior nota e menor ID
n = candidatos
for fim in range(n-1,0,-1):
    #determina o indice do maior elemento(imaior)
    imaior = 0
    for i in range(1,fim+1):
        if (lista[i]["nota"] > lista[imaior]["nota"]) or (lista[i]["nota"] == lista[imaior]["nota"] and lista[i]["ids"] < lista[imaior]["ids"]):
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
    nota2,ids2 = input().split()
    lista2.append({'nota2':int(nota2),'ids2':int(ids2)})

#5°passo:verificar se candidatos em analise foram selecionados
for i in range(0,len(lista2)-1):

    n = len(os_chosen)
    esq = 0
    dir = n - 1

    while esq <= dir:
        meio = (esq+dir)//2
        if os_chosen[meio] == lista2[i]:
            break
        elif lista2[i]< os_chosen[meio]:
            dir = meio - 1
        else:
            esq = meio + 1

    if os_chosen[meio] == lista2[i]:
        print('Sim')
    else:
        print('Nao')
