import utils
from submenus import clientes, mascotas, veterinarios, turnos


opciones = [
    ("1", "Clientes", clientes.abrir_menu),
    ("2", "Mascotas", mascotas.abrir_menu),
    ("3", "Turnos", turnos.abrir_menu),
    ("4", "Veterinarios", veterinarios.abrir_menu),
]

utils.mostrar_menu("Menú principal", "Menú principal » ", opciones)