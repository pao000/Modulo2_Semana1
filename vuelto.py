vuelto = 512
billetes_monedas = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
vuelto_restante = vuelto
respuesta = {}

for billete_moneda in billetes_monedas:
    cantidad = vuelto_restante // billete_moneda
    if cantidad > 0:
        respuesta[billete_moneda] = cantidad
        vuelto_restante -= cantidad * billete_moneda

print(respuesta)
