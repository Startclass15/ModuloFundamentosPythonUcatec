#1. Bucles Iterativos for
#for iterador in secuencia
#OJO: La secuencia puede ser (Rango, lista, tupla)
#Rango
#range(inicio,final,paso)
for iterador in range(1,31,2):
    print(iterador)

#EJericio mostar los numeros pares hasta el 100
for pares in range(2,101,2):
    print(pares)

for impares in range(101):
    print(impares)

#Recorrido por listas o tuplas
colores=("Rojo","Amarillo","Cafe","Azul","Verde")
for c in colores:
    print(c)

#Ejercicio Propuesto:
#Mostrar la tabla de multiplicar de cualquier numero ingresado por teclado FOR
#Salida: 1x5=5
#        2x5=10

tablaN=int(input("Ingrese el numero de la tabla que desesa ver. "))
for tabla in range(1,11,1):
    print(f"{tabla}x{tablaN}={tabla*tablaN}")

#2. Bucles Condicionados while
# sintaxis
# while condicion:
#    instruccion
#1. Contador (incremento), 2. Condicional,  3.Salida

contador=1
while contador<=100:
    print(contador)
    contador +=1

#Pares 
par=2

while par<=100:
    print(par)
    par+=2


