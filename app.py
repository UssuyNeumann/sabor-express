import os

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
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear')
    print('Encerrando o sistema.\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal.')
    main()

def escolher_opcao():
    #snake_case
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}') #interpolação de strings
    
    match opcao_escolhida:
        case 1:
            print('Cadastrar Restaurante')
        case 2:
            print('Listar Restaurante')
        case 3:
            print('Ativar Restaurante')
        case 4: 
            finalizar_app()
        case _:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()