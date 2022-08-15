
from cProfile import label
import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 7]

x1 = [1, 3, 5, 7, 9]
y1 = [4, 8, 12, 14, 7]

x2 = [2, 4, 6, 8, 10]
y2 = [1, 6, 10, 14, 18]

#Título
plt.title("Meu primeiro gráfico com python")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

################## G R Á F I C O    DE    L I N H A S ##############################

plt.plot(x,y)

################## G R Á F I C O    DE    B A R R A S ##############################

# plt.bar(x,y)

# C O M P A R A N D O 
# plt.bar(x1,y1, label = "Grupo 1")
# plt.bar(x2,y2, label = "Grupo 2")
# plt.legend() #Legendas

################# G R Á F I C O    DE    P O N T O S    D I S P E R S O S ##############################

plt.scatter(x, y, label = "Meus Pontos", color = "R")#Pontos
plt.legend() #Legendas


################# G R Á F I C O    DE    B A R R A S ##############################
 

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
plt.show()