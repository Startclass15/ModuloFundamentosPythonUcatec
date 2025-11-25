#1. Cargado de datos (datasets, pandas)
#2. Separacion de datos
#3. Preprocesamiento
#4. Creacion de un modelo
#5. Entrenamiento del modelo
#6. Probar el Modelo
#7. Evaluar el Modelo (Metricas)

#Ejer 1. Crear un modelo que realice predicciones para partidos del mundial
#Empate - Ganar - Perder
#A=Bolivia
#B=Otro Equipo
#Etiquetado(0=EMPATE - 1=BOLIVIA GANA - 2=BOLIVIA PIERDE)
#Variables( )
#Bolivia - OTRO equipo
#0-0   = 0
#0-2   = 2
#2-0   = 1
#0-3   = 2 
#1-0   = 1
#1-0   = 1
#0-3   = 2
#0-2   = 2
#0-3   = 2

#Paso 1. Importar las librerias
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Paso 2.  Cargar los datos
partidos=[
    [0,0],
    [0,2],
    [2,0],
    [0,3],
    [1,0],
    [1,0],
    [0,3],
    [0,2],
    [0,3]
]
etiquetas=[0,2,1,2,1,1,2,2,2]


#Paso Extra 1. Separacion de datos
pEntrenamieto,pTesteo,eEntrenamiento, eTesteo=train_test_split(partidos,etiquetas,test_size=0.2, random_state=42)




#Paso 3. Creacion de un Modelo
modelo=DecisionTreeClassifier()

#Paso 4. Entrenar el modelo (fit)
modelo.fit(pEntrenamieto,eEntrenamiento)



#Paso Extra 2. Dibujar el arbol de desiciones
plt.figure(figsize=(12,8))
plot_tree(
    modelo,
    feature_names=['Goles Bolivia','Goles Rival'],
    class_names=["Empate","Ganar","Perder"],
    filled=True,
    fontsize=14
)

plt.show()



#Paso 5. Prueba del modelo (prediccion) (predict)
#Simulacion de Boliva 4 - Peru 1
prediccion=modelo.predict(pTesteo)
print(prediccion)
#mETRICAS DE COMPORTAMIENTO DEL MODELO
print("Resultado Probabilidades")
print(accuracy_score(eTesteo,prediccion))

print("Mariz de confusion")
print(confusion_matrix(eTesteo,prediccion))

print("Reporte prediccion")
print(classification_report(eTesteo,prediccion))

print("Bolivia ",prediccion)
#0 Empatado 1 Ganado 2 Perdido

#Paso 6. Evaluacion del Modelo
partido1=[[3,1]]
print("Prediccion partido 1. ",modelo.predict(partido1))

partido2=[[0,0]]
print("Prediccion partido 2. ",modelo.predict(partido2))

partido3=[[0,4]]
print("Prediccion partido 3. ",modelo.predict(partido3))





