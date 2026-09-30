esta_chovendo = input("Está chovendo agora? (sim/nao): ").lower()

chance_chuva = int(
    input("Qual a chance de chuva segundo a previsão? (0 a 100): ")
)

ceu = input("Como está o céu? (limpo/nublado/escuro): ").lower()

transporte = input(
    "Qual será o meio de transporte? (a_pe/onibus/carro): "
).lower()

if esta_chovendo == "sim":
    levar_guarda_chuva = True

elif chance_chuva > 60 and transporte == "a_pe":
    levar_guarda_chuva = True

elif ceu == "escuro" and chance_chuva >= 40:
    levar_guarda_chuva = True

else:
    levar_guarda_chuva = False

if levar_guarda_chuva:
    print("Leve o guarda-chuva!")

else:
    print("Não é necessário levar o guarda-chuva.")
