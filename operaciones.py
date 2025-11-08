#1.Operaciones Aritmeticas + - * / // % **
numero1=15
numero2=7
#Suma, resta, multiplicacion, division
sumar=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
print(f"Suma: {sumar} - Resta: {resta} - Multiplicacion: {multiplicacion} - Division: {division}")

#Division entera //
divisionEntera=numero1//numero2
print(divisionEntera)
#Modulo %
modulo=numero1%numero2
print(modulo)
#Exponente **
potencia=numero1**numero2
print(potencia)

#2. Operadores de asignacion 
#Igualdad asigna un valor a una variables
x=18
#suma += , -=, *=, /=
x+=2
print(x)

#3. Operadores de comparacion
a=16
b=18
#Igualdad ==
print(a==b)
#Distinto que !=
print(a!=b)
#Mayor que >
print(a>b)
#Menor que <
print(a<b)
#Mayor o igual >=
print(a>=b)
#Meno o Igual <=
print(a<=b)

#4. Operadores Logicos (condicionales/bucles)
edad=21
licenciaConducir=True
#y and
edad>=18 and licenciaConducir
#o or
#no not

#5. Operadores a nivel BITS
#& AND BIT A BIT 
#| OR BIT A BIT
#^ XOR BIT A BIT
#~ NOT BIT A BIT
#<< Desplazamiento a la izquierda
#>> Desplazamiento a la derecha
print(bin(5))
print(bin(3))
a=5
b=3
print(a&b)