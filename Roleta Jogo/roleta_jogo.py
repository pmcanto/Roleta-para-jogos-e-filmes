import random

jogos = []

def ler_lista():
    # declara a variável como global
    global jogos
    with open('lista_jogo.txt', 'r') as file:
        # Lê todo o conteúdo do arquivo e faz uma lista com ele
        lista1 = file.readlines()
    for elemento in lista1:
        # Tira o \n e coloca como caixa baixa
        jogo = elemento.rstrip('\n').lower()
        jogos.append(jogo)

def imprimir_lista():
    global jogos
    print('\nOs jogos em sua lista são\n')
    print('*_' * 10 + '*\n')
    i = 0
    for jogo in jogos:
        i += 1
        print(i, jogo)

def deletar_jogo():
    # declara a variável como global
    global jogos
    # Pede para o usuário escrever o jogo sem uso de algarismos especiais e acentos
    print('Digite o jogo a ser deletado, sem uso de algarismos especiais e acentos:')
    jogo_del = input().lower()
    # Se o jogo estiver na lista de jogos
    if jogo_del in jogos:
        # Deleta o jogo na lista de jogos
        jogos.remove(jogo_del)
        # Abre o arquivo e reescreve a lista, menos o jogo.
        with open('lista_jogo.txt', 'w') as file:
            for jogo in jogos:
                file.write(f"{jogo}\n")
    else:
        print(f'O jogo "{jogo_del}" não está na lista.')

def adicionar_jogo():
    # declara a variável como global
    global jogos
    # Pede para o usuário escrever o jogo sem uso de algarismos especiais e acentos
    print('Digite o jogo a ser adicionado, sem uso de algarismos especiais e acentos:')
    jogo_add = input().lower()
    # Se o jogo estiver na lista de jogos
    if jogo_add in jogos:
        print(f'O jogo "{jogo_add}" já está na lista.')
    else:
        # Adiciona o jogo na lista de jogos
        jogos.insert(0, jogo_add)
        # Abre o arquivo e reescreve a lista, mais ele.
        with open('lista_jogo.txt', 'w') as file:
            for jogo in jogos:
                file.write(f"{jogo}\n")

def escolher_jogo():
    # declara a variável como global
    global jogos
    # Ve quantos jogos tem a lista
    qnt_jogos = len(jogos)
    # Escolhe um número aleatório entre 0 e a quantidade de jogos que tem a lista
    jogo_escolhido = random.randrange(0, qnt_jogos)
    # Imprime o jogo escolhido
    print(f'O jogo escolhido foi {jogos[jogo_escolhido]}!')

def menu():
    option = 0
    while option != 5:
        # prints com as opções do usuário
        print('\nO que você gostaria de fazer hoje, gamer?')
        print('\nPara ver quais jogos estão em sua lista, digite 1')
        print('\nPara girar uma roleta e decidir o jogo que você vai jogar, digite 2')
        print('\nPara remover um jogo de sua lista, digite 3')
        print('\nPara adicionar um jogo à sua lista, digite 4')
        print('\nPara sair, digite 5')
        # Escolha do usuário
        option = int(input())

        # Escolhe uma opção de tarefa
        if option == 1:
            imprimir_lista()
        elif option == 2:
            escolher_jogo()
        elif option == 3:
            deletar_jogo()
        elif option == 4:
            adicionar_jogo()
        # Se não escolher um número de 1 a 5
        if not 1 <= option <= 5:
            print('Opção Inválida, tente novamente')

ler_lista()
menu()
