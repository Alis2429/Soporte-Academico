print("Sistema de Soporte Académico")


def registrar_solicitud(codigo, nombre, tipo_consulta, descripcion):
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }
    return solicitud


def validar_codigo(codigo):
    return codigo.strip() != "" and len(codigo) >= 5


def validar_tipo_consulta(tipo):
    tipos_validos = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    return tipo.lower() in tipos_validos


solicitud = registrar_solicitud(
    "N00543943",
    "Alisson",
    "matrícula",
    "Consulta sobre inscripción de cursos"
)

print("\n--- Validaciones ---")
print("Código válido:", validar_codigo(solicitud["codigo"]))
print("Tipo válido:", validar_tipo_consulta(solicitud["tipo_consulta"]))