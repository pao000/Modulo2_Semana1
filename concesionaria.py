# Datos proporcionados
total_autos = 537
autos_negros = 227
autos_blancos = 168
autos_rojos = 56

# Calcular el número de autos blancos y rojos
print("Autos blancos vendidos:", autos_blancos)
print("Autos rojos vendidos:", autos_rojos)

# Forma 1: Calcular el número de autos no negros restando los autos negros del total
autos_no_negros = total_autos - autos_negros
print("Forma 1 - Autos no negros:", autos_no_negros)

# Forma 2: Sumar los autos de otros colores al total de autos no negros
otros_colores = 49 + 37
autos_no_negros_2 = total_autos - autos_negros + otros_colores
print("Forma 2 - Autos no negros:", autos_no_negros_2)

# Calcular porcentaje de vehículos vendidos por color
porcentaje_negros = (autos_negros / total_autos) * 100
porcentaje_blancos = (autos_blancos / total_autos) * 100
porcentaje_rojos = (autos_rojos / total_autos) * 100
porcentaje_grises = (49 / total_autos) * 100
porcentaje_otros = (37 / total_autos) * 100

# Imprimir resultados
print("Porcentaje de vehículos vendidos por color:")
print("Negros:", porcentaje_negros, "%")
print("Blancos:", porcentaje_blancos, "%")
print("Rojos:", porcentaje_rojos, "%")
print("Grises:", porcentaje_grises, "%")
print("Otros:", porcentaje_otros, "%")

# Promedio de autos vendidos por día
promedio_autos_dia = total_autos / 365
print("Promedio de autos vendidos por día:", promedio_autos_dia)
