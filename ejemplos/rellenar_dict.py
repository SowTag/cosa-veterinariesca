from datos import rellenar_dict

# Ejemplo de rellenar_dict


# Supongamos que un cliente puede tener nombre, apellido y DNI, pero por algún motivo solo tenemos los primeros dos:

cliente = {
    "nombre": "Rosa",
    "apellido": "Melano",
}

print(cliente)

# Si ahora quiero acceder al DNI,
try:
    print(f"DNI: {cliente['dni']}")
except KeyError:
    print("ERROR! La clave cliente['dni'] no existe entonces Python tira una excepción")

# En cambio, si antes uso rellenar_dict:

cliente2 = rellenar_dict(cliente, ['nombre', 'apellido', 'dni'])

# rellenar_dict va a ver que el cliente tenga todas las claves, y definir las que no tenga:
print(cliente2)

# Compará el primer print con el segundo, pasamos de:
# {'nombre': 'Rosa', 'apellido': 'Melano'}
# a:
# {'nombre': 'Rosa', 'apellido': 'Melano', 'dni': None}

# Entonces, ahora intentar acceder al DNI no va a tirar una excepción, sino simplemente devolver None:
print(f"DNI: {cliente2['dni']}")