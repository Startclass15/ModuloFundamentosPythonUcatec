#CONCEPTOS BASICOS DE LIBRERIAS
#1. MODULOS 
#2. PAQUETES
#3. LIBRERIA (instalacion => terminal comandos (pip))

#Paquetes internos dentro de Python
#Paso 1. Importarlos (import )
import math
import os

print(math.sqrt(25))
print(math.pi)
print(math.e)
print(math.sin(45))
print(math.cos(45))
print(math.hypot(3,4))

print(os.listdir("."))
#os.mkdir("Prueba")
#os.rmdir("Prueba")
print(os.name)
print(os.cpu_count())

#APLICATIVA DEL MODULO OS 
#VARIABLES DE ENTRONO
print(os.environ)
#Crear una variable de entorno
os.environ["Google"]="1223151545451202"

print(os.environ.get("Google"))
print(os.environ.get("PATH"))

#import tkinter as tk

#boton=tk.Button()
#boton.unbind_class()

#import multiprocessing

#proceso=multiprocessing.Process()
#proceso.start()

import sqlite3


#Librerias externas (terceros)
#numpy, pandas, tensorflow, google

#Paso 1. Instalacion / terminal de comandos
# pip install numpy 
# pip install pandas
#Paso 2. Importar la libreria
import numpy as np
import pandas as pd

data=pd.DataFrame({
    "Nombre":["Kevin","Juan"],"Edad":[29,25]
})

print(data)

array=np.array([1,2,3,4])
print(array)

#Para actualizar librerias 
#pip install --upgrade numpy