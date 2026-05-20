# trilha-de-python
Python - for_code

Desafio 2:

- Explicação do funcionamento do programa:

O programa funciona inicialmente com a entrada de dados pelo próprio usuário, usando 2 try e except (caso digitar string em um float), e se algum dos valores númericos forem negativos, nulos ou as entradas forem inválidas, o programa encerra imediatamente apontando de qual monstro deu o erro.

Em seguida, criado a função de atacar que fornecido os dados de cada monstro, define o novo HP do defensor subtraindo do ataque sofrido, caso o ataque deixe ele com vida negativa, seu hp vai pra 0.

Depois, feito a exibição de placar que printa após cada ataque de cada monstro os status atuais.

Por fim, feito um loop com while para os turnos que roda conforme a condição dos HPs de ambos serem maiores que 0. A cada turno (iteração do loop), cada monstro ataca e exibe o placar após o ataque. Quando um dos monstros zerarem o seu HP, sai do loop e roda a condição de vitória.


- Instruções de uso:

Só baixar o código simulador_tcg.py e rodar em algum ambiente Python, código produzido e testado via IDLE.


- Respostas às perguntas teóricas abaixo.

-- 1. Qual é a principal diferença prática entre usar um laço for e um laço while em Python? Por que o while foi a melhor escolha para este duelo?

R: O laço for repete até uma certa contagem de vezes definida ou até onde sabe quantas vezes vai repetir. No while, não sabemos, e por isso ele repete enquanto uma condição for verdadeira, nesse caso usado o HPs > 0.


-- 2. Para que serve a palavra-chave return dentro de uma função? O que acontece se uma função fizer um cálculo matemático mas não possuir o return?

R: O comando return serve para devolver um resultado ou encerrar uma função, se não tiver return na função em um cálculo matemático, ele retornará None.

-- 3. O que é um "Loop Infinito" e como podemos evitá-lo ao construir uma
estrutura while?

R: Loop Infinito é quando aquela parte de um laço do código que fica rodando infinitamente pois nunca atinge a condição de parada, no while para evitarmos isso podemos fazer de várias formas, desde atualizarmos uma condição ou dar um break.
