class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# Crear objeto persona
persona1= Persona("Brenes", 39)
persona1.saludar()

esposa= Persona("Daniela", 36)
esposa.saludar()

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} esta estudiando el grado {self.grado}.")

estudiante1= Estudiante("Byron", 29, "Maestria")
estudiante1.saludar()
estudiante1.estudiar()