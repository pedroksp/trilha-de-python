# trilha-de-python
Python - for_code

- Explicação do funcionamento do programa:

O programa funciona inicialmente com a entrada de dados pelo próprio usuário, usando try e except (caso digitar string em um float), e se algum dos valores númericos forem negativos ou as entradas forem inválidas, o programa encerra imediatamente.

Em seguida, fazemos os cálculos da viagem usando a cotação do euro definido no início do código e pelas entradas definidas pelo usuário, assim calculando custos, status, orçamento e etc.

Por fim, a exibição de resultados com f-strings e verificação por if/else das variáveis definidas do orçamento possível, status da viagem e objetivo.


- Instruções de uso:

Só baixar e rodar em algum ambiente Python, código produzido e testado via IDLE.


- Respostas às perguntas teóricas abaixo.

-- Qual a diferença entre o comando git add . e git commit -m "mensagem"?

R: git add . adiciona todo o conteúdo alterado na pasta atual, enquanto o git commit -m adiciona um commit com tudo que está sendo preparado com os arquivos do git add;

-- Por que é necessário realizar o casting (conversão de tipo) ao usar a função input() em Python para cálculos matemáticos?

R: O comando input é do tipo str (string), sendo assim todo dado recebido se tornará automaticamente um string.

-- O que acontece se tentarmos somar uma variável do tipo str com uma do tipo float? 

R: Erro, pois uma string não pode ser somada com um float. O operador da soma pode ser usado apenas string para string como concatenação.
