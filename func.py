def menu(msg: str):
    """
    Exibe uma mensagem centralizada e separada por dividers
    :param msg: A string a ser usada como mensagen
    """
    print('-=' * 50)
    print(msg.center(100))
    print('-=' * 50)


def opcoes(arq):
    """
    Exibe as funcionalidades disponíveis pelo aplicativo e recebe a entrada da opção desejada
    :param arq: Arquivo onde serão feitas as modificações
    :return: Retorna o valor resultante da função functions()
    """
    while True:
        print(f'{"1 - Novo Contato":<30}', end='')
        print(f'{"2 - Listar Contato":<30}', end='')
        print(f'{"3 - Buscar Contato":<30}', end='')
        print(f'{"0 - Sair":<30}')
        opcao = int()
        try:
            opcao = int(input('Opção desejada: '))
            if opcao not in [0, 1, 2, 3]:

                print('Digite uma opção válida!')
                print('-=' * 50, end='\n')
                continue
            else:
                break
        except ValueError:
            print('Digite uma opção válida!')
            print('-=' * 50, end='\n')
            continue
    return functions(opcao, arq)


def functions(opcao, arq):
    """
    Realiza o redirecionamento de funções
    :param opcao: Valor numérico coletado pela função opcoes(), cada qual referente a uma função específica
    :param arq: O arquivo onde as alterações serão realizadas
    :return: Mensagem de despedida e número 0 para o caso da opção 0, caso contrário,
    redireciona para a função correspondente a cada opção
    """
    if opcao == 1:
        cadastrar(arq)
    elif opcao == 2:
        listar(arq)
    elif opcao == 3:
        buscarcontato(arq)
    else:
        print('Saindo do programa!')
        return 0


def checararquivo(arq: str):
    """
    Checa a existência de um determinado arquivo na máquina do usuário
    :param arq: O nome do arquivo a ser verificado
    :return: True se o arquivo existir, False se não existir
    """
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq: str):
    """
    Cria um arquivo de texto simples vazio
    :param arq: O nome a ser designado ao arquivo
    """
    a = open(arq, 'x', encoding='utf-8')
    a.close()
    print(f'Arquivo {arq} criado com sucesso!')


def cadastrar(arq):
    """
    Faz a coleta dos inputs de Nome, E-mail e Telefone do contato e os adiciona no arquivo de texto
    :param arq: O arquivo de texto onde se deseja salvar as informações
    """
    a = open(arq, 'at', encoding='utf-8')
    while True:
        nome_contato = str(input('Nome do contato: ')).strip().capitalize()
        if nome_contato == '':
            nome_contato = 'Desconhecido'
            break
        elif not (nome_contato.isalpha()):
            print('Digite um nome válido!')
            continue
        else:
            break
    while True:
        email = str(input('E-mail do contato: ')).strip()
        if not (email.isascii() or email.__contains__(' ')):
            print('Digite um E-mail válido!')
            continue
        else:
            break
    while True:
        telefone = str(input('Telefone do contato: ')).strip()
        if not (telefone.isalnum() or telefone.__contains__(' ')):
            print('Digite um Telefone válido e não utilize espaços!')
            continue
        else:
            break
    a.write(f'{nome_contato};{email};{telefone}\n')
    a.close()
    print('Contato cadastrado com sucesso!', '\n')


def buscarcontato(arq: str):
    """
    Coleta um input referente ao contato a ser buscado na lista de contatos e
    exibe as informações do contato caso ele já exista
    :param arq: O nome do arquivo onde estão armazenados os dados
    :return:
    """
    while True:
        nome = str(input('Digite o nome a ser buscado: '))
        if not (nome.isalpha()):
            print('Digite um nome válido!')
            continue
        else:
            break
    a = open(arq, 'r')
    info = {'Nome': [], 'Email': [], 'Telefone': []}
    for i in a:
        line = i.lower().replace('\n', '').split(';')
        if nome.lower() in line:
            info['Nome'].append(line[0])
            info['Email'].append(line[1])
            info['Telefone'].append(line[2])
    if len(info['Nome']) > 0:
        print(f'{nome} foi localidado na lista de contatos.')
        print('-=' * 40)
        print(f'{"NOME":<25}', end='')
        print(f'{"E - MAIL":<37}', end='')
        print(f'{"TELEFONE":>10}')
        print('*' * 80)
        for i, v in enumerate(info['Nome']):
            print(f"{info['Nome'][i]}{info['Email'][i]:^50}{info['Telefone'][i]:^25}")
        print('*' * 80, end='\n')
    else:
        print(f'{nome} não foi localizado na lista de contatos.', '\n')


def listar(arq: str):
    """
    Exibe os contatos presentes no arquivo de forma tabulada e formatada
    :param arq: O nome do arquivo contendo os dados dos contatos
    """
    a = open(arq, 'r', encoding='utf-8')
    if a:
        print('-=' * 40)
        print(f'{"NOMES":<20}', end='')
        print(f'{"E - MAILS":<30}', end='')
        print(f'{"TELEFONES":>20}')
        print('-=' * 40)
        for line in a:
            line = line.replace('\n', '')
            dado = line.split(';')
            print(f'{dado[0]:<20}{dado[1]:<41}{dado[2]}')
        print('-=' * 40)
    else:
        print('Não há contatos cadastrados!')
