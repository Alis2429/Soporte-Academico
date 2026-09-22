print("Sistema de Soporte Académico")


def registrar_solicitud(codigo, nombre, tipo_consulta, descripcion):
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }
    return solicitud


solicitud = registrar_solicitud(
    "N00543943",
    "Alisson",
    "matrícula",
    "Consulta sobre inscripción de cursos"
)

print("\n--- Solicitud registrada ---")
print("Código:", solicitud["codigo"])
print("Nombre:", solicitud["nombre"])
print("Tipo:", solicitud["tipo_consulta"])
print("Descripción:", solicitud["descripcion"])