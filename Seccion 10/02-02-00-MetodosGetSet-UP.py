class Persona:
	def __init__(self, nombre, apellido, edad):
		self._nombre = nombre
		self.apellido = apellido
		self.edad = edad

	@property
	def nombre(self):
		print('Llamando método get nombre')
		return self._nombre

	@nombre.setter
	def nombre(self, nombre):
		print('Llamando método set nombre')
		self._nombre = nombre

	def mostrar_detalle(self):
		print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Roger', 'Valencia', 28)
persona1.nombre = 'Alexis Garcia'
print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)