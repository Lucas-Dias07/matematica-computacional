com_conexao = bool(int(input("Está conectado à internet? (1 = Sim / 0 = Não): ")))

if not com_conexao:
    print("Modo Offline ativado. Executando músicas baixadas.")
