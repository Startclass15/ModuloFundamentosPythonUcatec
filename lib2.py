#Graficas de barras
import matplotlib.pyplot as plt

#Prueba
categorias=["A","B","C","D","E","F"]
ganancias=[50,150,20,70,550,12]


plt.bar(categorias,ganancias,color="orange")
plt.title("Pyplot")
plt.xlabel("Eje de categorias")
plt.ylabel("Eje Ganancia")

plt.show()
 