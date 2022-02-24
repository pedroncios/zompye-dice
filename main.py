# Importa a função 'randrange' do módulo 'random' para que seja
# possível obter um número randômico em um range específico
from random import randrange
# Importa o módulo time para controle de delays entre as jogadas
import time

DELAY = 1
SHOW_CUP = False


def print_bag(_cup):
    if SHOW_CUP:
        print(f'\nO copo de dados está com {len(_cup)} dados')
        print('Dados no copo:', _cup)
        input('\nPressione ENTER para continuar...')


# Define as faces de cada cor de dado
# C = Cérebro
# T = Tiro
# F = Fugitivo
green_faces = 'CCCTFF'
yellow_faces = 'CCTTFF'
red_faces = 'CTTTFF'

answer = ''
while answer.lower() != 'n':
    current_player = 0

    # Define o número de jogadores
    number_of_players = input('Bem-vindo ao Zompye Dice! Vamos jogar? Digite o número de jogadores: ')
    while not number_of_players.isnumeric() or int(number_of_players) < 2:
        number_of_players = input('Por favor digite um número de jogadores maior que 1: ')
    number_of_players = int(number_of_players)  # Converte para inteiro para facilitar o uso no restante do código

    player_names = []
    scores = []
    for i in range(number_of_players):
        # Define o nome dos jogadores
        player_names.append(input(f'Qual o nome do jogador {i + 1}? '))
        # Define a pontuação dos jogadores
        scores.append(0)

    current_round = 1
    end_of_game = False
    while not end_of_game:

        cup = ['G', 'G', 'G', 'G', 'G', 'G', 'Y', 'Y', 'Y', 'Y', 'R', 'R', 'R']
        footprints_dices = []
        round_score = 0
        shotgun_blasts = 0
        next_player_round = False

        while not next_player_round:
            print(f'\n******* Rodada {current_round} - {player_names[current_player]} *******')

            print_bag(cup)

            # O turno sempre considera os dados fugitivos do turno anterior
            dices_to_roll = footprints_dices
            footprints_dices = []
            rolled_dices = []
            footprints = 0

            # Sorteia os dados
            print('\nSorteando dados...')
            time.sleep(DELAY)
            for i in range(3 - len(dices_to_roll)):
                index = randrange(len(cup))
                dices_to_roll.append(cup[index])
                cup.remove(cup[index])
            print('Dados sorteados:', dices_to_roll)

            print_bag(cup)

            # Sorteia as faces dos dados
            print('\nJogando os dados sorteados...')
            time.sleep(DELAY)
            for dice in dices_to_roll:
                if dice == 'G':  # green
                    rolled_dices.append(green_faces[randrange(6)])
                elif dice == 'Y':  # yellow
                    rolled_dices.append(yellow_faces[randrange(6)])
                elif dice == 'R':  # red
                    rolled_dices.append(red_faces[randrange(6)])
            print('Faces que saíram:', rolled_dices)

            # Verifica as faces que saíram
            for i in range(3):
                if rolled_dices[i] == 'C':  # brains
                    round_score += 1
                elif rolled_dices[i] == 'T':  # shotgun blasts
                    shotgun_blasts += 1
                elif rolled_dices[i] == 'F':  # footprints
                    footprints += 1
                    footprints_dices.append(dices_to_roll[i])

            time.sleep(0.5)
            print('\n------ Saldo acumulado da rodada ------')
            print(f'Cérebros: {round_score}\nTiros: {shotgun_blasts}\nFugitivos: {footprints}')
            print('Dados dos fugitivos:', footprints_dices)
            print('---------------------------------------')

            # Verifica se perdeu a rodada
            if shotgun_blasts >= 3:
                print('\nVocê levou 3 tiros! Não marca pontos nessa rodada e é a vez do próximo jogador...')
                next_player_round = True
            else:
                answer = ''
                while not (answer.lower() == 's' or answer.lower() == 'n'):
                    answer = input('\nQuer tentar comer mais cérebros? (s/n) ')

                if answer == 'n':
                    # Se optar por parar computa os pontos do jogador
                    scores[current_player] += round_score
                    next_player_round = True

        # Mostra o placar atual
        print('\n------ Placar ------')
        print(f'Rodada {current_round}\n')
        for i in range(number_of_players):
            print(f'{player_names[i]}: {scores[i]} ponto(s)')
        print('--------------------')
        input('\nPressione ENTER para continuar...')

        # Define quem é o próximo jogador
        if current_player == (number_of_players - 1):
            # Todos jogaram esta rodada, verifica se alguém ganhou
            for i in range(number_of_players):
                if scores[i] >= 13:
                    print(f'\n*-*-*-*-*-*-*-* O JOGADOR {player_names[i]} VENCEU!!! *-*-*-*-*-*-*-*')
                    end_of_game = True
                    break

            if not end_of_game:
                # Volta para o primeiro jogador
                current_player = 0
                # Contabiliza a rodada, pois todos jogaram
                current_round += 1
        else:
            current_player += 1

    answer = ''
    while not (answer.lower() == 's' or answer.lower() == 'n'):
        answer = input('\nGostaria de jogar novamente? (s/n) ')
