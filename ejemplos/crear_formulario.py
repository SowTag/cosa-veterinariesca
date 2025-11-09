import utils


# Supongamos que tenemos estas dos funciones validadoras:
def validar_nombre(nombre):
    errores = []

    if len(nombre) < 3:
        errores.append("El nombre tiene que tener 3 o más caracteres")

    if not nombre.isalpha():
        errores.append("El nombre solo puede contener letras")

    return errores


def validar_numero(numero):
    errores = []

    if len(numero) != 3:
        errores.append("El número tiene que tener 3 caracteres exactos")

    if not numero.isdigit():
        errores.append("El número tiene que contener solo caracteres numéricos")

    return errores


# Ahora, puedo generar un diccionario con un formulario:

formulario = [
    ("nombre", "Nombre de 3 o más caracteres", validar_nombre),
    ("numero", "Número de 3 caracteres exactos", validar_numero)
]

diccionario = utils.crear_formulario(formulario)

if diccionario is None:
    print("Se canceló la creación del diccionario")
else:
    print(f"Diccionario creado: {diccionario}")