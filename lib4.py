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
dis =ax.scatter(x,y)
ax.set_xlim(0,200)
ax.set_ylim(0,10)

for iterador in range(200):
    x.append(iterador)
    y.append(random.randint(0,10))

    dis.set_offsets(list(zip(x,y)))


    #Autonomia en el escalado
    ax.relim()
    ax.autoscale_view()
    figura.canvas.draw()
    figura.canvas.flush_events()

    time.sleep(0.2)

plt.ioff()
plt.show()
