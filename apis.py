#API (Conjunto de reglas para realizar la comunicacion entre dos sistemas)
#Librerias peticiones requests
import requests
#Paso 1. Instalar la libreria de Google
#Libreria Google (Servicios Google Cloud)
#pip install google-generativeai
#Paso 2. Importar la libreria
import google.generativeai as genai

apiGoogleCloud=""
#Paso 3.Configurar la api Key
genai.configure(api_key=apiGoogleCloud)

#Paso 4. Configurar un Modelo 
modelo=genai.GenerativeModel(model_name="gemini-2.5-flash-lite-preview-09-2025")

#Paso 5. Probar el Modelo
pregunta=input("Ingresa tu pregunta? ")
respuesta=modelo.generate_content(pregunta)
print(respuesta.text)


respuestaImagen=genai.generate_image(
    prompt=pregunta,
    model="imagen-4.0-generate-001"
    )

#Guardado de la imagen 
for iterador, img in enumerate(respuestaImagen.images):
    with open(f"imagenGenerada_{iterador}.png","wb") as imagen:
        imagen.write(img.image_bytes)


