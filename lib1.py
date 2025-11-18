#Paso 1. Importar la libreria
import matplotlib.pyplot as plt

#Paso 2. Configurar la grafica (plot)
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,5,4,1,8,5,6,7,11,3]

#plt.plot(x,y,color="red", linestyle="--", linewidth=2)
#Escalas de dispersion (scatter())
plt.scatter(x,y, color="green")

#Personalizar la graficas
plt.title("Grafica Prueba")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

#Paso 3. Mostrar la figura (show())
plt.show()

