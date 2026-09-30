valor_compra = 17
valor_pago = 100

troco = valor_pago - valor_compra

print("Troco:", troco)

notas = [50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = troco // nota

    if quantidade > 0:
        print(f"{quantidade} nota(s)/moeda(s) de R$ {nota}")
        troco = troco % nota
