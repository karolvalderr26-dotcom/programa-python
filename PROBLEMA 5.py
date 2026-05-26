# ==========================================
# PROGRAMA: CONTROL DE HORAS SEMANALES
# ==========================================

# Matriz con los recursos y horas trabajadas
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Ana", 8, 8, 8, 8, 8],
    ["Carlos", 9, 9, 8, 9, 8],
    ["Luisa", 7, 8, 7, 8, 7],
    ["Pedro", 10, 9, 10, 9, 10]
]

# Función para calcular total y clasificación
def calcular_horas(recurso):

    nombre = recurso[0]

    # Suma de horas desde la posición 1
    total_horas = sum(recurso[1:])

    # Clasificación
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    # Retornar resultados
    return nombre, total_horas, clasificacion


# Mostrar resultados
print("===== REPORTE SEMANAL =====\n")

for recurso in recursos:

    nombre, total, estado = calcular_horas(recurso)

    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", estado)
    print("---------------------------")
    