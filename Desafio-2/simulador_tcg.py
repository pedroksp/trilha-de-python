#Função que valida os valores inteiros digitados, se forem nulos/negativos, encerra o programa imediatamente
def valida_num(valor):
    if valor < 0:
        raise ValueError("Valores negativos são inválidos! Tente novamente!")
    
    elif valor == 0:
        raise ValueError("Valores nulos são inválidos! Tente novamente!")
        
    return valor

#Loops de entrada para o Monstro 1 e 2
while True:
    try:
        nome_m1 = str(input("Digite o nome do Monstro 1: "))

        hp_m1 = valida_num(int(input("Digite os pontos de vida (HP) do Monstro 1: ")))

        pts_ataque_m1 = valida_num(int(input("Digite os pontos de ataque do Monstro 1: ")))

    except ValueError as e:
        if "nulos" in str(e) or "negativos" in str(e):
            print(f"\nErro no Monstro 1: {e}")

        else:
            print("\nAlguma entrada não foi aceita no Monstro 1.")

        print("Operação encerrada.")
        exit()

while True:
    try:
        nome_m2 = str(input("Digite o nome do Monstro 2: "))

        hp_m2 = valida_num(int(input("Digite os pontos de vida (HP) do Monstro 2: ")))

        pts_ataque_m2 = valida_num(int(input("Digite os pontos de ataque do Monstro 2: ")))

    except ValueError as e:
        if "nulos" in str(e) or "negativos" in str(e):
            print(f"\nErro no Monstro 2: {e}")

        else:
            print("\nAlguma entrada não foi aceita no Monstro 2.")

        print("Operação encerrada.")
        exit()


def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    print(f"{nome_atacante} atacou {nome_defensor} causando {ataque} de dano!\n") 

    hp_defensor = hp_defensor - ataque

    if hp_defensor < 0:
        hp_defensor = 0

    print(f"{nome_defensor} agora tem {hp_defensor} de vida.\n")
    
    return hp_defensor


def exibir_placar(nome1, hp1, nome2, hp2):
    print(f"Após o turno, temos:\n {nome1} com {hp1} de vida\n {nome2} com {hp2} de vida.\n")
        
        

        
