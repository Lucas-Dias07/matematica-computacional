eh_noite = bool(int(input("É noite? (1 = Sim / 0 = Não): ")))
farol_ligado = bool(int(input("O farol está ligado? (1 = Sim / 0 = Não): ")))

if eh_noite and not farol_ligado:
    print("Atenção: Acenda os faróis para sua segurança!")
