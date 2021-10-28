class Persona:
	def __init__(self, nombre, apellido, edad):
		self._nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def mostrar_detalle(self):
		print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Roger', 'Valencia', 28)
persona1._nombre = 'Alexis Garcia'
persona1.mostrar_detalle()
