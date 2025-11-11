import datos
import impresiones
import submenus.mascotas
import utils
import validaciones


def mostrar_todos_los_clientes():
    clientes = datos.obtener_clientes()

    utils.imprimir_titulo(f"Mostrando {len(clientes)} cliente(s)")

    for cliente in clientes:
        impresiones.imprimir_cliente_simple(cliente)


def buscar_cliente_por_dni():
    utils.imprimir_titulo("Buscar cliente por DNI o ID")

    dni_o_id = utils.input_validado("DNI o ID del cliente", validaciones.validar_dni_o_id_cliente_existe,
                                    cancelable=True)

    if dni_o_id is None:
        print("* Búsqueda cancelada")
        return

    cliente = datos.buscar_cliente_por_dni_o_id(dni_o_id)

    utils.imprimir_titulo(f"Datos de {cliente['nombre']} {cliente['apellido']}")

    impresiones.imprimir_cliente_detallado(cliente)

    mascotas = datos.buscar_mascotas_de_cliente(cliente)

    print()
    if len(mascotas) == 0:
        print("Sin mascotas asociadas.")
    else:
        print(f"{len(mascotas)} mascota(s) asociadas:")

        for mascota in mascotas:
            impresiones.imprimir_mascota_simple(mascota)

    def agregar_mascota_a_cliente():
        submenus.mascotas.crear_nueva_mascota(cliente)

    def administrar_mascotas():
        submenus.mascotas.mostrar_mascotas_de_cliente(cliente)

    def eliminar():
        eliminar_cliente(cliente)

    opciones = [
        ("1", f"Registrar una nueva mascota a nombre de {cliente['nombre']}", agregar_mascota_a_cliente),
        ("2", f"Administrar las mascotas de {cliente['nombre']}", administrar_mascotas),
        ("3", f"Eliminar a {cliente['nombre']}", eliminar)
    ]

    utils.mostrar_menu(f"Opciones para {cliente['nombre']}", f"{cliente['nombre']} » ", opciones)


def crear_nuevo_cliente():
    utils.imprimir_titulo("Crear un nuevo cliente")

    formulario = [
        ("dni", "DNI", validaciones.validar_dni_unico_cliente),
        ("nombre", "Nombre", validaciones.validar_nombre),
        ("apellido", "Apellido", validaciones.validar_apellido),
        ("teléfono", "Teléfono", validaciones.validar_telefono),
        ("fecha_nacimiento", "Fecha de nacimiento", validaciones.validar_fecha_nacimiento),
    ]

    nuevo_cliente = utils.crear_formulario(formulario)

    if nuevo_cliente is None:
        print("* Creación cancelada")
        return

    clientes = datos.obtener_clientes()

    clientes.append(nuevo_cliente)

    datos.guardar_clientes(clientes)

    print("* Nuevo cliente creado")


def eliminar_cliente(cliente_a_eliminar=None):
    utils.imprimir_titulo("Eliminar un cliente")

    if cliente_a_eliminar is None:
        dni_o_id = utils.input_validado("DNI o ID del cliente", validaciones.validar_dni_o_id_cliente_existe,
                                        cancelable=True)

        if dni_o_id is None:
            print("* Eliminación cancelada")
            return

        cliente_a_eliminar = datos.buscar_cliente_por_dni_o_id(dni_o_id)

    nombre = cliente_a_eliminar['nombre']
    apellido = cliente_a_eliminar['apellido']
    dni = cliente_a_eliminar['dni']

    confirmacion = utils.solicitar_confirmacion(f"¿Seguro que desea eliminar a {nombre} {apellido} (DNI {dni})?")

    if not confirmacion:
        print("* Eliminación cancelada")
        return

    mascotas_cliente = datos.buscar_mascotas_de_cliente(cliente_a_eliminar)

    if len(mascotas_cliente) > 0:
        print(
            f"ADVERTENCIA: {nombre} {apellido} tiene {len(mascotas_cliente)} mascota(s) asociada(s) y van a ser eliminadas del sistema:")

        for mascota in mascotas_cliente:
            impresiones.imprimir_mascota_simple(mascota)

        confirmacion_mascotas = utils.solicitar_confirmacion(f"¿Eliminar también {len(mascotas_cliente)} mascota(s)?")

        if not confirmacion_mascotas:
            print("* Eliminación cancelada")
            return

        mascotas = datos.obtener_mascotas()

        for mascota_cliente in mascotas_cliente:
            mascotas.remove(mascota_cliente)

        datos.guardar_mascotas(mascotas)
        print(f"* {len(mascotas_cliente)} mascota(s) eliminada(s)")

    clientes = datos.obtener_clientes()

    clientes.remove(cliente_a_eliminar)

    datos.guardar_clientes(clientes)

    print("* Cliente eliminado")


def abrir_menu():
    opciones = [
        ("1", "Ver todos los clientes", mostrar_todos_los_clientes),
        ("2", "Buscar un cliente por DNI", buscar_cliente_por_dni),
        ("3", "Crear nuevo cliente", crear_nuevo_cliente),
        ("4", "Eliminar cliente", eliminar_cliente),
    ]

    utils.mostrar_menu("Menú principal » Clientes", "Clientes » ", opciones)
