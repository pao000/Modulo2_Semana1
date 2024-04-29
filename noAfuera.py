presentismo = 80  # Porcentaje de asistencia
total_clases = 40  # Total de clases
tiene_justificativo = True  # True si tiene justificativo, False si no tiene

if (presentismo / total_clases) >= 0.75 or tiene_justificativo:
    print("Puede rendir")
else:
    print("No puede rendir")
