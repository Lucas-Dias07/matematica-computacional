print("=== ROBÔ BARISTA ===")

tipo_cafe = input("Digite o tipo de café (puro/expresso): ").lower()
acucar = input("Deseja açúcar? (sim/nao): ").lower()
leite = input("Deseja leite? (sim/nao): ").lower()

agua = int(input("Quantidade de água disponível (ml): "))
quantidade_leite = int(input("Quantidade de leite disponível (ml): "))

# Verificação do tipo de café
if tipo_cafe != "puro" and tipo_cafe != "expresso":
    print("Tipo de café inválido.")

else:
    # Verificação da água
    if agua <= 0:
        print("Erro: reservatório de água vazio.")

    # Verificação do leite
    elif leite == "sim" and quantidade_leite <= 0:
        print("Erro: reservatório de leite vazio.")

    else:
        print("\nPreparando o café...")

        print("1. Colocando água.")
        print("2. Preparando o", tipo_cafe + ".")

        if leite == "sim":
            print("3. Adicionando leite.")

        if acucar == "sim":
            print("4. Adicionando açúcar.")

        print("5. Café pronto!")
        print("6. Entregando o café na mesa.")
