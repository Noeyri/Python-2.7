#

print("Ingrese el consumo a pagar:")
consumo = int(raw_input())

descuento = 0

if(consumo >= 500):
    print("Total de pagar:")
    descuento = consumo * 0.1

    print(consumo - descuento)

else:
    print("Total a pagar:")
    print(consumo)