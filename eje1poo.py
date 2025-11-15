#crear la clase animal
class Animal:
    def __init__(self,especie,color, tamaño):
        self.especie=especie
        self.color=color
        self.tamaño=tamaño

    def dormir(self):
        print("Esta durmiendo....")
    def comer(self,comida):
        print(f"Esta comiendo {comida}")
    def hacerSonido(self):
        print("Esta haciendo sonido")

gato=Animal("Gato","Cafe","Pequeño")
jirafa=Animal("Jirafa","Amarillo con cafe","Grande")
pez=Animal("Acuatico","rojo","Pequeño")

gato.dormir()
jirafa.hacerSonido()
pez.hacerSonido()

#Subclase AnimalesDomesticos

#Paso 1. Definir la subclase(Clase)
class AninalDomestico(Animal):
    #Paso 2. definir el contructor
    def __init__(self,especie,color,tamaño,nombre,vacunas,dueño):
        #Paso 3. Heredar atributos de la clase padre super()
        super().__init__(especie,color,tamaño)
        self.nombre=nombre
        self.vacunas=vacunas
        self.dueño=dueño
    #Paso 4. Definir las acciones de la subclase
    def obedecer(self):
        print(f"{self.nombre} esta obedeciendo a su dueño {self.dueño}")
    def dormir(self):
        print(f"El {self.especie} esta durmiendo en su cama")
 


#Paso 5. Objetos de la subclase
perro=AninalDomestico("Perro","Cafe","Mediano","Scott","Completas","Kevin Arroyo")
perro.dormir()
perro.obedecer()
perro.comer("Balanceado")
gato=AninalDomestico("Gato","Blanco","Pequeño","kitty","Completas","Juan")
gato.dormir()
gato.hacerSonido()
gato.obedecer()


#Ej 1. Realizar la clase padre Persona (nombre, edad, ci)
#crear la subclase estudiante(materia, codEstudiante, carrera)
#crear la subclase docente(profesion,codDocente,carrera)
#aplicando herencia y polimorfismo




