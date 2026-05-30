# trilha-de-python
Python - for_code

Desafio 3:

- Explicação do funcionamento do programa:

O programa funciona inicialmente com a entrada de dados das listas de reagentes, lotes e purezas, fazendo o set das purezas para determinar quantos valores únicos que ela tem.

Em sequência, combinamos as listas por um list-zip para unir os 3 itens em uma lista de tuplas.

Depois, fazemos um relatório de cada frasco com seu lote, nome e valor, mostrando um a um.

Por fim, é usado o list comprehension para printar os lotes que tem as purezas com maior ou igual a 98%.


- Instruções de uso:

Só baixar o código inventario_lab.py e rodar em algum ambiente Python, código produzido e testado via IDLE.


- Respostas às perguntas teóricas abaixo.

-- 1. Levando em consideração a estrutura do nosso inventário, por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?

R: Por que um dicionário só guarda dois elementos sendo únicos, chave e valor. Se tivermos chaves repetidas, isso é sobrescrito e só permanecemos com uma chave. 

-- 2. O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?

R: Cria um objeto zip iterador, onde inicialmente não armazena os dados antecipadamente. Ele só tem uma referências as listas originais para gerar as tuplas através do list/dict e etc.


-- 3. Observando o seu código final, de que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?

R: O Python faz todo o trabalho comprimindo uma iteração que levaria cinco linhas em apenas uma, fazendo com que na mesma parte crie uma lista, ocorra o loop, implementa a condição if e automaticamente faz o append.
