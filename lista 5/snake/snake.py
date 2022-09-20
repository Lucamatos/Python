#dada a matriz,as posições dos ovos e das armadilhas, dizer o total de ovos no final do percurso.
#o percurso é percorrido da esquerda->direita depois direita->esquerda e assim por diante.
##########################################################

#1°passo:entrada das dimensões da matriz >
L,C = [int(x) for x in input().split()]
percurso = []

#2°passo:definindo elementos da matriz > 
for l in range(L):
    linha = [int(x) for x in input().split()]
    percurso.append(linha)

#3°passo:iniciando percurso > coleta e perda de ovos >
#percurso:começa da esquerda pra direita,proxima linha é percorrida de maneira inversamente a anterior >
ovos = 0
for l in range(L):
    #percorre a linha no sentido esquerda>direita
    if l % 2 == 0:
        for c in range(C):
            ovos += percurso[l][c]
            if ovos < 0:
                ovos = 0
    #percorre a linha no sentido direita>esquerda
    if l %2 == 1:
        for c in range(C-1,-1,-1):
            ovos += percurso[l][c]
            if ovos<0:
                ovos = 0
            
#4°passo:imprime o total de ovos:
print(ovos)