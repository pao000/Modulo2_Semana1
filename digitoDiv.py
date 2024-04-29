numero = int(input("Ingresa un número: "))
ultimo_digito = abs(numero) % 10  # Obtiene el último dígito del número
if ultimo_digito % 3 == 0:
    print(f"El último dígito de {numero} es {ultimo_digito} y es divisible por 3.")
else:
    print(f"El último dígito de {numero} es {ultimo_digito} y no es divisible por 3.")
