andar_atual = int(input("Em qual andar o elevador está? (1 a 10): "))

if andar_atual < 1 or andar_atual > 10:
    print("Andar inválido.")

else:
    quantidade_pedidos = int(input("Quantos pedidos existem? "))

    pedidos_subir = []
    pedidos_descer = []

    for i in range(quantidade_pedidos):
        andar = int(input(f"Digite o andar do pedido {i + 1}: "))

        if andar < 1 or andar > 10:
            print("Andar inválido. Pedido ignorado.")

        else:
            direcao = input(
                "A pessoa deseja subir ou descer? "
            ).lower()

            if direcao == "subir":
                pedidos_subir.append(andar)

            elif direcao == "descer":
                pedidos_descer.append(andar)

            else:
                print("Direção inválida. Pedido ignorado.")

    print("\n=== PEDIDOS RECEBIDOS ===")
    print("Pedidos para subir:", pedidos_subir)
    print("Pedidos para descer:", pedidos_descer)

    # Verifica primeiro os pedidos que estão na direção do elevador
    if pedidos_subir:
        pedidos_subir.sort()

        print("\nAtendendo pedidos para subir:")

        for andar in pedidos_subir:
            if andar >= andar_atual:
                print("Elevador parando no andar", andar)

        andar_atual = pedidos_subir[-1]

    if pedidos_descer:
        pedidos_descer.sort(reverse=True)

        print("\nAtendendo pedidos para descer:")

        for andar in pedidos_descer:
            if andar <= andar_atual:
                print("Elevador parando no andar", andar)

        andar_atual = pedidos_descer[-1]

    print("\nElevador terminou os pedidos.")
    print("Andar atual:", andar_atual)
