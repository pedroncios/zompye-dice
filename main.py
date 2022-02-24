# Importa a função 'randrange' do módulo 'random' para que seja
# possível obter um número randômico em um range específico
from random import randrange
# Importa o módulo time para controle de delays entre as jogadas
import time

DELAY = 1

# Define as faces de cada cor de dado
# C = Cérebro
# T = Tiro
# F = Fugitivo
facesVerde = 'CCCTFF'
facesAmarelo = 'CCTTFF'
facesVermelho = 'CTTTFF'

answer = ''
while answer.lower() != 'n':
    nJogadores = 0
    jogadorAtual = 0

    # Define o número de jogadores
    nJogadores = input('Bem-vindo ao Zompye Dice! Vamos jogar? Digite o número de jogadores: ')
    while not nJogadores.isnumeric() or int(nJogadores) < 2:
        nJogadores = input('Por favor digite um número de jogadores maior que 1: ')
    nJogadores = int(nJogadores)  # Converte para inteiro para facilitar o uso no restante do código

    nomesJogadores = []
    pontuacao = []
    for i in range(nJogadores):
        # Define o nome dos jogadores
        nomesJogadores.append(input(f'Qual o nome do jogador {i+1}? '))
        # Define a pontuação dos jogadores
        pontuacao.append(0)

    rodadaAtual = 1
    fimDeJogo = False
    while not fimDeJogo:

        copo = ['G', 'G', 'G', 'G', 'G', 'G', 'Y', 'Y', 'Y', 'Y', 'R', 'R', 'R']
        dadosFugitivos = []
        pontos = 0
        tiros = 0
        vezDoProxJogador = False

        while not vezDoProxJogador:
            print(f'\n*** Rodada {rodadaAtual} - {nomesJogadores[jogadorAtual]} ***')

            print(f'\nO copo está com {len(copo)} dados')
            print('Dados no copo:', copo)
            input('\nPressione ENTER para continuar...')

            # O turno sempre considera os dados fugitivos do turno anterior
            dadosSorteados = dadosFugitivos
            dadosFugitivos = []
            facesSorteadas = []
            fugitivos = 0

            # Sorteia os dados
            print('\nSorteando dados...')
            time.sleep(DELAY)
            for i in range(3-len(dadosSorteados)):
                index = randrange(len(copo))
                dadosSorteados.append(copo[index])
                copo.remove(copo[index])
            print('Dados sorteados:', dadosSorteados)

            print(f'\nO copo está com {len(copo)} dados')
            print('Dados no copo:', copo)
            input('\nPressione ENTER para continuar...')

            # Sorteia as faces dos dados
            print('\nJogando os dados sorteados...')
            time.sleep(DELAY)
            for dice in dadosSorteados:
                if dice == 'G':  # green
                    facesSorteadas.append(facesVerde[randrange(6)])
                elif dice == 'Y':  # yellow
                    facesSorteadas.append(facesAmarelo[randrange(6)])
                elif dice == 'R':  # red
                    facesSorteadas.append(facesVermelho[randrange(6)])
            print('Faces que saíram:', facesSorteadas)

            # Verifica as faces que saíram
            for i in range(3):
                if facesSorteadas[i] == 'C':  # cérebro
                    pontos += 1
                elif facesSorteadas[i] == 'T':  # tiro
                    tiros += 1
                elif facesSorteadas[i] == 'F':  # fugitivos
                    fugitivos += 1
                    dadosFugitivos.append(dadosSorteados[i])

            print('\n------ Saldo acumulado da rodada ------')
            print(f'Cérebros: {pontos}\nTiros: {tiros}\nFugitivos: {fugitivos}')
            print('Dados dos fugitivos:', dadosFugitivos)
            print('---------------------------------------')

            # Verifica se perdeu a rodada
            if tiros >= 3:
                print('\nVocê levou 3 tiros! Não marca pontos nessa rodada e é a vez do próximo jogador...')
                input('\nPressione ENTER para continuar...')
                vezDoProxJogador = True
            else:
                answer = ''
                while not (answer.lower() == 's' or answer.lower() == 'n'):
                    answer = input('\nQuer tentar comer mais cérebros? (s/n) ')

                if answer == 'n':
                    # Se optar por parar computa os pontos do jogador
                    pontuacao[jogadorAtual] += pontos
                    vezDoProxJogador = True

        # Mostra o placar atual
        print('\n------ Placar ------')
        print(f'Rodada {rodadaAtual}\n')
        for i in range(nJogadores):
            print(f'{nomesJogadores[i]}: {pontuacao[i]} ponto(s)')
        print('--------------------')
        input('\nPressione ENTER para continuar...')

        # Define quem é o próximo jogador
        if jogadorAtual == (nJogadores - 1):
            # Todos jogaram esta rodada, verifica se alguém ganhou
            for i in range(nJogadores):
                if pontuacao[i] >= 13:
                    print(f'\n*-*-*-*-*-*-*-* O JOGADOR {nomesJogadores[i]} VENCEU!!! *-*-*-*-*-*-*-*')
                    fimDeJogo = True
                    break

            if not fimDeJogo:
                # Volta para o primeiro jogador
                jogadorAtual = 0
                # Contabiliza a rodada, pois todos jogaram
                rodadaAtual += 1
        else:
            jogadorAtual += 1

    answer = ''
    while not (answer.lower() == 's' or answer.lower() == 'n'):
        answer = input('\nGostaria de jogar novamente? (s/n) ')
