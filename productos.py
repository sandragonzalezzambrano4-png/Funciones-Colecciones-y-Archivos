# Programa para registrar estudiantes

estudiantes = []

# Agregar nombres a la lista
estudiantes.append("Sandra")
estudiantes.append("Johana")
estudiantes.append("Edgar")

# Mostrar los estudiantes registrados
print("Estudiantes registrados:")

for estudiante in estudiantes:
    print(estudiante)

# Buscar un estudiante
nombre = input("Ingrese el nombre que desea buscar: ")

if nombre in estudiantes:
    print("El estudiante está registrado.")
else:
    print("El estudiante no está registrado.")