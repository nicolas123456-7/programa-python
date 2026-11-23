def calcular_y_clasificar_jornada(horas_dias):
    total_horas = 0
    for horas in horas_dias:
        total_horas = total_horas + horas
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"
    return total_horas, clasificacion
# Matriz con 4 recursos: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
registro_horas = [
    ["Ana", 8, 8, 8, 8, 8],
    ["Carlos", 9, 8, 9, 8, 8],
    ["Luisa", 7, 8, 8, 7, 6],
    ["Mateo", 10, 9, 8, 8, 7],
]
print("=== REPORTE SEMANAL DE JORNADA LABORAL ===")
for fila in registro_horas:
    nombre = fila[0]
    horas_lunes_a_viernes = [fila[1], fila[2], fila[3], fila[4], fila[5]]
    total, jornada = calcular_y_clasificar_jornada(horas_lunes_a_viernes)
    print(f"Recurso: {nombre} | Total horas: {total} | Jornada: {jornada}")