import datos
import impresiones
import submenus.turnos
import utils
import validaciones


def mostrar_todas_las_mascotas():
    mascotas = datos.obtener_mascotas()

    utils.imprimir_titulo(f"Mostrando {len(mascotas)} mascota(s)")

    for mascota in mascotas:
        impresiones.imprimir_mascota_simple(mascota)


def mostrar_opciones_mascota(mascota):
    def crear_turno():
        submenus.turnos.crear_nuevo_turno(mascota)

    def eliminar():
        eliminar_mascota(mascota)

    opciones = [
        ("1", "Asignar un turno", crear_turno),
        ("2", "Eliminar", eliminar)
    ]

    utils.mostrar_menu(f"Opciones para {mascota['nombre']}", f"{mascota['nombre']} » ", opciones)


def mostrar_mascotas_de_cliente(cliente=None):
    if cliente is None:
        dni_o_id = utils.input_validado("DNI o ID del cliente", validaciones.validar_dni_o_id_cliente_existe,
                                        cancelable=True)

        if dni_o_id is None:
            print("* Búsqueda cancelada")
            return

        cliente = datos.buscar_cliente_por_dni_o_id(dni_o_id)

    mascotas = datos.buscar_mascotas_de_cliente(cliente)

    opciones = []

    for indice, mascota in enumerate(mascotas):
        def mostrar_opciones():
            mostrar_opciones_mascota(mascota)

        tecla = str(indice + 1)
        nombre = f"{mascota['nombre']} de raza {mascota['raza']} nacido el {mascota['fecha_nacimiento']}"
        opciones.append((tecla, nombre, mostrar_opciones))

    utils.mostrar_menu(f"Mostrando {len(mascotas)} mascota(s) de {cliente['nombre']}",
                       f"Seleccionar una mascota de {cliente['nombre']} » ", opciones)


def crear_nueva_mascota(cliente_duenio=None):
    utils.imprimir_titulo("Crear una mascota")

    if cliente_duenio is None:
        dni_o_id = utils.input_validado("DNI o ID del cliente dueño", validaciones.validar_dni_o_id_cliente_existe,
                                        cancelable=True)

        if dni_o_id is None:
            print("* Búsqueda cancelada")
            return

        cliente_duenio = datos.buscar_cliente_por_dni_o_id(dni_o_id)

    formulario = [
        ("nombre", "Nombre", validaciones.validar_nombre),
        ("raza", "Raza", validaciones.validar_raza),
        ("fecha_nacimiento", "Fecha de nacimiento", validaciones.validar_fecha_nacimiento_mascota)
    ]

    nueva_mascota = utils.crear_formulario(formulario)

    if nueva_mascota is None:
        print("* Creación cancelada")
        return

    nueva_mascota['id_dueño'] = cliente_duenio['id']

    mascotas = datos.obtener_mascotas()

    mascotas.append(nueva_mascota)

    datos.guardar_mascotas(mascotas)

    print(
        f"* Nueva mascota creada para {cliente_duenio['nombre']} {cliente_duenio['apellido']} (DNI {cliente_duenio['dni']})")


def eliminar_mascota(mascota_a_eliminar):
    nombre = mascota_a_eliminar['nombre']
    raza = mascota_a_eliminar['raza']
    fecha_nacimiento = mascota_a_eliminar['fecha_nacimiento']

    utils.imprimir_titulo(f"Eliminar a {mascota_a_eliminar['nombre']}")

    confirmacion = utils.solicitar_confirmacion(
        f"¿Seguro que desea eliminar a {nombre}, de raza {raza} nacido el {fecha_nacimiento}?")

    if not confirmacion:
        print("* Eliminación cancelada")
        return

    mascotas = datos.obtener_mascotas()

    mascotas.remove(mascota_a_eliminar)

    datos.guardar_mascotas(mascotas)

    print("* Mascota eliminada")


def abrir_menu():
    opciones = [
        ("1", "Ver todas las mascotas", mostrar_todas_las_mascotas),
        ("2", "Administrar las mascotas de un cliente", mostrar_mascotas_de_cliente),
        ("3", "Crear nueva mascota", crear_nueva_mascota)]

    utils.mostrar_menu("Menú principal » Mascotas", "Mascotas » ", opciones)
