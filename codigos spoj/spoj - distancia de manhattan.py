#escreva o código aqui:

#entradas:
Xm,Ym,Xr,Yr = map(int,input().split())
#declarando variáveis:
distancia_X = int(Xm-Xr)
distancia_Y = int(Ym-Yr)
#processamento de variáveis:
cruzamentos_minimos = distancia_Y + distancia_X
#saída:
print((cruzamentos_minimos-(cruzamentos_minimos))-cruzamentos_minimos)
