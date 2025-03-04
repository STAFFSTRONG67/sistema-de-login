#Cadastro de usuário e senhas
# 1-Cadastre um novo usuário. 2-Faça login (senha correta). 3-Listar os usuários cadastrados. 4-Sair do programa quando desejar.

usuarios = {}

while True:
    print('\n1 - Cadastrar novo usuário')
    print('2 - Fazer login')
    print('3 - Listar usuários cadastrados')
    print('4 - Sair')

    escolha = input('Escolha uma opção: ')

    if not escolha.isdigit():   #Verificação se é número
        print('Entrada inválida. Digite um número de 1 a 4')
        continue

    escolha = int(escolha)

    if escolha == 1:
        while True:  #Verificação de usuário cadastrado
            nome = input('\nNome de usuário: ').title().strip()
            if nome not in usuarios:
                break
            print('O usuário já existe. Tente outro nome.')

        senha = input('Senha: ').strip()
        usuarios[nome] = senha
        print('Usuário cadastrado com sucesso!')

    elif escolha == 2:
        nome = input('\nNome de usuário: ').title().strip()
        if nome not in usuarios:
            print('Usuário inexistente!')
        else:
            senha = input('Senha: ').strip()
            if senha == usuarios[nome]:
                print(f'Login bem-sucedido. Bem-vindo {nome}')
            else:
                print('Senha inválida. Tente novamente')

    elif escolha == 3:
        if usuarios:
            print(f'\nUsuários cadastrados:', ', '.join(usuarios.keys()))
        else:
            print('\nNenhum usuário cadastrado')

    elif escolha == 4:
        print('Programa Encerrado. Obrigado!')
        break

    else:
        print('Entrada inválida. Escolha uma opção de 1 a 4.')
