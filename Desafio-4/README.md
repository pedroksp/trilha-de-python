# trilha-de-python
Python - for_code

Desafio 4:

- Explicação do funcionamento do programa:

O programa funciona percorrendo os diretórios do repositório local com a função processar_diretorio(), que varre e armazena os arquivos criados e removidos e faz uma limpeza inicial pra evitar problemas. A mesma chama a função de processar pasta, que lista todos os arquivos no diretório atual, verifica se está vazio e faz a iteração de criar o .gitkeep ou não dado seu caso específico.

Em seguida, a função de registrar logs faz com que crie uma pasta de logs caso não exista e cria um arquivo de log com o registro usando o tempo atual.

Por fim, a exibição de resultados é processada no main com a quantidade arquivos criados e removidos e a ação realizada.

- Instruções de uso:

Só baixar e rodar em algum ambiente Python, código produzido e testado via IDLE.


- Respostas às perguntas teóricas abaixo.

Explique as diferenças entre:

-- json.dump() vs json.dumps()

R: Ambos serializam objetos Python para o JSON, mas há diferenças no destino, json.dump() grava em um arquivo enquanto json.dumps() retorna uma string JSON.

-- json.load() vs json.loads()

R: Nesse caso, ambos agora desserializam JSON para Python, onde json.load() lê um arquivo e json.loads() lê uma string.

