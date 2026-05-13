while True:
    try:
        orcamento_disponivel = float(input("Digite o orçamento disponível em R$: "))

        destino = str(input("\nDigite o local (país/cidade) da viagem: "))

        custo_passagem = float(input("\nDigite o custo da passagem em R$: "))

        custo_diario_hospedagem = float(input("\nDigite o custo diário da hospedagem em EUR (Euros): "))

        qntd_dias = int(input("\nInforme a quantidade de dias da viagem: "))

    except ValueError:
        print(f"\nAlguma entrada está inválida!, tente novamente.\n")
        continue
