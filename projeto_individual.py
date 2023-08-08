import numpy as np
import matplotlib.pyplot as plt

#Função de simulação de dados: Simula a soma do resultado do lançamento de dois dados (1-6):
data_simulation = lambda : np.random.randint(1,7) + np.random.randint(1,7)
    
#Função de simulação múltipla: Dado um parâmetro n, chama n a função data_simulation: 
multiple_simulation = lambda n: np.array([data_simulation() for i in range(n)])

#Análise de dados: 
n = int(input('Digite a quantidade de simulações: '))
total_simulations = multiple_simulation(n)

#Média, Máximo e Mínimo: 
print(f'A média dos resultados é: {total_simulations.mean():.2f}')
print(f'O lançamento máximo é: {total_simulations.max()}')
print(f'O lançamento mínimo é: {total_simulations.min()}')

#Cria um dicionário cuja as chaves são os lançamentos possíveis e os valores zerados:
dice_roll_count = {i: 0 for i in range(2, 13)}
#Popula o dicionário com a contagem dos lançamentos: 
for dice_roll in total_simulations:
    dice_roll_count[dice_roll] += 1

#Plota o gráfico com a contagem dos elementos:
plt.bar(dice_roll_count.keys(),dice_roll_count.values(), color='#23238E') 
plt.xlabel('Lançamentos')
plt.ylabel('Contagem')
plt.title('Contagem por lançamentos')
plt.show()

'''
Da análise dos resultados percebe-se que, quanto maior o n, mais próxima a
distribuição dos lançamentos será da distribuição normal de probabilidades da 
soma de lançamentos de 2 dados. 

Isto é, a soma de lançamentos de valor 7 possui probabilidade maior (6/36) de 
ocorret, enquanto as somas de valores 2 e 12 possuem a probabilidade menor (1/36).

Com isso, pode-se afirmar que a suposição de jogo justo é correta e que o jogador
possui maior probabilidade de acerto se apostar no número 7.
'''