class Persona:
	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def mostrar_detalle(self):
		print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Roger', 'Valencia', 28)
persona1.mostrar_detalle()

persona2 = Persona('Isabel', 'Miranda', 30)
persona2.mostrar_detalle()