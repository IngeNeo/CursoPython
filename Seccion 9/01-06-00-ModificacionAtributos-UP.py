class Persona:
	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

persona1 = Persona('Roger', 'Valencia', 28)
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1.nombre = 'Dylan Rios'
persona1.apellido = 'Garcia'
persona1.edad = 25
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Isabel', 'Miranda', 30)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
