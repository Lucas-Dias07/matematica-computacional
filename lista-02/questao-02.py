botao = input("O botão de pedestres foi apertado? (sim/nao): ").lower()

if botao == "nao":
    print("Nenhum pedestre solicitou a travessia.")
    print("O semáforo continua funcionando normalmente.")

else:
    tempo_verde_pedestre = int(
        input("Há quantos segundos o sinal de pedestres ficou verde? ")
    )

    tempo_espera_carros = int(
        input("Há quantos segundos os carros estão com o sinal verde? ")
    )

    if tempo_verde_pedestre < 5:
        print("Aguarde. O sinal de pedestres ficou verde há menos de 5 segundos.")

    elif tempo_espera_carros < 10:
        print("Aguarde. É necessário garantir um tempo mínimo para os carros.")

    else:
        print("Atenção: o sinal dos carros ficará vermelho.")
        print("Som de aviso para os pedestres.")
        print("Sinal dos carros: VERMELHO")
        print("Sinal dos pedestres: VERDE")
        print("Pedestres podem atravessar.")
