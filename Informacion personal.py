#Diccionario
informacion_personal = {
'nombre':'Maria Gabriela Sosa Moreira',
'edad':22,
'ciudad':'Quito',
'provincia':'Pichincha',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Quito'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Estudiante de universidad'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0985151696'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)