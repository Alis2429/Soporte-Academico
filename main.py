print("===================================")
print("   SISTEMA DE SOPORTE ACADÉMICO")
print("===================================")


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar solicitud")
    print("2. Salir")


def validar_texto(texto):
    return texto.strip() != ""


def validar_codigo(codigo):
    return validar_texto(codigo) and len(codigo) >= 5


def validar_tipo_consulta(tipo):
    tipos_validos = [
        "matrícula",
        "pagos",
        "constancia",
        "plataforma",
        "otro"
    ]
    return tipo.lower() in tipos_validos


def asignar_prioridad(tipo_consulta):
    if tipo_consulta.lower() in ["matrícula", "pagos"]:
        return "Alta"
    elif tipo_consulta.lower() in ["constancia", "plataforma"]:
        return "Media"
    else:
        return "Baja"


def registrar_solicitud(codigo, nombre, tipo_consulta, descripcion):
    prioridad = asignar_prioridad(tipo_consulta)

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion,
        "prioridad": prioridad
    }

    return solicitud


def mostrar_resumen(solicitud):
    print("\n--- RESUMEN DE SOLICITUD ---")
    print("Código:", solicitud["codigo"])
    print("Nombre:", solicitud["nombre"])
    print("Tipo de consulta:", solicitud["tipo_consulta"])
    print("Descripción:", solicitud["descripcion"])
    print("Prioridad:", solicitud["prioridad"])


solicitud = registrar_solicitud(
    "N00543943",
    "Alisson",
    "matrícula",
    "Consulta sobre inscripción de cursos"
)

mostrar_resumen(solicitud)