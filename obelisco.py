altura_obelisco = 67.5  # Altura en metros
grosor_billete = 0.00011  # Grosor en metros
altura_pila = 1 * grosor_billete  # Altura inicial de la pila de billetes

dias = 0
while altura_pila <= altura_obelisco:
    altura_pila *= 2  # Duplica la altura de la pila
    dias += 1

print(f"La pila de billetes supera la altura del obelisco después de {dias} días.")
