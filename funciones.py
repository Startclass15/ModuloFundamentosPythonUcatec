#Una funcion es un bloque de codigo reutilizable
#sintaxis def
# def nombrefuncion(parametros):
#    #bloque de codigo
#     #return   

#Tipos de funciones
#1. Funciones sin parametros
def bienvenida():
    print("Hola bienvenido....")

bienvenida()
bienvenida()
bienvenida()
bienvenida()

#2. Funciones con parametros
#fUNCION CON PARAMETROS PERO SIN FUNCION DE RETORNO
def bienvenida2(nombre):
    print(f"Hola bienvenido {nombre}...")

bienvenida2("Kevin")
bienvenida2("Juan")
bienvenida2("Ana")
#FUNCiON CON PARAMETROS CON FUNCION DE RETORNO
def sumar(x,y):
    resultado=x+y
    return resultado

print(sumar(78,8))

#Funciones con multiples parametros y multiples retornos
def operacionesAritmeticas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return suma,resta,multiplicacion,division #Convertir en una tupla

s,r,m,d=operacionesAritmeticas(25,9)
print("Suma es: ",s)
print("Resta es: ",r)
print("Multiplicacion es: ",m)
print("Division es: ",d)
