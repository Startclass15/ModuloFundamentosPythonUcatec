#PARADIGMA ORIENTADO A OBJETOS
# CLASE (PERSONA)
# PROPIEDADES (nombre,edad,ci)
# ACCIONES (Dormir, Comer)

#PASO 1. DEFINIR LA CLASE (class Nombreclase)
class Persona:
    #Paso 2. DEFINIR EL CONTRUCTOR DE LA CLASE (funcion)
    def __init__(self,nombre,edad,ci):
        #Almacenar los atributos
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    #Paso 3. DEFINIR LAS ACCIONES DE LA CLASE - METODOS def ()
    def dormir(self):
        print(f"{self.nombre} Esta durmiendo...")
    def comer(self,comida):
        print(f"{self.nombre} Esta comiendo {comida}")

#Paso 4. crear los objets de la clase
persona1=Persona("Kevin Arroyo",29,7444412)
persona2=Persona("Juan Perez",25,4451542)
persona3=Persona("Ana",25,85541212)

persona1.dormir()
persona2.comer("Pan")
persona3.comer("Carne")
