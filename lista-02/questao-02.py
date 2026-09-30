valor_compra = 17
valor_pago = 100

troco = valor_pago - valor_compra

print("Valor da compra: R$", valor_compra)
print("Valor pago: R$", valor_pago)
print("Troco: R$", troco)

valores = [50, 20, 10, 5, 2, 1]

print("\nNotas e moedas para o troco:")

for valor in valores:
    quantidade = troco // valor

    if quantidade > 0:
        print(f"{quantidade} de R$ {valor}")
        troco = troco % valor
