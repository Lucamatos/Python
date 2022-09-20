#dado o numero de casais,a idade dos homens e das mulheres,imprimir o homem mais velho e a mulher mais nova, e assim sucessivamente.
#1°passo:numero de casais,idades H, idades M
C = int(input())
i_H = [int(x) for x in input().split()]
i_M = [int(x) for x in input().split()]
#3°passo:organizar homens de forma descrescentes e mulheres de forma crescente
n = len(i_H)
for fim in range(n-1,0,-1):
    for i in range(0,fim):
        if i_H[i] < i_H[i+1]:
            i_H[i],i_H[i+1] = i_H[i+1],i_H[i] 
        if i_M[i] > i_M[i+1]:
            i_M[i],i_M[i+1] = i_M[i+1],i_M[i] 

#4°passo:
for i in range(C):
    print(i_H[i],i_M[i])