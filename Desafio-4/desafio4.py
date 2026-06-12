#Import dos módulos necessários
import os
import json
from datetime import datetime

def processar_pasta(caminho_pasta, lista_criados, lista_removidos):
    """Função que processa um diretório, verificando se está vazio ou não.
       - Caso esteja e não tem .gitkeep: Cria o arquivo
       - Caso não esteja e tem/não tem .gitkeep: Arquivo não estará presente"""

    #Lista todos os arquivos e pastas no dir. atual
    coisas = os.listdir(caminho_pasta)

    conteudo = [item for item in coisas if item != '.gitkeep']

    #Verifica se diretório está vazio
    pasta_vazia = (len(conteudo) == 0)

    #Constrói o caminho pro gitkeep e verifica se já existe
    caminho_gitkeep = os.path.join(caminho_pasta, '.gitkeep')

    gitkeep_existente = os.path.exists(caminho_gitkeep)


    #Se a pasta estiver vazia, cria um gitkeep e adiciona a lista de arq. criados
    if pasta_vazia:
        if not gitkeep_existente:
            with open(caminho_gitkeep, 'w') as f:
                pass
            
            lista_criados.append(caminho_gitkeep)
            print(f"Criado: {caminho_gitkeep}")

    #Caso não esteja, pula/remove gitkeep e adiciona a lista de arq. removidos (se foi)
    else:
        if gitkeep_existente:
            os.remove(caminho_gitkeep)
            lista_removidos.append(caminho_gitkeep)
            print(f"Removido: {caminho_gitkeep}")



def registrar_logs(criados, removidos):
    """Registra as execuções dos programas em arquivos JSON"""

    #Define e cria caminho para a pasta logs, caso não exista, e seu arquivo
    pasta_logs = os.path.join('.', 'logs')

    os.makedirs(pasta_logs, exist_ok=True)

    arquivo_log = os.path.join(pasta_logs, 'log.json')

    #Armazena o histórico de logs
    historico_de_logs = []

    #Verifica se o arq. de log já existe, carregando o histórico, caso contrário solta um erro.
    if os.path.exists(arquivo_log):
        try:
            with open(arquivo_log, 'r', encoding='utf-8') as f:
                historico_de_logs = json.load(f)

        except json.JSONDecodeError:
            print("Erro de arquivo log.json, crie um histórico novo")

    #Registra tempo atual e coloca os dados em um novo registro no arquivo.
    tempo_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    novo_registro = {'data_hora': tempo_atual, 'gitkeeps_criados': criados, 'gitkeeps_removidos': removidos}

    historico_de_logs.append(novo_registro)

    with open(arquivo_log, 'w', encoding='utf-8') as f:
        json.dump(historico_de_logs, f, indent=2, ensure_ascii=False)

    print(f'Execução registrada em {arquivo_log}')


def processar_diretorio():
    """Percorre os diretórios"""

    #Armazena os .gitkeeps criados e removidos
    arquivos_criados = []
    arquivos_removidos = []

    #Percorre as pastas com subpastas e arquivos
    #Remove subpastas logs e git para evitar problemas
    for raiz, subpasta, arquivos in os.walk('.'):
        if 'logs' in subpasta:
            subpasta.remove('logs')

        if '.git' in subpasta:
            subpasta.remove('.git')

        #Chama a função processar_pasta para começar o trabalho
        processar_pasta(raiz, arquivos_criados, arquivos_removidos)

    return arquivos_criados, arquivos_removidos


def main():

    #Processa os diretórios
    criados, removidos = processar_diretorio()

    #Registra logs
    registrar_logs(criados,removidos)

    #Mostra o resultado da execução
    #.gitkeeps criados/removidos e data/hora
    print(f"Arquivos .gitkeep criados = {len(criados)}")
    print(f"Arquivos .gitkeep removidos = {len(removidos)}")

if __name__ == "__main__":
    main()
