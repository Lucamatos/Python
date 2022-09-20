#1°passo:definir dimensão das matriz de bugs -->
L,C = [int(x) for x in input().split()]
matriz_B = [] #matriz de bugs vazia

#2°passo:determinar bugs da matriz com 0 e 1 -->
for i in range(L):
  X_B = [int(x) for x in input().split()] #0 ou 1
  matriz_B.append(X_B)
bugs = 0 
for l in range(L):
  for c in range(C):
    if matriz_B[l][c]==1:
      bugs+=1
     
#3°passo:numero de tentativas -->
tentativas = int(input())

#4°passo:posições a serem atingidas p/kd tentativa -->
bugs_shooted = 0
for i in range(tentativas):  
  l1, c2 = [int(x) for x in input().split()] #posição a ser acessada
  if matriz_B[l1-1][c2-1] ==1: #verifica se a coordenada é =1
    bugs_shooted+=1 #se for =1 o besouro é morto
    matriz_B[l1-1][c2-1] = 0 #precisa zerar a posição, pq no caso de tentativas iguais, não contar como +1 besouro morto

#5°passo:verificar se todos besouros foram mortos e fazer impressão de acordo -->
if bugs_shooted == bugs:
  print('HASTA LA VISTA BABY')
elif bugs_shooted < bugs:
  print('ILL BE BACK')