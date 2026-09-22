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

def registrar_y_mostrar(codigo, nombre, tipo, descripcion):
    if not validar_codigo(codigo):
        print("Error: código inválido.")
        return

    if not validar_texto(nombre):
        print("Error: nombre vacío.")
        return

    if not validar_tipo_consulta(tipo):
        print("Error: tipo de consulta inválido.")
        return

    if not validar_texto(descripcion):
        print("Error: descripción vacía.")
        return

    solicitud = registrar_solicitud(
        codigo,
        nombre,
        tipo,
        descripcion
    )

    mostrar_resumen(solicitud)

solicitudes = [
    ("N00543943", "Alisson", "matrícula", "Consulta sobre inscripción"),
    ("B67890", "Luis", "pagos", "Consulta sobre pago de matrícula"),
    ("C54321", "María", "otro", "Consulta general")
]


print("\n===================================")
print("       REGISTRO DE SOLICITUDES")
print("===================================")

for solicitud in solicitudes:
    registrar_y_mostrar(
        solicitud[0],
        solicitud[1],
        solicitud[2],
        solicitud[3]
    )