import json
import os

# Las claves que se usan en el JSON. Por ejemplo,
# {
#     "mensajes": []
# }
# "mensajes" es la clave.
COLECCION_CLIENTES = "clientes"
COLECCION_MASCOTAS = "mascotas"
COLECCION_TURNOS = "turnos"
COLECCION_VETERINARIOS = "veterinarios"

# Las claves que tiene que tener cada tipo de dato, si un dato no
# lo tiene entonces se lo agrega con el valor None para evitar KeyError.
# Véase ejemplos/rellenar_dict.py
CLAVES_CLIENTE = ["id", "dni", "nombre", "apellido", "teléfono", "fecha_nacimiento"]
CLAVES_MASCOTA = ["id", "id_dueño", "nombre", "raza", "fecha_nacimiento"]
CLAVES_TURNO = ["id", "fecha", "motivo_visita", "id_veterinario", "id_mascota", "disponibilidad", "asistencia"]
CLAVES_VETERINARIO = ["id", "dni", "nombre", "apellido", "teléfono", "fecha_nacimiento", "especialidad"]

# Ruta en donde se guarda el JSON.
RUTA_JSON = "datos.json"


def cargar_json():
    asegurar_archivo_json_existe()

    with open(RUTA_JSON, "r") as f:  # r = read (lectura)
        return json.load(f)


# Simplemente, crea un archivo vacío en RUTA_JSON si no existe
def asegurar_archivo_json_existe():
    if not os.path.exists(RUTA_JSON):
        guardar_json({})


def guardar_json(datos):
    with open(RUTA_JSON, "w", encoding="utf-8") as f:  # w = write (escritura)
        json.dump(datos, f, indent=4,
                  ensure_ascii=False)  # indent=4 hace que el JSON tenga un formato que lo hace más legible

    # encoding="utf-8" y ensure_ascii=False hacen que se puedan guardar acentos y Ñ al JSON


def rellenar_dict(dic, claves):
    for clave in claves:
        if clave not in dic:  # si la clave no existe en el diccionario, establecerla en None
            dic[clave] = None

    return dic


def obtener_coleccion(clave_coleccion):
    data = cargar_json()

    if clave_coleccion in data:
        return data[clave_coleccion]
    else:
        return []


def guardar_coleccion(clave, coleccion):
    data = cargar_json()

    data[clave] = coleccion

    guardar_json(data)


def obtener_turnos():
    # El código de abajo (el return) es lo mismo que esto:

    # turnos = obtener_coleccion(CLAVE_PRINCIPAL_TURNOS)
    # turnos_rellenos = []
    # for turno in turnos:
    #     turnos_rellenos.append(rellenar_dict(turno, CLAVES_TURNOS))
    #
    # return turnos_rellenos

    # Esencialmente, dice "ejecutar rellenar_dict para cada turno en la colección de turnos"
    return [rellenar_dict(turno, CLAVES_TURNO) for turno in obtener_coleccion(COLECCION_TURNOS)]


def obtener_clientes():
    return [rellenar_dict(cliente, CLAVES_CLIENTE) for cliente in obtener_coleccion(COLECCION_CLIENTES)]


def obtener_mascotas():
    return [rellenar_dict(mascota, CLAVES_MASCOTA) for mascota in obtener_coleccion(COLECCION_MASCOTAS)]


def obtener_veterinarios():
    return [rellenar_dict(veterinario, CLAVES_VETERINARIO) for veterinario in obtener_coleccion(COLECCION_VETERINARIOS)]


def guardar_clientes(clientes):
    guardar_coleccion(COLECCION_CLIENTES, clientes)


def guardar_mascotas(pacientes):
    guardar_coleccion(COLECCION_MASCOTAS, pacientes)


def guardar_turnos(turnos):
    guardar_coleccion(COLECCION_TURNOS, turnos)


def guardar_veterinarios(veterinarios):
    guardar_coleccion(COLECCION_VETERINARIOS, veterinarios)


def buscar_veterinario_por_dni_o_id(dni_o_id):
    for veterinario in obtener_veterinarios():
        if veterinario['id'] == dni_o_id or veterinario['dni'] == dni_o_id:
            return veterinario

    return None


def buscar_cliente_por_dni_o_id(dni_o_id):
    for cliente in obtener_clientes():
        if cliente['id'] == dni_o_id or cliente['dni'] == dni_o_id:
            return cliente

    return None


def buscar_cliente_duenio_de_mascota(mascota):
    for cliente in obtener_clientes():
        if mascota['id_dueño'] == cliente['id']:
            return cliente

    return None


def buscar_mascotas_de_cliente(cliente):
    mascotas = []

    for mascota in obtener_mascotas():
        if mascota['id_dueño'] == cliente['id']:
            mascotas.append(mascota)

    return mascotas


def buscar_mascota_por_id(id_mascota):
    for mascota in obtener_mascotas():
        if mascota['id'] == id_mascota:
            return mascota
    return None


def buscar_turno_por_id(id_turno):
    for turno in obtener_turnos():
        if turno['id'] == id_turno:
            return turno
    return None
