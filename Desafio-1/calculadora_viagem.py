#Valor da cotação do euro-real
cotacao_euro = 6.10


#"Loop" das entradas
#Se alguma entrada estiver inválida ou com valor númerico negativo encerra o programa imediatamente.

while True:
    try:
        orcamento_disponivel = float(input("Digite o orçamento disponível em R$: "))

        destino = str(input("\nDigite o local (país/cidade) da viagem: "))

        custo_passagem = float(input("\nDigite o custo da passagem em R$: "))

        custo_diario_hospedagem = float(input("\nDigite o custo diário da hospedagem em EUR (Euros): "))

        qntd_dias = int(input("\nInforme a quantidade de dias da viagem: "))

        if orcamento_disponivel < 0 or custo_passagem < 0 or custo_diario_hospedagem < 0 or qntd_dias < 0:
            print("Valores negativos são inválidos!")
            exit()

        break

    except ValueError:
        print("\nEntrada inválida!")
        exit()

#Custo da diária em real
custo_diario_real = custo_diario_hospedagem * cotacao_euro

#Custo da hospedagem, de x dias, temos y de custo.
calc_hospedagem = qntd_dias * custo_diario_real

#Custo total da viagem
custo_total = custo_passagem + calc_hospedagem

#Orçamento possível, calculado se custo total é menor ou igual ao orçamento disponível
orcamento_possivel = custo_total <= orcamento_disponivel

#Status da viagem, se é viável ou não
status_viagem = orcamento_possivel and qntd_dias > 0

#Quanto faltará ou sobrará para alcançar o objetivo da viagem
objetivo = orcamento_disponivel - custo_total


#Exibição final dos resultados
print("---------------------------------")
print(f"\nResumo final da sua viagem à {destino}!")
print(f"\nValor total da hospedagem (R$): {calc_hospedagem:.2f}")
print(f"\nCusto total da viagem (R$): {custo_total}:.2f")

if orcamento_possivel:
    print("\nOrçamento possível.")
else:
    print("\nOrçamento não possível.")

if status_viagem:
    print("\nA viagem é viável.")
else:
    print("\nA viagem não é viável.")

if objetivo > 0:
    print(f"\nSobrará R${objetivo}:.2f com a viagem.")
else:
    print(f"\nFaltará R${abs(objetivo):.2f} com a viagem.")
