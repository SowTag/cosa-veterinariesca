import utils

# Confirmación en "sí" por defecto
c = utils.solicitar_confirmacion("¿Confirmás?", por_defecto=True)

print(f"Confirmado: {c}")

# Confirmación en "no" por defecto
c = utils.solicitar_confirmacion("¿Confirmás?", por_defecto=False)

print(f"Confirmado: {c}")
