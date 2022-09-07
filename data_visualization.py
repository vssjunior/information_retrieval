#Documentação oficial https://matplotlib.org/stable/users/index.html

from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import random
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 7]

x1 = [1, 3, 5, 7, 9]
y1 = [4, 8, 12, 14, 7]

x2 = [2, 4, 6, 8, 10]
y2 = [1, 6, 10, 14, 18]

#Título
# plt.title("Meu primeiro gráfico com python")

# #Eixos
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")

################## G R Á F I C O    DE    L I N H A S ##############################

# plt.plot(x,y, color="yellow", linestyle=":")#Cor através de input string
# plt.plot(x,y, color="#009900", linestyle=":") #Cor Hexadecimal

################## G R Á F I C O    DE    B A R R A S ##############################

# plt.bar(x,y)

# C O M P A R A N D O 
# plt.bar(x1,y1, label = "Grupo 1")
# plt.bar(x2,y2, label = "Grupo 2")
# plt.legend() #Legendas

################# G R Á F I C O    DE    P O N T O S    D I S P E R S O S (Scatterplot)##############################

# plt.scatter(x, y, label = "Meus Pontos", color = "R")#Pontos
# plt.legend() #Legendas


################# M A R C A D O R E S ##############################
 

# plt.scatter(x, y, label="Meus Pontos", color="red", marker="^", s=100)#Pontos | s = size | 
# plt.legend() #Legendas

# plt.show()


################# S A L V A N D O   O S     G R Á F I C O S     G E R A D O S ##############################
# plt.savefig("figura1.png", dpi=300)#dpi 300 é um tamanho padrão para impressão (quanto maior este valor, mais qualidade e maior o tamanho da imagem)
# plt.savefig("figura1.pdf")


################## I N T E R P R E T A N D O    C S V ########################################
# dados = open("populacao_brasileira.csv").readlines()

# a = []
# b = []

# for i in range(len(dados)):
#     if i != 0:
#         linha = dados[i].split(";")
#         a.append(int(linha[0]))
#         b.append(int(linha[1]))

# plt.plot(a,b)
# plt.title("Crescimento da População Brasileira 1980-2016")
# plt.xlabel("Ano")
# plt.ylabel("População x100.00.000")
# plt.show()

################## I N T E R P R E T A N D O    B O X P L O T ########################################
# Boxplot (diagrama de caixa) é uma técnica de visualização de dados em que representa a variação de dados por meio de quartis
# O retângulo central concentra 50% dos dados plotados. A linha ao centro indica a mediana.
# Os círculos representam os outlier (valores que destoam muito dos outros valores apresentados).


vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0,50)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
