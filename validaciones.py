from datetime import datetime

import datos

FORMATO_FECHA = "%d/%m/%Y"
FORMATO_FECHA_HORA = f"{FORMATO_FECHA} %H:%M"


def validar_nombre(nombre):
    longitud_minima = 3

    errores = []

    if len(nombre) < longitud_minima:
        errores.append(f"El nombre tiene que tener {longitud_minima} o más caracteres.")

    return errores


def validar_apellido(apellido):
    longitud_minima = 3

    errores = []

    if len(apellido) < longitud_minima:
        errores.append(f"El apellido tiene que tener {longitud_minima} o más caracteres.")

    return errores


def validar_telefono(telefono):
    longitud_esperada = 10  # para un número con código 11, son 11 + 8 caracteres
    prefijo_esperado = "11"

    errores = []

    if not telefono.isdigit():
        errores.append("El teléfono debe ser un valor numérico")

    if not len(telefono) == longitud_esperada:
        errores.append(f"El teléfono debe tener exactamente {longitud_esperada} caracteres de largo")

    if not telefono.startswith(prefijo_esperado):
        errores.append(f"El teléfono debe empezar con \"{prefijo_esperado}\"")

    return errores


def validar_fecha(fecha, formato=FORMATO_FECHA):
    errores = []

    try:
        datetime.strptime(fecha, formato)
    except ValueError:  # datetime.strptime intenta transformar la fecha y si falla tira el error ValueError
        errores.append("La fecha se encuentra en un formato inválido, debe ser en formato DD/MM/YYYY")

    return errores


def validar_fecha_nacimiento(fecha):
    edad_minima = 16  # años

    segundos_en_un_anio = 365.2425 * 24 * 60 * 60

    errores = validar_fecha(fecha)

    if len(errores) != 0:  # la fecha de por sí es inválida y no tiene sentido hacer el resto de verificaciones
        return errores

    # Tenemos cierta garantía de que esto no puede tirar ValueError por el chequeo que hace validar_fecha
    fecha_parseada = datetime.strptime(fecha, FORMATO_FECHA).date()

    diferencia = datetime.today().date() - fecha_parseada

    diferencia_anios = diferencia.total_seconds() / segundos_en_un_anio

    if diferencia_anios < edad_minima:
        errores.append(f"No se cumple la edad mínima de {edad_minima} años")

    return errores


def validar_fecha_nacimiento_mascota(fecha):
    errores = validar_fecha(fecha)

    if len(errores) != 0:
        return errores

    fecha_parseada = datetime.strptime(fecha, FORMATO_FECHA).date()

    if datetime.today().date() < fecha_parseada:
        errores.append("La fecha de nacimiento no puede estar en el futuro")

    return errores


# Validaciones básicas para un DNI
def validar_dni(dni):
    longitud_minima = 6
    longitud_maxima = 8

    errores = []

    if not dni.isdigit():
        errores.append("El DNI debe ser numérico")

    if not longitud_minima <= len(dni) <= longitud_maxima:
        errores.append(f"El DNI debe tener entre {longitud_minima} y {longitud_maxima} caracteres")

    return errores


# Valida que el DNI sea válido y que no haya un veterinario con el mismo DNI
def validar_dni_unico_veterinario(dni):
    errores = validar_dni(dni)

    # El DNI de por sí es inválido, no tiene sentido verificar que sea único
    if len(errores) != 0:
        return errores

    veterinarios = datos.obtener_veterinarios()

    for veterinario in veterinarios:
        if veterinario["dni"] == dni:
            nombre = veterinario["nombre"]
            apellido = veterinario["apellido"]

            errores.append(f"Ya existe un veterinario, {nombre} {apellido}, con ese DNI")

    return errores


# Lo mismo, validar que el DNI sea único entre los clientes
def validar_dni_unico_cliente(dni):
    errores = validar_dni(dni)

    if len(errores) != 0:
        return errores

    clientes = datos.obtener_clientes()

    for cliente in clientes:
        if cliente['dni'] == dni:
            nombre = cliente["nombre"]
            apellido = cliente["apellido"]

            errores.append(f"Ya existe un cliente, {nombre} {apellido}, con ese DNI")

    return errores


def validar_especialidad(especialidad):
    longitud_minima = 5

    errores = []

    if len(especialidad) < longitud_minima:
        errores.append(f"La especialidad debe tener al menos {longitud_minima} caracteres")

    return errores


def validar_dni_o_id_veterinario_existe(dni_o_id):
    errores = []

    if datos.buscar_veterinario_por_dni_o_id(dni_o_id) is None:
        errores.append("No se encontró un veterinario con ese DNI o ID")

    return errores


def validar_dni_o_id_cliente_existe(dni_o_id):
    errores = []

    if datos.buscar_cliente_por_dni_o_id(dni_o_id) is None:
        errores.append("No se encontró un cliente con ese DNI o ID")

    return errores


def validar_id_mascota_existe(id_mascota):
    mascotas = datos.obtener_mascotas()

    for mascota in mascotas:
        if mascota['id'] == id_mascota:
            return []

    return ["No se encontró una mascota con ese ID"]


def validar_id_turno_existe(id_turno):
    turnos = datos.obtener_turnos()

    for turno in turnos:
        if turno['id'] == id_turno:
            return []

    return ["No se encontró un turno con ese ID"]


def validar_raza(raza):
    longitud_minima = 3

    errores = []

    if len(raza) < longitud_minima:
        errores.append(f"La raza debe contener al menos {longitud_minima} caracteres")

    return errores


def validar_fecha_turno(fecha):
    errores = validar_fecha(fecha, formato=FORMATO_FECHA_HORA)

    if len(errores) != 0:
        return errores

    fecha_parseada = datetime.strptime(fecha, FORMATO_FECHA_HORA)

    if datetime.now() > fecha_parseada:
        errores.append("La fecha del turno debe estar en el futuro.")

    return errores


def validar_colisiones_turnos(turno_a_comprobar):
    distancia_minima_entre_turnos = 60 * 60  # 60 * 60 segundos = 1 hora
    distancia_minima_string = "1 hora"  # mensaje que se muestra en el error

    errores = validar_fecha(turno_a_comprobar['fecha'], FORMATO_FECHA_HORA)

    # No debería pasar, pero por las dudas es preferible devolver el error de fecha inválida y no una excepción
    if len(errores) != 0:
        return errores

    fecha_turno_a_comprobar = datetime.strptime(turno_a_comprobar['fecha'], FORMATO_FECHA_HORA)

    for turno in datos.obtener_turnos():
        # Solo nos interesa la colisión si los turnos comparten mascota o veterinario
        if (turno['id_mascota'] == turno_a_comprobar['id_mascota'] or
                turno['id_veterinario'] == turno_a_comprobar['id_veterinario']):
            fecha_turno_parseada = datetime.strptime(turno['fecha'], FORMATO_FECHA_HORA)
            distancia_horaria = (fecha_turno_parseada - fecha_turno_a_comprobar).total_seconds()

            if abs(distancia_horaria) < distancia_minima_entre_turnos:
                errores.append(
                    f"Debe haber al menos {distancia_minima_string} entre turnos, se encontró una colisión con el turno {turno['id']}, con fecha {turno['fecha']}")
    return errores


def validar_motivo_visita(motivo):
    longitud_minima = 5

    errores = []

    if len(motivo) < longitud_minima:
        errores.append(f"El motivo de la visita debe tener al menos {longitud_minima} caracteres")

    return errores
