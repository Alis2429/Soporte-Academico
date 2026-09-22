print("Sistema de Soporte Académico")

def registrar_solicitud(codigo, nombre, tipo_consulta, descripcion):
    return {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }


def validar_codigo(codigo):
    return codigo.strip() != "" and len(codigo) >= 5


solicitud = registrar_solicitud(
    "N00543943",
    "Alisson",
    "matrícula",
    "Consulta sobre inscripción de cursos"
)

print("\n--- Validación del código ---")
print("Código:", solicitud["codigo"])
print("Código válido:", validar_codigo(solicitud["codigo"]))