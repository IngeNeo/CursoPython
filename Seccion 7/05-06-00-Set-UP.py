# set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
# revisar si un elemento está presente
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print(planetas)
#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
# eliminar elemento sin arrojar error
planetas.discard('Júpiters')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar el set
del planetas
print(planetas)