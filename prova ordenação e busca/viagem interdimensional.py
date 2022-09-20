#dado o numero de dimensões disponíveis e as solicitadas por morty,imprimir o numero de viagens que serão atendidas por rick
#1°:inserir n° de d. disponíveis d. solicitadas
N,M = [int(x) for x in input().split()]

#2°:inserir d. disponíveis
d_p = [int(x) for x in input().split()]

#3°:inserir d. solicitadas
d_s = [int(x) for x in input().split()]

#4°:realizar busca
d_v = 0
for i in d_s:
    n = len(d_p)
    esq = 0
    dir = n - 1
    while esq < dir:
        meio = esq + (dir - esq) // 2
        if i > d_p[meio]:
            esq = meio + 1
        else:
            dir = meio
    if d_p[esq] == i:
        d_v += 1
#5°:imprimir quantidade de d. que morty irá visitar
print(d_v)
        
