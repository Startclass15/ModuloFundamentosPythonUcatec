#Tipos de graficas
#1. Diagramas 
# 1. Diagramas de caja (boxplot)
import matplotlib.pyplot as plt
import numpy as np

#Diagrama de violin (violinplot)
data=np.random.randn(100)

plt.violinplot(data)
plt.show()



