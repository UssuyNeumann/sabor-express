import os

#criando lista vazia
restaurantes = []

def exibir_nome_do_programa():
    print("""
███████╗ █████╗ ██████╗  ██████╗ ██████╗     ███████╗██╗  ██╗██████╗ ██████╗ ███████╗███████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
███████╗███████║██████╔╝██║   ██║██████╔╝    █████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ███████╗███████╗
╚════██║██╔══██║██╔══██╗██║   ██║██╔══██╗    ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
███████║██║  ██║██████╔╝╚██████╔╝██║  ██║    ███████╗██╔╝ ██╗██║     ██║  ██║███████╗███████║███████║
╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
""")
#print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar/inativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o sistema')

def opcao_invalida():
    #docstring 
    '''
    Essa função exibe mensagem opção invalida e volta ao menu

    Outputs:
    - exibe a mensagem e retorna ao menu principal  
    '''
    print('Opção Inválida!\n')
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    # os.system('clear')
    linha = '=' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    #docstring 
    '''
    Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - nome do restaurante
    - categoria 

    Outputs:
    - adiciona um novo restaurante e categoria a lista de restaurantes 
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    nome_categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    #criar um dicionario {'chave':valor}
    dados_restaurante = {'nome':nome_restaurante, 'categoria':nome_categoria , 'ativo':False}
    #atribui o dicionario a lista []
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante foi {nome_restaurante} cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Lista de restaurantes cadastrados')
    print(f"{'Nome'.ljust(23)} | {'Categoria'.ljust(20)} | Status")
    
    try:
        for restaurante in restaurantes:
        # print(f'.{restaurante} ')
            nome = restaurante['nome']
            categoria = restaurante['categoria']
            #ternario
            ativo = 'ativo' if restaurante['ativo'] else 'inativo'
            print(f' - {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
            voltar_menu_principal()
    except:
        print('Cadastro Vazio.')
        voltar_menu_principal()

def alterar_status_restaurante():
    exibir_subtitulo('Alterando Status do Restaurante')
    nome = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado =  False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado: 
        print('O restaurante não foi encontrado.')
    
    voltar_menu_principal()

def escolher_opcao():
    try:
        #snake_case
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}') #interpolação de strings
        
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alterar_status_restaurante()
            case 4: 
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida() 

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()