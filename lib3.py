#Funcionamiento de graficas dinamincas

#Paso 1. Importar las animaciones
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import numpy as np
import time
#Libreria local
import random

#Activacioon del modo interactivo
plt.ion()

x=[]
y=[]

#Paso 2. Configuracion en tiempo real
figura,ax=plt.subplots()
line, =ax.plot(x,y)

for iterador in range(200):
    x.append(iterador)
    y.append(random.random()*10)

    line.set_xdata(x)
    line.set_ydata(y)


    #Autonomia en el escalado
    ax.relim()
    ax.autoscale()
    figura.canvas.draw()
    figura.canvas.flush_events()

    time.sleep(0.1)

plt.ioff()
plt.show()
