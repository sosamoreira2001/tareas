# 1. Escritura de Archivo de Texto:
# Crear un nuevo archivo llamado my_notes.txt y escribir al menos tres líneas de notas personales en el archivo.

with open("my_notes.txt", "w") as file:
    file.write("1. Recordar comprar los pañales en el supermercado.\n")
    file.write("2. Llamar a toda la familia para una comida.\n")
    file.write("3. Preparar la presentación para mañana la clase.\n")

# 2. Lectura de Archivo de Texto:
# Abrir el archivo my_notes.txt, leer el contenido del archivo línea por línea y mostrar cada línea leída en la consola.

with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() elimina el carácter de nueva línea al final de cada línea

# 3. Cierre de Archivos:
# Cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
# No es necesario cerrar explícitamente el archivo cuando se usa la estructura "with open()".

# El archivo se cierra automáticamente al salir del bloque "with".