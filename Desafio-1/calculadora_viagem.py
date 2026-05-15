#Valor da cotação do euro-real
cotacao_euro = 6.10

#Função que valida se os números digitados int/float são positivos, caso contrário chama o ValueError
def valida_num(valor):
    if valor < 0:
        raise ValueError("Valores negativos não podem ser digitados!")
    
    return valor

#"Loop" das entradas
#Se alguma entrada estiver inválida ou com valor númerico negativo encerra o programa imediatamente.

while True:
    try:
        orcamento_disponivel = valida_num(float(input("Digite o orçamento disponível em R$: ")))

        destino = str(input("\nDigite o local (país/cidade) da viagem: "))

        custo_passagem = valida_num(float(input("\nDigite o custo da passagem em R$: ")))

        custo_diario_hospedagem = valida_num(float(input("\nDigite o custo diário da hospedagem em EUR (Euros): ")))

        qntd_dias = valida_num(int(input("\nInforme a quantidade de dias da viagem: ")))

        break

    except ValueError as e:
        if "negativos" in str(e):
            print(f"\n{e}")

        else:
            print("\nEntrada inválida!")

        print("Operação encerrada.")
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
print(f"\nCusto total da viagem (R$): {custo_total:.2f}")

if orcamento_possivel:
    print("\nOrçamento possível.")
else:
    print("\nOrçamento não possível.")

if status_viagem:
    print("\nA viagem é viável.")
else:
    print("\nA viagem não é viável.")

if objetivo > 0:
    print(f"\nSobrará R${objetivo:.2f} com a viagem.")
else:
    print(f"\nFaltará R${abs(objetivo):.2f} para a viagem.")
