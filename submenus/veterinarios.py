import datos
import impresiones
import utils
import validaciones


def mostrar_todos_los_veterinarios():
    veterinarios = datos.obtener_veterinarios()

    utils.imprimir_titulo(f"Mostrando {len(veterinarios)} veterinario(s)")

    for veterinario in veterinarios:
        impresiones.imprimir_veterinario_simple(veterinario)

def buscar_veterinario_por_dni():
    utils.imprimir_titulo("Buscar veterinario por DNI o ID")

    dni_o_id = utils.input_validado("DNI o ID del veterinario", validaciones.validar_dni_o_id_veterinario_existe,
                                    cancelable=True)

    if dni_o_id is None:
        print("* Búsqueda cancelada")
        return

    veterinario = datos.buscar_veterinario_por_dni_o_id(dni_o_id)

    impresiones.imprimir_veterinario_detallado(veterinario)


def crear_nuevo_veterinario():
    utils.imprimir_titulo("Crear un nuevo veterinario")

    formulario = [
        ("dni", "DNI", validaciones.validar_dni_unico_veterinario),
        ("nombre", "Nombre", validaciones.validar_nombre),
        ("apellido", "Apellido", validaciones.validar_apellido),
        ("teléfono", "Teléfono", validaciones.validar_telefono),
        ("fecha_nacimiento", "Fecha de nacimiento", validaciones.validar_fecha_nacimiento),
        ("especialidad", "Especialidad", validaciones.validar_especialidad)
    ]

    nuevo_veterinario = utils.crear_formulario(formulario)

    if nuevo_veterinario is None:
        print("* Creación cancelada")
        return

    veterinarios = datos.obtener_veterinarios()

    veterinarios.append(nuevo_veterinario)

    datos.guardar_veterinarios(veterinarios)

    print("* Nuevo veterinario creado")


def eliminar_veterinario():
    utils.imprimir_titulo("Eliminar un veterinario")

    dni_o_id = utils.input_validado("DNI o ID del veterinario", validaciones.validar_dni_o_id_veterinario_existe,
                                    cancelable=True)

    if dni_o_id is None:
        print("* Eliminación cancelada")
        return

    veterinario_a_eliminar = datos.buscar_veterinario_por_dni_o_id(dni_o_id)

    nombre = veterinario_a_eliminar['nombre']
    apellido = veterinario_a_eliminar['apellido']
    dni = veterinario_a_eliminar['dni']

    confirmacion = utils.solicitar_confirmacion(f"¿Seguro que desea eliminar a {nombre} {apellido} (DNI {dni})?")

    if not confirmacion:
        print("* Eliminación cancelada")
        return

    veterinarios = datos.obtener_veterinarios()

    veterinarios.remove(veterinario_a_eliminar)

    datos.guardar_veterinarios(veterinarios)

    print("* Veterinario eliminado")


def abrir_menu():
    opciones = [
        ("1", "Ver todos los veterinarios", mostrar_todos_los_veterinarios),
        ("2", "Buscar un veterinario por DNI", buscar_veterinario_por_dni),
        ("3", "Crear nuevo veterinario", crear_nuevo_veterinario),
        ("4", "Eliminar veterinario", eliminar_veterinario),
    ]

    utils.mostrar_menu("Menú principal » Veterinarios", "Veterinarios » ", opciones)
