#escreva o código aqui:

#entradas:
comprimento, d_pedagios = map(int,input().split())
custokm,valor_pedagios = map(int,input().split())
#declarando variáveis:
gasolina = int(custokm * comprimento)
n_pedagios = int(comprimento // d_pedagios)
#processamento de variáveis:
custo_total_pedagios = int(n_pedagios*valor_pedagios)
custo_viagem = gasolina + custo_total_pedagios
#saída:
print(custo_viagem)