print("=== CALCULADORA DE PONTUAÇÃO ===")

presenca = float(input("Digite a pontuação de Presença (0 a 100): "))
posicionamento = float(input("Digite a pontuação de Posicionamento (0 a 100): "))
ponto_extra = float(input("Digite a pontuação de Ponto Extra (0 a 100): "))

if 0 <= presenca <= 100 and 0 <= posicionamento <= 100 and 0 <= ponto_extra <= 100:
    print("Pontuações cadastradas com sucesso!")

    media = (presenca + posicionamento + ponto_extra) / 3

    print(f"Média final: {media:.2f}")
else:
    print("Erro: todas as pontuações devem estar entre 0 e 100.")
