class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def desplegar(self):
		print(f'Nombre: {self.nombre}, Edad: {self.edad}')


persona1 = Persona('Roger', 28)
persona1.desplegar()
persona2 = Persona('Isabel', 21)
persona2.desplegar()
