import uuid


# Imprime un título de ancho fijo alineado en consola.
def imprimir_titulo(titulo):
    ancho_maximo = 80
    separador = "—"
    espacios = 3

    espacio_disponible = ancho_maximo - len(titulo)

    ancho_por_lado = (espacio_disponible // 2) - espacios

    separador_por_lado = separador * (ancho_por_lado + 1)
    espacios_por_lado = " " * espacios

    titulo = separador_por_lado + espacios_por_lado + titulo + espacios_por_lado + separador_por_lado

    print(titulo[:ancho_maximo])


# Abre un input que toma una función validadora y no continúa hasta que el valor ingresado sea válido o se cancele el input
# prompt: el mensaje que va a mostrar el input()
# validador: una función que valide el input, debe retornar un array de errores (en strings)
# cancelable: si el input es cancelable, en cuyo caso presionar Enter va a cancelar el input y hacer que esta función retorne None
def input_validado(prompt, validador, cancelable=False):
    primer_intento = True

    respuesta = ""
    errores = []

    if cancelable:
        prompt = f"{prompt} [Enter para cancelar]"

    prompt = f"{prompt} » "

    while len(errores) != 0 or primer_intento:
        primer_intento = False

        respuesta = input(prompt)

        errores = validador(respuesta)

        if len(respuesta) == 0 and cancelable:
            errores = []
        else:
            for error in errores:
                print(f"* {error}")

    # Si la longitud de la respuesta es cero y el input es cancelable, devolver None (input cancelado)
    return None if cancelable and len(respuesta) == 0 else respuesta


# Muestra un menú navegable por CLI
# titulo: un título a mostrar
# mensaje_entrada: el mensaje que va a tener el input()
# opciones: un array de tuplas (<tecla>, <nombre>, <función>)
#       <tecla>: la tecla que el usuario debe presionar para activar esa función
#       <nombre>: el nombre que se le da a la función
#       <función>: la función que se ejecuta al elegir esa opción
# * Véase ejemplos/mostrar_menu.py
def mostrar_menu(titulo, mensaje_entrada, opciones):
    volver = False

    while not volver:
        imprimir_titulo(titulo)
        print()

        for opcion in opciones:
            tecla = opcion[0]
            nombre = opcion[1]

            print(f"\t{tecla}. {nombre}")

        print("\t0. ↩ Salir")
        print()

        seleccionado = input(mensaje_entrada)
        print()

        for opcion in opciones:
            tecla = opcion[0]
            funcion = opcion[2]

            if tecla == seleccionado:
                funcion()

        if seleccionado == "0":
            volver = True


# Genera un ID único en un string
def generar_id_unico():
    # uuid.uuid4() genera un ID de 128 bits, osea uno en 2^128 = 340282366920938463463374607431768211456
    # esto hace que sea poco factible tener colisiones (generar dos ID iguales) y es lo que se usa comúnmente en entornos
    # de producción.
    return str(uuid.uuid4())  # uuid = Universally Unique ID (identificador universalmente único)


# Crea un formulario que pide varios campos y retorna el diccionario con los mismos rellenos, permite cancelación en cuyo
# caso se retorna None.
# formulario: un array de claves, nombres y funciones de validación a rellenar
# agregar_id: si se debe agregar una clave 'id' con un ID autogenerado al objeto devuelto
# * Véase ejemplos/crear_formulario.py
def crear_formulario(formulario, agregar_id=True):
    diccionario = {}

    for campo in formulario:
        clave = campo[0]
        prompt = campo[1]
        validador = campo[2]

        respuesta = input_validado(prompt, validador, cancelable=True)

        if respuesta is None:  # se canceló el input
            return None  # cancelar el form entero, esto se maneja en la función externa

        diccionario[clave] = respuesta

    if agregar_id:
        diccionario['id'] = generar_id_unico()

    return diccionario


# Muestra un mensaje pidiendo confirmación al usuario.
# mensaje: el mensaje que se va a mostrar
# por_defecto: la opción por defecto, si el usuario presiona Enter
# * Véase ejemplos/solicitar_confirmacion.py
def solicitar_confirmacion(mensaje, por_defecto=False):
    respuesta_positiva = "s"  # sí
    respuesta_negativa = "n"  # no

    letra_positiva = respuesta_positiva.upper() if por_defecto else respuesta_positiva.lower()
    letra_negativa = respuesta_negativa.upper() if not por_defecto else respuesta_negativa.lower()

    sugerencia_respuestas = f"[{letra_positiva}/{letra_negativa}]"

    respuesta = ""

    while respuesta not in [respuesta_positiva, respuesta_negativa]:
        respuesta = input(f"{mensaje} {sugerencia_respuestas} ").lower()

        if len(respuesta) == 0:
            return por_defecto

    return respuesta == respuesta_positiva.lower()
