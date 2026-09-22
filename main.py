print("Sistema de Soporte Académico")


def validar_texto(texto):
    return texto.strip() != ""


texto = "Consulta sobre pagos"

print("\n--- Validación de texto ---")
print("Texto:", texto)
print("Texto válido:", validar_texto(texto))