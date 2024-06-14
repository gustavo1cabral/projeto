lista = []
filmes = {}
login = None
senha = None
login1 = None
senha1 = None
filme3 = None
salas = None
horas = None
capacidade = None
valor_ingressos = None
preco_pipoca = None


def cadastrar_usuario(tipo):
    global lista, login, senha, login1, senha1
    if tipo == 'adm':
        login = input('Digite seu login: ')
        lista.append(login)
        print('Login salvo.')
        senha = input('Digite sua senha: ')
        lista.append(senha)
        print('Senha salva.')



    elif tipo == 'cliente':
        login1 = input('Digite seu login: ')
        lista.append(login1)
        print('Login salvo.')
        senha1 = input('Digite sua senha: ')
        lista.append(senha1)
        print('Senha salva.')
        usuario = {'login': login1, 'senha': senha1}
        print(usuario)


def menu_adm():
    global filmes

    adm = input('Digite seu login: ')
    if adm == login:
        pass
    else:
        return
    adm_senha = input('Digite sua senha: ')

    if adm_senha == senha:
        pass
    else:
        return

    while True:
        print('\nMenu de Administração')
        print('1 - Cadastrar filme')
        print('2 - Buscar filme')
        print('3 - Atualizar filme')
        print('4 - Remover filme')
        print('5 - Ingressos disponíveis')
        print('6 - Todos os ingressos vendidos')
        print('7 - Listar os ingressos vendidos para um filme especifico')
        print('8 - dinheiro arrecadado')
        print('0 - Sair')
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            filmes = []

            titulo1 = input('Qual filme deseja cadastrar? ')
            filmes.append(titulo1)

            sala = input('Qual sala vai passar o filme? ')
            filmes.append(sala)

            horario = input('Qual horário vai passar o filme? ')
            filmes.append(horario)

            capacidade = int(input('Quantas pessoas podem assistir o filme? '))
            if (capacidade > 0):
                pass
            else:
                return
            filmes.append(capacidade)

            valor_ingresso = float(input('Qual o valor dos ingressos? '))
            if (valor_ingresso > 0):
                pass
            else:
                return
            filmes.append(valor_ingresso)

            preco_pipoca = float(input('Preço da pipoca? '))
            if (preco_pipoca > 0):
                pass
            else:
                return
            filmes.append(preco_pipoca)

            ingressos_vendidos = 0
            filmes.append(ingressos_vendidos)

            dinheiro_arrecadado = 0
            filmes.append(dinheiro_arrecadado)

            print('Filme cadastrado com sucesso.')

        elif opcao == '2':

            print(filmes)


        elif opcao == '3':
            buscar = input('Digite o filme para atualizar: ')
            if buscar in filmes:
                novo_filme = input('Digite o novo filme: ')
                filmes[filmes.index(buscar)] = novo_filme
                print('Filme atualizado.')
            else:
                print('Filme não encontrado.')


        elif opcao == '4':
            remover = input('Digite o filme para remover: ')
            if remover in filmes:
                filmes.remove(remover)
                print('Filme removido.')
            else:
                print('Filme não encontrado.')


        elif opcao == '5':
            print(filmes[3])


        elif (opcao == '6'):
            print(f'{filmes[6]} foram vendidos')


        elif opcao == '7':
            nome = input('Digite o título do filme para listar os ingressos vendidos: ')
            for filme in filmes:
                if (filmes[0] == nome):
                    print(f'Ingressos vendidos para {nome}: {filmes[6]}')
                else:

                    print('Filme não encontrado.')

        elif (opcao == '8'):
            print(filmes[7])


        elif opcao == '0':
            print('Saindo do menu de administração.')
            break


def comprar_ingressos():
    global lista, capacidade, volor_ingresso, valor_pipoca
    cliente = input('Digite seu login: ')
    if cliente == login1:
        pass
    elif cliente == login:
        print('Adm não pode comprar ingresso.')
        return
    else:
        return

    cliente1 = input('Digite sua senha: ')
    if cliente1 == senha1:
        print('Bem-vindo.')

    else:
        print('Senha incorreta.')

    anos = int(input('quantos anos voçe tem'))
    if (anos > 17):

        print(f'Filmes disponíveis: {filmes[0]}')
        filme_escolhido = input('Qual filme você vai assistir? ')

        for filme in filmes[0]:
            if (filmes[0] == filme_escolhido):
                print('filme escolhido com sucesso')
                pass
            else:
                print('Filme não encontrado.')
                return

        print(f'O ingresso custa: {filmes[4]}')
        print(f'ingressos disponiveis {filmes[3]}')

        comprar = int(input('Quantos ingressos você vai comprar? '))

        if (comprar <= filmes[3]):
            filmes[3] -= comprar
            filmes[6] = comprar
            print('ingresso comprado com sucwsso')
            pass
        else:
            print('numero de ingresso indisponivel.')
            return

        print(f'a pipoca custa {filmes[5]}')
        pipocas = int(input('Quantas pipocas deseja comprar? '))
        print('pipoca comprada com sucesso')
        filmes[7] = comprar * filmes[4] + pipocas * filmes[5]

        print(f'voçe comprou {comprar} ingresso para o filme {filmes[0]} e comprou {pipocas} pipocas')

    else:

        print(f'Filmes disponíveis: {filmes[0]}')
        filme_escolhido = input('Qual filme você vai assistir? ')

        for filme in filmes[0]:
            if (filmes[0] == filme_escolhido):
                print('filme escolhido com sucesso')
                pass
            else:
                print('Filme não encontrado.')
                return

        print(f'O ingresso custa: {filmes[4] * 0.50}')
        print(f'ingressos disponiveis {filmes[3]}')

        comprar = int(input('Quantos ingressos você vai comprar? '))

        if (comprar <= filmes[3]):
            filmes[3] -= comprar
            filmes[6] = comprar
            print('ingresso comprado com sucwsso')
            pass
        else:
            print('numero de ingresso indisponivel.')
            return

        filmes[3] -= comprar
        filmes[6] = comprar
        print('ingresso comprado com sucwsso')

        pipocas = int(input('Quantas pipocas deseja comprar? '))
        print('ingresso comprado com sucesso')

        filmes[7] = (comprar * filmes[4] * 0.50) + (pipocas * filmes[5] * 0.50)

        print(f'voçe comprou {comprar} ingresso para o filme {filmes[0]} e comprou {pipocas} pipocas')


while True:
    print('\nMenu Principal')
    print('1 - Administração')
    print('2 - Comprar ingressos')
    print('3 - Gerenciar login')
    print('0 - Sair')
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        menu_adm()

    elif opcao == '2':
        comprar_ingressos()

    elif opcao == '3':
        cadastrar = input('Digite 0 para adm ou 1 para cliente: ')

        if cadastrar == '0':
            cadastrar_usuario('adm')
        elif cadastrar == '1':
            cadastrar_usuario('cliente')

    elif opcao == '0':
        print('Saindo do programa.')
        break