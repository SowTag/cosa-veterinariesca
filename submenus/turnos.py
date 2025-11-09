import datos
import impresiones
import utils
from datetime import datetime

import validaciones


# Otra idea:
# Mostrar opciones de "ver turnos de hoy, ver turnos para esta semana"
# Mostrar todos los turnos ordenados, permitir seleccionar un turno y cambiar asistencia, disponibilidad, etc.

def buscar_turno_por_id():
    id_turno = utils.input_validado("ID del turno a buscar", validaciones.validar_id_turno_existe, cancelable=True)

    if id_turno is None:
        print("* Búsqueda cancelada")
        return

    turno = datos.buscar_turno_por_id(id_turno)

    impresiones.imprimir_turno_detallado(turno)

# sorted() necesita una propiedad del turno para comparar, en este caso va a ser la fecha
def ordenar_turnos(turno_a_ordenar):
    return datetime.strptime(turno_a_ordenar['fecha'], validaciones.FORMATO_FECHA_HORA)

def mostrar_todos_los_turnos():
    # Ordenar los turnos por fecha (de anterior a posterior)
    turnos_ordenados = sorted(
        datos.obtener_turnos(),
        key=ordenar_turnos
    )

    utils.imprimir_titulo(f"Mostrando {len(turnos_ordenados)} turno(s)")

    for turno in turnos_ordenados:
        impresiones.imprimir_turno_simple(turno)


def crear_nuevo_turno(mascota=None):
    utils.imprimir_titulo("Creación de turno: Detalles del paciente y veterinario")
    if mascota is None:
        print(
            "* Tip: Una forma más sencilla de asignar un turno es en Mascotas > Administrar las mascotas de un cliente")
        id_mascota = utils.input_validado("ID de la mascota", validaciones.validar_id_mascota_existe, cancelable=True)

        if id_mascota is None:
            print("* Búsqueda cancelada")
            return

        mascota = datos.buscar_mascota_por_id(id_mascota)


    dni_o_id_veterinario = utils.input_validado("DNI o ID del veterinario",
                                                validaciones.validar_dni_o_id_veterinario_existe,
                                                cancelable=True)
    if dni_o_id_veterinario is None:
        print("* Creación de turno cancelada")
        return

    veterinario = datos.buscar_veterinario_por_dni_o_id(dni_o_id_veterinario)

    formulario = [
        ("fecha", "Fecha", validaciones.validar_fecha_turno),
        ("motivo_visita", "Motivo de la visita", validaciones.validar_motivo_visita),
    ]

    utils.imprimir_titulo(f"Creación de turno: {mascota['nombre']} con {veterinario['nombre']} {veterinario['apellido']} (DNI {veterinario['dni']})")
    turno = utils.crear_formulario(formulario)


    if turno is None:
        print("* Creación de turno cancelada")
        return

    turno['id_mascota'] = mascota['id']
    turno['id_veterinario'] = veterinario['id']

    turnos = datos.obtener_turnos()

    turnos.append(turno)

    datos.guardar_turnos(turnos)

    print(f"* Turno guardado para el {turno['fecha']}")


def cancelar_turno():
    id_turno = utils.input_validado("ID del turno a buscar", validaciones.validar_id_turno_existe, cancelable=True)

    if id_turno is None:
        print("* Eliminación cancelada")
        return

    turno = datos.buscar_turno_por_id(id_turno)

    turnos = datos.obtener_turnos()

    turnos.remove(turno)

    datos.guardar_turnos(turnos)

    print("* Turno eliminado")



def abrir_menu():
    opciones = [
        ("1", "Buscar un turno específico por ID", buscar_turno_por_id),
        ("2", "Ver todos los turnos ordenados", mostrar_todos_los_turnos),
        ("3", "Crear nuevo turno", crear_nuevo_turno),
        ("4", "Eliminar un turno", cancelar_turno)
    ]

    utils.mostrar_menu("Menú principal » Turnos", "Turnos » ", opciones)
