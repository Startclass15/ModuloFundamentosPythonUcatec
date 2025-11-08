#Condicionales 
#if condicion:
#   bloque de codigo verdadero
#else:
#   bloque de codigo falso

edad=12
if edad>=18:
    print("Es mayor de edad...")
else:
    print("Es menor de edad...")

#2. Condicionales Multiples (if - elif - else)
#if condicion1:
    #Bloque de codigo verdadero
#elif condicion2:
    #Bloque de codigo falso para la condicion1 y verdadero para condicion2
#elif condicion 3:
    #Bloque codigo 
#elif condicion 4:
    #Bloque codigo
#else:
#   #Bloque de codigo 

nota=90
if nota>=90:
    print("Excelente")
elif nota>=80:
    print("Muy Bien")
elif nota>=70:
    print("Bien")
else:
    print("Regular")

#Aplicando operadores logicos and or
edad=21
licenciaConducir=False
#y and
if edad>=18 and licenciaConducir:
    print("Es mayor de edad y puede manejar el auto")
else:
    print("No puede manejar")

#Condicionales Anidados
#if condicion
#   if condicion
#Ejercicio votacion
edadP=int(input("Ingrese su edad: "))
ci=input("Tiene su carnet de identidad (si/no)")
if edadP>=18:
    if ci=="si":
        print("Puede realizar su voto")
    else: 
        print("Necesita su ci para votar")
else:
    print("Aun no puede votar es menor de edad...")

#Entradas de datos input() "Obtiene los datos en string"
#Para obtener datos numericos de un input debemos convertirlo
# int o float
