#Introduccion a Python
#Tipos de datos 
#1. Tipos de datos Simples (Numericos, cadenas de caracteres, logicos)
nombre="Kevin Arroyo Montaño"
precio=150.50
encender=True
#2. Tipos de datos Complejos
#2.1. Listas (Cojunto de datos - mutables) sintaxis= []
colores=["Rojo","Verde","Azul","Cafe","Rosado"]
numeros=[334,45,69,1,22.5,354,10]
lista=["A",15,True]
#Escritura de datos print()
#2.1.1. Operaciones de las listas
#2.1.1.1. Acceso a los elementos de una lista
print(colores[0]) #El primer elemento de una lista [0]
print(colores[2])
print(colores[-1]) #El ultimo elemento de una lista [-1]
#2.1.1.2. Modificacion de datos de una lista
colores[1]="Lila"
print(colores)
colores[-1]="Celeste"
print(colores)
#2.1.1.3. Agregado de datos a una lista
#2.1.1.3.1. Agregado al final de la lista (append)
colores.append("Blanco")
print(colores)
#2.1.1.3.2. Insertar un elemento en una posicion especifia (insert)
colores.insert(1,"Negro")
print(colores)
#2.1.1.3.3. Agregar varios elementos en la lista (extend)
colores.extend(["Anaranjado","Amarillo","Plomo","Amarillo"])
print(colores)
#2.1.1.4. Eliminacion de elementos en una lista
#2.1.1.4.1. Eliminacion del primer elemento que coincida con el valor ingresado (remove)
colores.remove("Amarillo")
print(colores)
#2.1.1.4.2. Eliminacion de un elemento en una posicion especifica (pop)
colores.pop()
print(colores)
#2.1.1.4.3. Eliminacion por id en rango definidos del
del colores[0:2]
print(colores)
#2.1.1.4.4. Eliminacion de todos los elementos de la lista (clear)
colores.clear()
print(colores)
#2.1.1.4.5. Longitud de una lista len()
print(len(numeros))
print(len(colores))
#2.2. Tuplas conjunto de elementos - inmutables ()
codigos=(4534,4889,122,15156,63123)
print(codigos)

#2.3. Diccionarios (Conjunto de datos almacenados con pares de clave:valor) {}
usuarios={
    "nombre":"Kevin",
    "contraseña":1454512,
    "estado":True
}

#2.3.1. Obtencio de los valores  (clave)
print(usuarios["nombre"])
print(usuarios["nombre"], "Contraseña: ", usuarios["contraseña"])
#2.3.2. Agregadado de elementos
usuarios["nombre"]="Juan"
print(usuarios["nombre"])
#2.3.3. Actualizacion de datos
usuarios.update(
    {
        "celular":65402398,
        "correo":"abc@gmail.com"
    }
)
print(usuarios["celular"])
print(usuarios)
#2.3.3. Eliminacion de elementos pop
valor=usuarios.pop("estado")
print(valor)
print(usuarios)
#valor2=usuarios.pop("edad")
#print(valor2)
del usuarios["celular"]
print(usuarios)
#Eliminacion de todos los elmentos el diccionario clear()
usuarios.clear()
print(usuarios)

#2.4. DICCIONARIOS ANIDADOS
baseDatos={
    "usuarios":[
        {
            "id":1,
            "nombre":"Kevin",
            "contraseña":45415121
        },
        {
            "id":2,
            "nombre":"Juan",
            "contraseña":1215842
        },
        {
            "id":3,
            "nombre":"Ana",
            "contraseña":9815842
        }

    ],
    "productos":[
        {
            "idProducto":1,
            "nombreProducto":"producto1",
            "precio":150
        },
         {
            "idProducto":2,
            "nombreProducto":"producto2",
            "precio":600
        },
        {
            "idProducto":2,
            "nombreProducto":"producto3",
            "precio":850
        }

    ]
}

print(baseDatos["productos"][-1])