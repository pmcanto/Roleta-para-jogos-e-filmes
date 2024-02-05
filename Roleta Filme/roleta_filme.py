import random

filmes = []

def ler_lista():
    # declara a variavel como global
    global filmes
    with open('lista_filmes.txt', 'r') as file:
        # Le todo o conteudo do arquivo e faz uma lista com ele
        lista1 = file.readlines()
    for elemento in lista1:
        # tira o \n e coloca como caixa baixa 
        filme = elemento.rstrip('\n').lower()
        filmes.append(filme)

def imprimir_lista():
    global filmes
    print('\nOs filmes em sua lista são\n')
    print('*_' * 10 + '*\n')
    i = 0
    for filme in filmes:
        i += 1
        print(i,filme)

def deletar_filme():
    # declara a variavel como global
    global filmes
    # Pede para o usuário escrever o filme sem uso de algarismo especiais e acentos
    print('Digite o filme a ser deletado, sem uso de algarismos especiais e acentos:')
    filme_del = input().lower()
    #Se o filme estiver na lista de filmes
    if filme_del in filmes:
        #deleta o filme na lista filmes
        filmes.remove(filme_del)
        #abre o arquivo e reescreve a lista, menos ele.
        with open('lista_filmes.txt', 'w') as file:
            for filme in filmes:
                file.write(f"{filme}\n")
    else:
        print(f'O filme "{filme_del}" não está na lista.')
    
def adicionar_filme():
    # declara a variavel como global
    global filmes
    # Pede para o usuário escrever o filme sem uso de algarismo especiais e acentos
    print('Digite o filme a ser adicionado, sem uso de algarismos especiais e acentos:')
    filme_add = input().lower()
    #Se o filme estiver na lista de filmes
    if filme_add in filmes:
        print(f'O filme "{filme_del}" já está na lista.')
    else:
        #adiciona o filme na lista filmes
        filmes.insert(0,filme_add)
        #abre o arquivo e reescreve a lista, mais ele.
        with open('lista_filmes.txt', 'w') as file:
            for filme in filmes:
                file.write(f"{filme}\n")

def escolher_filme ():
    # declara a variavel como global
    global filmes
    # Ve quantos filmes tem a lista
    qnt_filmes = len(filmes)
    # Escolhe um número aleátorio entre 0 e a quantidade de filmes que tem a lista
    filme_escolhido = random.randrange(0,qnt_filmes)
    #Imprime o filme escolhido
    print(f'o filme escolhido foi {filmes[filme_escolhido]} !')

def menu():
    option = 0
    while option != 5:
        #prints com as opções do usuário
        print('\nO que você gostaria de fazer hoje, cinéfilo?')
        print('\nPara ver quais filmes estão na sua watchlist, digite 1')
        print('\nPara girar uma roleta e decidir o filme que você vai assistir, digite 2')
        print('\nPara remover um filme da sua lista, digite 3')
        print('\nPara adicionar um filme a sua lista, digite 4')
        print('\nPara sair, digite 5')
        #Escolha do usuário
        option = int(input())

        #Escolhe uma opção de tarefa
        if option == 1:
            imprimir_lista()
        elif option == 2:
            escolher_filme()
        elif option == 3:
            deletar_filme()
        elif option == 4:
            adicionar_filme()
        #Se não escolher um número de 1 a 5
        if not option <= 1 and option >= 5:
            print('Opção Invalida, tente novamente')

ler_lista()
menu()
        
    
