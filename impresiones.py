# Utilidades para imprimir distintos tipos de datos
import datos

# Impresión detallada: todos los campos, uno por línea
# Impresión simple: pocos campos, todos en una línea

DEFINICIONES_CLAVES = {
    "apellido": "Apellido",
    "asistencia": "asistencia",
    "disponibilidad": "Disponibilidad",
    "dni": "DNI",
    "especialidad": "Especialidad",
    "fecha": "Fecha",
    "id": "ID",
    "id_dueño": "ID del dueño",
    "id_mascota": "ID de la mascota",
    "id_veterinario": "ID del veterinario",
    "motivo_visita": "Motivo de la visita",
    "nombre": "Nombre",
    "raza": "Raza",
    "teléfono": "Teléfono",
}


# Imprime las claves de un diccionario si están presentes en la lista de definiciones, opcionalmente tomando una lista con el orden deseado
def imprimir_claves(diccionario, definiciones, orden_claves=None):
    claves = diccionario.keys if (orden_claves is None) else orden_claves

    for clave in claves:
        if clave in definiciones:
            nombre_clave = definiciones[clave]
            print(f"{nombre_clave}: {diccionario[clave]}")


def imprimir_cliente_detallado(cliente):
    imprimir_claves(cliente, DEFINICIONES_CLAVES, datos.CLAVES_CLIENTE)


def imprimir_mascota_detallado(mascota):
    imprimir_claves(mascota, DEFINICIONES_CLAVES, datos.CLAVES_MASCOTA)


def imprimir_turno_detallado(turno):
    imprimir_claves(turno, DEFINICIONES_CLAVES, datos.CLAVES_TURNO)


def imprimir_veterinario_detallado(veterinario):
    imprimir_claves(veterinario, DEFINICIONES_CLAVES, datos.CLAVES_VETERINARIO)


def imprimir_cliente_simple(cliente):
    dni = cliente['dni']
    nombre = cliente['nombre']
    apellido = cliente['apellido']
    telefono = cliente['teléfono']

    print(f"* {apellido}, {nombre} (DNI {dni}) - {telefono}")


def imprimir_mascota_simple(mascota):
    nombre = mascota['nombre']
    raza = mascota['raza']
    fecha_nacimiento = mascota['fecha_nacimiento']

    print(f"\t* {nombre}, de raza {raza}, nació el {fecha_nacimiento}")


def imprimir_turno_simple(turno):
    fecha = turno['fecha']
    motivo_visita = turno['motivo_visita']
    print(f"* Turno el {fecha} con motivo \"{motivo_visita}\"")


def imprimir_veterinario_simple(veterinario):
    dni = veterinario['dni']
    nombre = veterinario['nombre']
    apellido = veterinario['apellido']
    especialidad = veterinario['especialidad']
    telefono = veterinario['teléfono']

    print(f"* {apellido}, {nombre} (DNI {dni}) - especialidad: {especialidad} - {telefono}")
