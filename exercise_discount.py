def discount():
    precio = float(input())
    cantidad = int(input())

    subtotal = precio * cantidad

    if cantidad >= 10:
        porcentaje_desc = 20
    elif 5 <= cantidad <= 9:
        porcentaje_desc = 10
    else:
        porcentaje_desc = 0

    monto_desc = subtotal * (porcentaje_desc / 100)
    total_final = subtotal - monto_desc

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {porcentaje_desc}%")
    print(f"Monto de descuento: {monto_desc}")
    print(f"Total final: {total_final}")
