aceitou_termos = bool(int(input("Aceitou os termos? (1 = Sim / 0 = Não): ")))

if not aceitou_termos:
    print("Acesso negado. Você precisa aceitar os termos de serviço para jogar.")
