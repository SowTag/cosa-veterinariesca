import time

import utils


def opcion1():
    print("Esto es lo que está en la opción 1.")


def opcion2():
    print("Esto es lo que está en la opción 2. Contemos hasta 3:")

    for i in range(3):
        print(i + 1)
        time.sleep(1)


def opcion3():
    print(
        "Esta es la opción 3, dentro del submenú (date cuenta que no se vuelve al menú principal sino al mismo submenú).")


def submenu():
    opciones_submenu = [
        ("1", "Opción 3", opcion3)
    ]

    utils.mostrar_menu("Menú » Submenú", "Menú » Submenú: ", opciones_submenu)


opciones = [
    ("1", "Opción 1", opcion1),
    ("2", "Opción 2 (incluye delay de 3 seg)", opcion2),
    ("3", "Submenú (abre un submenú)", submenu)
]

utils.mostrar_menu("Menú principal", "Principal » ", opciones)
