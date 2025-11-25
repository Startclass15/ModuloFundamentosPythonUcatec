#Paso 1. Importacion de dependencias
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#Paso 2. Traer los datos de procesamiento
data=load_iris()
x=data.data
y=data.target

#Paso 3. Separacion de datos para entrenamiento y testeo
x_Entrenamiento, x_Testeo, y_Entrenamiento, y_Testeo=train_test_split(x,y,test_size=0.20)

#Paso 4. Crear el modelo
modelo=Sequential([
    Dense(16, activation="relu", input_shape=(4,)),
    Dense(8, activation="relu"),
    Dense(3,activation="softmax")
])

#Paso 5. Compilar el modelo
modelo.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=['accuracy']
)

#Paso 6. Entrenamiento del modelo
entrenamiento=modelo.fit(
    x_Entrenamiento,y_Entrenamiento,
    epochs=50,
    batch_size=16,
    validation_split=0.20
)

#Analizar el modelo
perdidad,salida=modelo.evaluate(x_Testeo,y_Testeo)
print(f"Precision del testeo fue de: {perdidad} - {salida}")

modelo.predict()