# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = (monto_total * porcentaje_descuento) / 100
    # Calcula el monto final después del descuento
    monto_final = monto_total - descuento
    # Devuelve el monto del descuento
    return descuento, monto_final

# Llamada a la función con solo el monto total de la compra
monto_total1 = 100
descuento1, monto_final1 = calcular_descuento(monto_total1)
print(f"Descuento aplicado: {descuento1} dolares")
print(f"Monto final a pagar: {monto_final1} dolares")

# Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
monto_total2 = 120  # monto varible
porcentaje_descuento2 = 20  # descuento variable
descuento2, monto_final2 = calcular_descuento(monto_total2, porcentaje_descuento2)
print(f"Descuento aplicado: {descuento2} pesos")
print(f"Monto final a pagar: {monto_final2} pesos")
